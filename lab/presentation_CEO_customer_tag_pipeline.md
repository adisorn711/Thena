# รู้จักลูกค้าดีขึ้น ด้วย Customer Tagging
**Data Science Team | เมษายน 2025**

---

## ปัญหาที่เรามีอยู่

> **เราแบ่งลูกค้าเป็นกลุ่มใหญ่ๆ แล้วยิง Campaign เดียวกันทั้งกลุ่ม**

ลูกค้าที่ใช้จ่ายเท่ากัน ไม่ได้มีพฤติกรรมเหมือนกัน
Campaign เดียวกันจึงตรงสำหรับบางคน และพลาดสำหรับคนส่วนใหญ่

---

## สิ่งที่เราเสนอ

**เปลี่ยนจาก "ลูกค้าอยู่กลุ่มไหน" → "ลูกค้าเป็นคนแบบไหน"**

แทนที่จะรู้แค่ว่าลูกค้าอยู่ใน Tier A หรือ Tier B
เราจะรู้ว่าลูกค้าแต่ละคนมีพฤติกรรมอะไรบ้าง

```
ลูกค้า A  →  ชอบกินข้าวนอกบ้าน  |  ใช้ Grab บ่อย  |  ช้อปออนไลน์  |  มีรถ
ลูกค้า B  →  นักเดินทาง  |  ใช้จ่ายสูง  |  ซื้อของ Luxury  |  สมาชิกฟิตเนส
```

**เราเรียกสิ่งนี้ว่า Customer Tags**

---

## ทำได้จากข้อมูลที่มีอยู่แล้ว

**ไม่ต้องลงทุนซื้อข้อมูลใหม่** — ใช้ Transaction ที่มีอยู่ทั้งหมด

ลูกค้าทุกครั้งที่รูดบัตร บอกเราถึงตัวเองโดยไม่รู้ตัว
เราแค่เรียนรู้ที่จะอ่านสิ่งที่เขาบอก

---

## ขนาดของโอกาส

| | |
|--|--|
| **Tags ทั้งหมด** | 151 Tags ครอบคลุมทุกมิติพฤติกรรม |
| **ทำได้ทันที** | 117 Tags โดยไม่รอข้อมูลเพิ่ม |
| **Refresh** | ทุกวัน — ตามพฤติกรรมจริง ไม่ใช่ข้อมูลเก่า |
| **ความแม่นยำ** | ทุก Tag มี Score บอกความมั่นใจ ไม่ใช่แค่ใช่/ไม่ใช่ |

---

## 10 มิติที่เราจะรู้จักลูกค้า

| มิติ | ตัวอย่าง Tags |
|------|-------------|
| 🍽️ การกิน | ชอบร้านดัง / สั่ง Delivery / กินดึก |
| ✈️ การเดินทาง | นักเดินทางบ่อย / เที่ยว Luxury / นักธุรกิจ |
| 🛍️ การช้อป | ช้อปออนไลน์ / แบรนด์หรู / ลูกค้า Shopee |
| 🎭 ไลฟ์สไตล์ | คนดูหนัง / สมาชิกฟิตเนส / คนฟัง Streaming |
| 🚗 การเดินทาง | มีรถ / ใช้ Grab / ขับ EV |
| 💊 สุขภาพ | ใส่ใจสุขภาพ / ไปโรงพยาบาลบ่อย |
| 💳 การเงิน | ใช้จ่ายสูง / ชำระเต็ม / ใช้ผ่อน |
| 👨‍👩‍👧 ช่วงชีวิต | มีบุตร / เลี้ยงสัตว์ / เจ้าของบ้าน |
| ⏰ เวลา | คนตื่นเช้า / มนุษย์กลางคืน / ช้อปวันหยุด |
| 📱 Digital | ใช้ออนไลน์เป็นหลัก / ลูกค้า Fintech |

---

## วิธีที่ระบบทำงาน — ภาพรวม

```
ลูกค้ารูดบัตร
      │
      ▼
┌─────────────────────┐
│   Transaction Data  │  ← 12 เดือนย้อนหลัง
│  ร้านไหน / เท่าไหร่ │
│  เมื่อไหร่ / ช่องไหน │
└─────────────────────┘
      │
      ▼
┌─────────────────────┐
│    Tag Engine       │  ← Refresh ทุกวัน 01:00
│  คำนวณ Score/Tag    │
└─────────────────────┘
      │
      ▼
┌──────────────────────────────────────────┐
│           Customer Tag Profile           │
│  ลูกค้า A:  frequent_diner  ▓▓▓▓▓ 0.82  │
│             high_spender   ▓▓▓▓▓ 0.90  │
│             car_owner      ▓▓▓░░ 0.71  │
└──────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────────────────┐
│            Personalized Trigger Rules               │
│  IF  frequent_diner ≥ 0.7  AND  high_spender ≥ 0.7 │
│  →   เสนอ "Dining Cashback Offer"                   │
│                                                     │
│  IF  car_owner = 1  AND  Tag เพิ่งเกิดใหม่          │
│  →   เสนอ "EV Privilege Welcome"                    │
│                                                     │
│  IF  frequent_diner score ลดลง > 30% ใน 30 วัน     │
│  →   เสนอ "Retention Offer"                         │
└─────────────────────────────────────────────────────┘
      │
      ▼
┌──────────────────────────────────────────┐
│   Delivery Channel                       │
│  Email / SMS / Push / Manual Outbound    │
│  ส่งตรงคน ในเวลาที่เหมาะ                 │
└──────────────────────────────────────────┘
      │
      ▼
   วัดผล → ปรับ Rule
```

