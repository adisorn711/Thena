# Customer Tag Pipeline — Implementation Spec
**Version**: 1.0 | **Date**: 2026-04-15
**Author**: Tee × Thena
**Status**: Ready for Engineering

---

## 1. Overview

Pipeline นี้แปลง raw transaction data → Customer Tags พร้อม confidence score
เพื่อใช้ใน campaign targeting, product personalization, และ ML feature engineering

### Input → Output

```
Transaction Table (12m rolling)
+ Merchant Tag Table
         ↓
  Customer Tag Pipeline
         ↓
customer_tag_output table (refreshed daily)
```

### Output Schema

```sql
customer_id     VARCHAR   -- รหัสลูกค้า
customer_tag    VARCHAR   -- ชื่อ tag เช่น 'frequent_diner'
tag_type        VARCHAR   -- 'scored' หรือ 'binary'
score           FLOAT     -- 0.0–1.0 (binary = 0 หรือ 1 เท่านั้น)
path            VARCHAR   -- 'A' (no enrichment) หรือ 'B' (enrichment)
as_of_date      DATE      -- วันที่รัน pipeline
```

### ตัวอย่าง Output

```
customer_id | customer_tag      | tag_type | score | path | as_of_date
C001        | frequent_diner    | scored   | 0.82  | A    | 2026-04-15
C001        | ev_driver         | binary   | 1.0   | A    | 2026-04-15
C001        | japanese_food_lover | scored | 0.61  | B    | 2026-04-15
C002        | high_spender      | scored   | 0.74  | A    | 2026-04-15
```

---

## 2. Input Tables

### 2.1 Transaction Table

| Column | Type | หมายเหตุ |
|--------|------|---------|
| `customer_id` | VARCHAR | รหัสลูกค้า |
| `merchant_tag` | VARCHAR | format: `<MCC>_<merchant_name>` เช่น `Dining_Fuji` |
| `merchant_name` | VARCHAR | ชื่อ merchant raw |
| `amount` | FLOAT | จำนวนเงิน (THB) |
| `txn_date` | DATE | วันที่ทำรายการ |
| `txn_hour` | INT | ชั่วโมงที่ทำรายการ (0–23) |
| `txn_day_of_week` | INT | 1=จันทร์, 7=อาทิตย์ |
| `currency` | VARCHAR | 'THB' หรือสกุลต่างประเทศ |
| `channel` | VARCHAR | 'online', 'in_store', 'app' |
| `payment_method` | VARCHAR | 'tap', 'chip', 'swipe', 'qr' |
| `installment_flag` | BOOLEAN | true = เป็น installment |
| `txn_type` | VARCHAR | 'purchase', 'cash_advance' |
| `credit_utilization` | FLOAT | % การใช้วงเงิน ณ วันนั้น |

### 2.2 Merchant Tag Table

| Column | Type | หมายเหตุ |
|--------|------|---------|
| `merchant_tag` | VARCHAR | format เดียวกับ transaction |
| `customer_tag` | VARCHAR | customer tag ที่ map ถึง |

> ใช้สำหรับ Path B (Enrichment) เท่านั้น
> Path A ใช้ rule table แทน (ดู Section 4)

---

## 3. Pipeline Architecture

### Full Flow

```
[Daily Trigger — 01:00 น.]
         │
         ▼
[Step 1] Filter transactions 12m rolling window
         WHERE txn_date >= CURRENT_DATE - 365
         │
         ▼
[Step 2] Extract MCC prefix
         mcc_prefix = SPLIT_PART(merchant_tag, '_', 1)
         │
         ├────────────────────┬
         ▼                    ▼
    [Path A]              [Path B]
    Join กับ           Join กับ
    MCC Rule Table     Merchant Tag Table
    117 tags           34 tags
         │                    │
         └─────────┬──────────┘
                   ▼
[Step 3] Aggregate per customer × customer_tag
         txn_count, total_spend, last_txn_date, distinct_merchant
         │
         ▼
[Step 4] Calculate score
         Scored tags  → freq + recency + breadth formula
         Binary tags  → exists check → 0 or 1
         │
         ▼
[Step 5] Apply threshold
         Scored: score ≥ 0.3 → include
         Binary: score = 1 → include
         │
         ▼
[Step 6] Write to customer_tag_output
         (replace partition as_of_date = today)
```

---

## 4. Path A — MCC Rule Table

Rule table เต็มอยู่ที่: `lab/path_a_rule_table.md`

### Signal Sub-types

| Sub-type | Logic | ตัวอย่าง tag |
|----------|-------|-------------|
| **A1** | MCC prefix เท่านั้น | `frequent_diner`, `pharmacy_regular` |
| **A2** | MCC prefix + Merchant keyword match | `fast_food_regular`, `grab_dependent` |
| **A3** | MCC prefix + Amount threshold | `fine_dining_enthusiast`, `budget_eater` |
| **A4** | MCC prefix + Timestamp filter | `brunch_person`, `late_night_diner` |
| **A5** | MCC combination (หลาย prefix) | `car_owner`, `health_conscious` |
| **A6** | Pure behavioral (ไม่ขึ้น MCC) | `high_spender`, `consistent_spender` |
| **A7** | Recurring pattern detection | `subscription_stacker`, `gym_member` |

### Merchant Keyword Matching

```sql
-- extract merchant name จาก merchant_tag
merchant_name_part = LOWER(SPLIT_PART(merchant_tag, '_', 2))

-- match กับ keyword list
merchant_name_part LIKE '%mcdonald%'
OR merchant_name_part LIKE '%kfc%'
```

