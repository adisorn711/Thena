# Customer Tagging Pipeline
### แผนงานออกแบบระบบ Customer Tags
**วันที่**: 15 เมษายน 2025 | **สถานะ**: พร้อม Implement

---

## 1. เราทำอะไร?

เปลี่ยนข้อมูล Transaction ที่มีอยู่แล้ว → **Tags ประจำตัวลูกค้า** ที่ใช้งานได้จริง

```
ลูกค้า 1 คน  →  หลาย Tags พร้อมกัน
                 frequent_diner   (score 0.82)
                 car_owner        (score 0.71)
                 high_spender     (score 0.90)
                 ev_driver        ✓
```

---

## 2. ทำไมต้อง Tags? (ไม่ใช่ Segment)

| Segmentation แบบเดิม | Customer Tags |
|----------------------|--------------|
| ลูกค้า 1 คน อยู่ **1 กลุ่มเท่านั้น** | ลูกค้า 1 คน มีได้ **หลาย Tags** |
| Static — แบ่งแล้วค้างไว้ | Dynamic — Refresh **ทุกวัน** |
| ไม่มี confidence | ทุก Tag มี **Score 0–1** |
| Campaign ตรงกลุ่มใหญ่ | Campaign ตรงพฤติกรรมจริง |

---

## 3. ข้อมูลที่ใช้

**ไม่ต้องหาข้อมูลใหม่** — ใช้จากที่มีอยู่แล้วทั้งหมด

| ข้อมูล | ใช้ทำอะไร |
|--------|----------|
| Merchant Tag (`Dining_Fuji`) | รู้ว่าลูกค้าใช้จ่ายที่ไหน ประเภทอะไร |
| Amount | วิเคราะห์พฤติกรรมการใช้จ่าย |
| Transaction Date/Time | รู้ pattern เวลา (กลางคืน / เช้า / วันหยุด) |
| Channel (Online/In-store) | รู้ความชอบช่องทาง |
| Currency | รู้การใช้จ่ายต่างประเทศ |

**Lookback**: 12 เดือนย้อนหลัง | **Refresh**: ทุกวัน

---

## 4. Pipeline Architecture

```
Transaction Data (12 เดือน)
         │
         ▼
  แยก MCC Prefix
  จาก Merchant Tag
  "Dining_Fuji" → "Dining"
         │
    ┌────┴────┐
    │         │
  Path A    Path B
 117 Tags   34 Tags
 ทำได้เลย  รอ Enrichment
    │         │
    └────┬────┘
         ▼
  คำนวณ Score ต่อ Tag
         ▼
  กรอง Score ≥ 0.3
         ▼
  Customer Tag Table
  (Refresh ทุกวัน 01:00)
```

---

## 5. Tags ทั้งหมด — 151 Tags

### แบ่งตามความพร้อม

| กลุ่ม | จำนวน | สถานะ |
|-------|-------|-------|
| **Path A** — ไม่รอ Enrichment | **117 tags** | ✅ ทำได้เลย |
| **Path B** — รอ Enrichment | **34 tags** | ⏳ รอ Phase ถัดไป |

### Path A — แบ่งตามประเภท Signal

| หมวด | Tags | ตัวอย่าง |
|------|------|---------|
| 🍽️ Food & Dining | 13 | `frequent_diner`, `cafe_hopper`, `delivery_dependent` |
| ✈️ Travel | 13 | `frequent_traveler`, `luxury_traveler`, `business_traveler` |
| 🛍️ Shopping | 19 | `marketplace_shopper`, `luxury_shopper`, `convenience_store_addict` |
| 🎭 Entertainment | 11 | `movie_lover`, `gym_member`, `streaming_subscriber` |
| 🚗 Transport | 10 | `car_owner`, `grab_dependent`, `ev_driver` |
| 💊 Health | 9 | `health_conscious`, `pharmacy_regular`, `gym_member` |
| 💳 Financial | 14 | `high_spender`, `installment_user`, `reward_maximizer` |
| 👨‍👩‍👧 Life Stage | 10 | `parent`, `pet_owner`, `homeowner` |
| ⏰ Time Pattern | 10 | `night_owl_spender`, `weekend_warrior`, `morning_person` |
| 📱 Digital | 8 | `online_native`, `crypto_curious`, `fintech_user` |