> **ไม่ว่าจะ automate หรือ manual** — ทุก offer มาจาก Tag ของลูกค้า ไม่ใช่การเดา

---

## นำไปใช้ได้ทันทีกับอะไร

### Targeted Campaign
```
แทนที่จะส่ง Dining Cashback ให้ทุกคน
→ ส่งเฉพาะคนที่มี Tag "frequent_diner" + "high_spender"
→ Conversion สูงขึ้น, Cost ต่ำลง
```

### Product Offer Matching
```
ลูกค้ามี Tag "ev_driver" + "high_spender"
→ นำเสนอ EV Charging Privilege ก่อนใคร
```

### Risk & Retention
```
ลูกค้า Tag เปลี่ยน — "frequent_diner" หายไป
→ สัญญาณ Churn ก่อนที่จะเลิกใช้บัตร
```

---

## End Game — เราจะไปถึงไหน

> Customer Tagging ไม่ใช่แค่เครื่องมือ Campaign
> มันคือ foundation ของการเปลี่ยน business model

Hyundai Card ใช้ระบบนี้สร้าง **5 Layers of Intelligence** — เราเดินบนเส้นทางเดียวกัน

| Layer | เป้าหมาย | ผลลัพธ์ทางธุรกิจ |
|-------|---------|----------------|
| **1. Tags** | รู้ว่าลูกค้าเป็นใคร | Foundation ทั้งหมด |
| **2. Personalized Trigger** | เสนอ offer ที่ใช่ ให้คนที่ใช่ ในเวลาที่เหมาะ | ลด CAC, เพิ่ม Conversion |
| **3. Personalized Products** | Card ที่ benefit ตรงกับแต่ละคน | ลด Churn, เพิ่ม Spend per Card |
| **4. Merchant Intelligence** | ขายความแม่นยำให้ Merchant | Revenue Stream ใหม่จาก Data |
| **5. Lifestyle Platform** | ส่วนหนึ่งของชีวิตลูกค้า | Brand Moat ที่คู่แข่ง copy ไม่ได้ |

### ตัวอย่าง Personalized Trigger (Layer 2)

| สิ่งที่เกิดขึ้น | สิ่งที่เราทำได้ |
|----------------|----------------|
| รูดปั๊มน้ำมันครั้งแรกในเมืองใหม่ | เสนอ Travel Insurance ทันที |
| `frequent_diner` score ลดฮวบ | แจ้งเตือน Churn → ส่ง Retention Offer |
| Tag `new_parent` เพิ่งเกิดขึ้น | เสนอ Family Protection Product |

### ทำไมนี่คือ Competitive Moat

> Credit Card ไม่ได้แข่งกันที่ Interest Rate หรือ Cashback %
> แต่แข่งกันที่ **"ใครรู้จักลูกค้าดีกว่า"**
>
> Hyundai Card สร้าง Music Library, Travel Library, Cooking Library
> ไม่ใช่เพราะ CSR — แต่เพราะ Tag data บอกว่าลูกค้าต้องการ experience นั้น
> ผลคือลูกค้าไม่ได้แค่ "ใช้บัตร" แต่ **"ใช้ชีวิตกับบัตร"**

---

## แผนการทำงาน

### Phase 1 — Prove Value (ทันที)
> เริ่มจาก 10 Tags ที่ชัดเจนและวัดผลได้
- `frequent_diner`, `high_spender`, `car_owner`, `grab_dependent` และอื่นๆ
- วัดผลผ่าน Campaign A/B Test เทียบกับ approach เดิม

### Phase 2 — Scale Up
> ขยายเป็น 117 Tags ครบทุกมิติ + เปิด Real-time Triggers
- Calibrate ความแม่นยำจาก Phase 1
- ใช้ Tags เป็น Feature ใน ML Models
- เริ่ม trigger-based campaign แทน calendar-based

### Phase 3 — Full Intelligence
> เพิ่มอีก 34 Tags ด้วยข้อมูล Enrichment + Merchant Intelligence
- เข้าใจลูกค้าในระดับ Cuisine Preference, Travel Destination
- เปิด Revenue Stream จาก Merchant Partnership Targeting

### Phase 4 — Platform (Long-term)
> จาก Financial Company → Lifestyle Intelligence Platform
- Personalized product benefits ระดับ individual
- Lifestyle experiences ที่ driven จาก Tag data

---

## สิ่งที่ต้องการจากการตัดสินใจวันนี้

| ต้องการ | เพื่ออะไร |
|--------|----------|
| Approve Phase 1 | เริ่ม implement 10 Tags แรก |
| กำหนด KPI ร่วมกัน | วัดความสำเร็จก่อน scale |
| ระบุ Campaign ที่จะ test | ให้มีผล Business ที่จับต้องได้ |

---

## Bottom Line

> เรามีข้อมูลลูกค้าอยู่แล้ว
> คำถามคือเราอ่านมันได้ดีแค่ไหน
>
> Customer Tagging คือการเปลี่ยนจาก
> **"รู้ว่าลูกค้าใช้จ่ายเท่าไหร่"**
> เป็น
> **"รู้ว่าลูกค้าเป็นใคร"**

---

*Data Science Team | เมษายน 2025*
