---
name: Double-Tagged Systems Enable Clean Automation
description: เมื่อ customer และ offer ใช้ tag taxonomy เดียวกัน matching logic เรียบง่าย และ automation ออกแบบได้ตรงไปตรงมา
type: project
---

เมื่อ entity ทั้งสองฝั่ง (customer + offer) ใช้ taxonomy เดียวกัน:

```sql
customer_tag_profile.tag  =  offer_tag_profile.tag
→ eligible list by JOIN alone
```

**Why:** Tee confirm ว่า existing system ออกแบบให้ offer ติด tag แบบเดียวกับ customer (Taxonomy A) ทำให้ไม่ต้องมี mapping layer กลาง — ลด complexity ของ matching engine ลงมาก

**How to apply:** เวลาออกแบบ automation pipeline สำหรับ recommendation/matching ให้ถามก่อนว่า "entity ทั้งสองฝั่งใช้ vocabulary เดียวกันไหม?" ถ้าใช่ → JOIN on shared key คือ solution เพียงพอ ไม่ต้องสร้าง intermediate translation layer
