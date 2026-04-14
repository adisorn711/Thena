# Merchant Tags vs Customer Tags — คนละ Layer

**Date**: 2026-04-15
**Source**: Session D-Tag Deep Dive — Thena × Tee

## Lesson

Merchant Tagging (one merchant → many attributes) และ Customer Tagging (one customer → many behavioral tags) คือคนละ layer ที่มักถูก confuse กัน

```
Merchant Tags  = อธิบายว่า "ร้านนี้คืออะไร"
Customer Tags  = อธิบายว่า "คนนี้ชอบอะไร / ทำอะไร"
```

Merchant Tags เป็น prerequisite สำหรับ Customer Tags บางตัว (เช่น cuisine-based) แต่ไม่ใช่ทั้งหมด — **78% ของ Customer Tags ทำได้จาก MCC + Merchant Name + Timestamp + Amount โดยไม่รอ Merchant Enrichment**

## Why It Matters

ทีมที่ทำ Merchant Enrichment มักคิดว่าตัวเองกำลังทำ Customer Tagging แล้ว ทำให้ไม่เริ่ม Customer Tagging จริงๆ ซึ่งเป็น delay ที่ไม่จำเป็น

## How to Apply

- Classify tags ตาม data dependency ก่อนเสมอ
- เริ่ม implement Customer Tags จาก signal ที่มีอยู่แล้ว ไม่รอ Enrichment พร้อม 100%
- สื่อสาร 3-layer architecture ให้ทีมเห็นภาพก่อน: MCC → Merchant Name → Enrichment → Customer Tags