---

## 6. วิธีคำนวณ Score

### Scored Tags (ส่วนใหญ่)
> วัดจาก 3 มิติ

```
Score = 40% × ความถี่ (Frequency)
      + 40% × ความใหม่ (Recency)
      + 20% × ความหลากหลาย (Breadth)
```

- **Frequency**: ใช้บ่อยแค่ไหน (normalize ด้วย log scale)
- **Recency**: ล่าสุดนานแค่ไหน (decay ทุก 90 วัน)
- **Breadth**: กี่ร้านที่ใช้ (วัด genuine interest ไม่ใช่ loyal 1 ร้าน)

### Binary Tags (บาง Tag)
> เปรียบได้กับ Categorical Feature

```
มี Transaction ตามเงื่อนไข = 1
ไม่มี = 0
```

ตัวอย่าง: `ev_driver`, `crypto_curious`, `airbnb_user`

**Threshold**: Score ≥ 0.3 → ได้รับ Tag (ปรับได้หลัง Pilot)

---

## 7. Quick Win — Phase 1

**เริ่ม 10 Tags ง่ายที่สุดก่อน** เพื่อ prove value เร็ว

| # | Tag | Signal หลัก |
|---|-----|------------|
| 1 | `frequent_diner` | Dining MCC, txn ≥ 120/ปี |
| 2 | `convenience_store_addict` | 7-Eleven/FamilyMart ≥ 180/ปี |
| 3 | `grocery_regular` | Tops/BigC/Lotus ≥ 36/ปี |
| 4 | `grab_dependent` | Grab ≥ 180/ปี |
| 5 | `high_spender` | Total spend > P75 |
| 6 | `mid_spender` | Total spend P25–P75 |
| 7 | `low_spender` | Total spend < P25 |
| 8 | `marketplace_shopper` | Shopee/Lazada ≥ 48/ปี |
| 9 | `streaming_subscriber` | Netflix/Disney+ recurring |
| 10 | `car_owner` | Fuel + Parking + Auto service ครบ |

---

## 8. Roadmap

```
Phase 1 (Now)
├── Implement Quick Win 10 Tags
├── Validate merchant keywords กับ data จริง
├── Pilot run → ดู Score Distribution
└── Calibrate threshold

Phase 2 (After Pilot)
├── ขยาย Path A ครบ 117 Tags
├── Per-tag threshold tuning
├── Complex tags (last_minute_booker, empty_nester)
└── Incremental refresh (ถ้า data ใหญ่ขึ้น)

Phase 3 (After Enrichment)
└── Path B — 34 Enrichment Tags
```

---

## 9. Output ที่ใช้งานได้

### Campaign Targeting
```
ev_driver = 1
AND high_spender_score ≥ 0.7
→ Target EV promotion สำหรับ high-value segment
```

### ML Feature Engineering
```
ใส่ทั้ง scored tags และ binary tags เป็น features ได้เลย
ไม่ต้อง transform เพิ่ม
```

### Personalization
```
frequent_diner + cafe_hopper
→ push dining cashback offer
```

---

## 10. ไฟล์อ้างอิง

| ไฟล์ | เนื้อหา |
|------|--------|
| `lab/path_a_rule_table.md` | Rule table ครบ 117 tags พร้อม threshold |
| `lab/customer_tag_pipeline_spec.md` | Full spec สำหรับ Engineer |
| `lab/customer_tag_library.md` | Tag definitions ครบ 151 tags |
| `lab/customer_tag_library_by_enrichment.md` | แยก Path A vs Path B |

---

*Customer Tagging Pipeline v1.0 | Data Science Team | 2026-04-15*
