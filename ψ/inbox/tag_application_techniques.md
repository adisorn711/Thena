# Tag Application Techniques — เตรียมทำ pptx

**สถานะ**: จด inbox ไว้ก่อน → เตรียม draft เป็น slide

---

## Context

Campaign manager ทำงานผ่าน SQL table อยู่แล้ว
โจทย์หลัก: ลด friction — ไม่ต้องมานั่งคิด threshold เอง

---

## เทคนิคที่จะนำเสนอ

### 1. Threshold-based Label ("Lover")
```
score ≥ threshold  →  frequent_diner = "lover"
```
- ทีมทำอยู่แล้ว — เป็น baseline

### 2. Tier Label
```
score ≥ 0.7  →  heavy
score ≥ 0.4  →  casual
score < 0.4  →  (ไม่ติด tag)
```
- campaign manager เลือก heavy vs casual ได้เลย

### 3. Trending Flag
```
score เดือนนี้ vs เดือนที่แล้ว
+20%  →  rising   ← กำลัง active มากขึ้น
-20%  →  fading   ← สัญญาณ churn / retention signal
```

### 4. Recency Flag
```
active  =  tag ติด + last txn ≤ 30 วัน
lapsed  =  tag ติด + last txn 31–90 วัน
```

### 5. Pre-built Bundle (Named Segment)
```
"premium_foodie"   =  frequent_diner(heavy) + high_spender
"young_urbanite"   =  grab_dependent + streaming_subscriber + online_native
"family_spender"   =  parent + grocery_regular + homeowner
```
- campaign manager เรียกชื่อ segment ได้เลย ไม่ต้องรู้ logic ข้างใน

---

## SQL Table Design (output ที่ campaign manager ใช้จริง)

### customer_tag_profile
```sql
customer_id     VARCHAR
tag             VARCHAR   -- 'frequent_diner'
score           FLOAT     -- 0.0–1.0
tier            VARCHAR   -- 'heavy' | 'casual' | NULL
trending        VARCHAR   -- 'rising' | 'stable' | 'fading'
recency_status  VARCHAR   -- 'active' | 'lapsed'
as_of_date      DATE
```

### customer_segment
```sql
customer_id     VARCHAR
segment_name    VARCHAR   -- 'premium_foodie', 'young_urbanite'
as_of_date      DATE
```

### ตัวอย่าง query ที่ campaign manager ใช้จริง
```sql
-- Heavy diner ที่ยัง active
SELECT customer_id FROM customer_tag_profile
WHERE tag = 'frequent_diner' AND tier = 'heavy' AND recency_status = 'active';

-- Win-back — เคยกินบ่อยแต่หายไป
SELECT customer_id FROM customer_tag_profile
WHERE tag = 'frequent_diner' AND trending = 'fading' AND recency_status = 'lapsed';

-- Bundle สำเร็จรูป
SELECT customer_id FROM customer_segment WHERE segment_name = 'premium_foodie';
```

---

## สิ่งที่ต้องทำต่อ
- [ ] Draft เป็น slide สำหรับ pptx
- [ ] เพิ่ม CREATE TABLE statement + pipeline script (draft แล้วถ้า Tee ต้องการ)
