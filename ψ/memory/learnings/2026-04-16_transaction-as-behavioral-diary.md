# Transaction เป็น Behavioral Diary

**Date**: 2026-04-16
**Source**: Session กับ Tee — Tag Library v2 Expansion 303 tags

## Lesson

ทุก tag ที่ดีเกิดจากการตั้งคำถามว่า "behavior นี้จะทิ้ง transaction fingerprint อะไรไว้" ไม่ใช่ "น่าจะมี tag อะไร interesting"

## Pattern: Behavioral Signature Design

```
❌ Label-first thinking
"น่าจะมี tag ว่า adventurous" → แล้วค่อยหา signal

✅ Signal-first thinking  
"ลูกค้าที่ outdoor gear + travel + sport txn combo" → tag = outdoor_adventurer
```

## 3 Dimensions ที่มักถูกมองข้าม

Credit card tagging มักโฟกัส spending ปัจจุบัน แต่ transaction บอก "investment dimensions" ด้วย:

| Dimension | MCC signals | ความหมาย |
|-----------|-------------|---------|
| **Education** | tuition + course + stationery | ลงทุนในตัวเอง |
| **Real Estate** | utility + HomePro + property | ลงทุนในทรัพย์สิน |
| **Investment** | brokerage + fund + gold | ลงทุนในอนาคตทางการเงิน |

ลูกค้าที่มี investment dimensions สูงมักเป็น high-value long-term customer

## Pattern: Behavioral Combo = Life Event

บาง life event ไม่มี explicit signal แต่ทิ้ง transaction combo ที่ unique:

```
newly_married = jewelry + wedding_vendor + honeymoon_travel ใน timeline เดียวกัน
new_parent    = baby_products spike + pharmacy + hospital combo
home_renovator = HomePro + contractor + high_spend ≥ 3 ครั้ง/ปี
```

## How to Apply

เวลาออกแบบ tag ใหม่:
1. ถามก่อนว่า "ถ้าคนมี behavior นี้จริง เขาจะรูดบัตรที่ไหน กี่ครั้ง เท่าไหร่"
2. ถ้าตอบไม่ได้ชัด → tag นั้นยังไม่ ready
3. Tag ที่ดีต้องมี threshold ที่ specific ไม่ใช่แค่ "บ่อย"