---

## 5. Scoring Logic

### 5.1 Tag Types

| Tag Type | คำอธิบาย | score range |
|----------|---------|-------------|
| **Scored** | คำนวณจาก frequency + recency + breadth | 0.0 – 1.0 |
| **Binary** | มี transaction ตามเงื่อนไข = 1, ไม่มี = 0 | 0 หรือ 1 |

> Binary tag เปรียบได้กับ **categorical feature** (presence/absence)
> Scored tag เปรียบได้กับ **continuous/normalized numeric feature**
> ทั้งสองใช้งานร่วมกันได้โดยตรงใน ML feature set และ campaign rule engine

### 5.2 Scored Tags — Formula

```
freq_score    = LOG(txn_count + 1) / LOG(P95_txn_count + 1)
recency_score = EXP(−days_since_last_txn / 90)
breadth_score = LOG(distinct_merchant + 1) / LOG(P95_distinct_merchant + 1)

final_score   = (0.4 × freq_score)
              + (0.4 × recency_score)
              + (0.2 × breadth_score)
```

**หมายเหตุ**:
- P95 คำนวณจากลูกค้าทั้ง portfolio (per tag) ณ วันที่รัน
- Tags ที่มี signal เดียว (เช่น A6: financial behavior) ปรับ weight ตามความเหมาะสม

### 5.3 Binary Tags — List

Tags ต่อไปนี้ใช้ binary scoring:

```
airbnb_user, ev_driver, crypto_curious, cash_advance_user,
social_commerce_buyer, secondhand_buyer, theme_park_visitor,
airbnb_user, dental_care_conscious, eye_care_regular,
maternal_care (co-occurrence), new_parent (spike detection)
```

เงื่อนไข: `txn_count ≥ N ตามที่กำหนดใน rule table → score = 1.0`

### 5.4 Threshold

```
Scored tags : score ≥ 0.3 → assign tag (active)
Binary tags : score = 1   → assign tag (active)
```

> Global threshold 0.3 ใช้ได้กับทุก tag ใน Phase 1
> ปรับ per-tag ได้ใน Phase 2 หลังมีข้อมูล distribution จริง

---

## 6. Refresh Schedule

| Parameter | Value |
|-----------|-------|
| Cadence | Daily |
| Trigger time | 01:00 น. (หลัง EOD batch) |
| Method | Full recalculation (Option A) |
| Lookback window | 12 months rolling (365 วัน) |
| Output | Replace partition `as_of_date = today` |

**Full recalculation** เลือกเพราะ:
- Data volume ยังไม่ใหญ่
- Cloud compute — cost acceptable
- Implementation ง่าย ไม่ต้องจัดการ incremental state

---

## 7. Quick Win — Phase 1 Tags (แนะนำเริ่มก่อน)

Tags ที่ signal ชัดเจน ไม่ต้องการ column พิเศษ implement ได้เร็วที่สุด:

| # | Tag | Sub-type | Signal หลัก |
|---|-----|----------|------------|
| 1 | `frequent_diner` | A1 | Dining MCC, txn count |
| 2 | `convenience_store_addict` | A2 | 7-Eleven/FamilyMart count |
| 3 | `grocery_regular` | A2 | Tops/BigC/Lotus count |
| 4 | `grab_dependent` | A2 | Grab txn count |
| 5 | `high_spender` | A6 | Total spend vs P75 |
| 6 | `mid_spender` | A6 | Total spend P25–P75 |
| 7 | `low_spender` | A6 | Total spend vs P25 |
| 8 | `marketplace_shopper` | A2 | Shopee/Lazada count |
| 9 | `streaming_subscriber` | A7 | Netflix/Disney+ recurring |
| 10 | `car_owner` | A5 | Fuel + Parking + Auto service combo |

---

## 8. Tags ที่ต้องระวัง (Complex)

| Tag | ความซับซ้อน | เหตุผล |
|-----|------------|-------|
| `last_minute_booker` | สูง | ต้องการ booking date ≠ travel date |
| `early_planner` | สูง | เช่นเดียวกัน |
| `empty_nester` | สูง | ต้องการ YoY trend comparison |
| `new_parent` | กลาง | spike detection จาก prior period |
| `multi_card_user` | กลาง | inference จาก pattern เท่านั้น |

> แนะนำ: defer tags เหล่านี้ไป Phase 2

---

## 9. Files Reference

| File | คำอธิบาย |
|------|---------|
| `lab/path_a_rule_table.md` | Rule table ครบ 117 tags พร้อม thresholds |
| `lab/customer_tag_library.md` | Tag definitions ครบ 151 tags |
| `lab/customer_tag_library_by_enrichment.md` | แยก 117 (Path A) vs 34 (Path B) |
| `lab/customer_tag_pipeline_spec.md` | ไฟล์นี้ — full spec |

---

## 10. Out of Scope (Phase 1)

- Path B (Enrichment tags) — รอ Merchant Enrichment พร้อม
- Per-tag threshold tuning — ทำหลังมี distribution จริง
- Incremental refresh (Option B) — ทำเมื่อ data volume ใหญ่ขึ้น
- Tag expiry / decay logic — ทำใน Phase 2

---

*Spec v1.0 — Thena × Tee | 2026-04-15*
*Reviewed by: [ชื่อ engineer] | Approved by: [ชื่อ lead]*
