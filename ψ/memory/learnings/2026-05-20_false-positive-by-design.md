---
name: False Positive — ถามตั้งแต่ design ไม่ใช่ตอน validate
description: ทุก signal ใหม่ต้องถาม "อะไรทำให้ false positive ได้?" ก่อน propose ให้ stakeholder
type: feedback
---

## Rule

เมื่อเสนอ signal ใหม่สำหรับ tag — ถาม "อะไรทำให้ false positive ได้?" ทันทีในขั้น design

ตัวอย่าง: `fuel_declining` ดูเหมือน EV intent signal ที่ดี แต่ confound กับ:
- Grab/ride-share ใช้มากขึ้น
- Work from home
- ย้ายบ้าน
- ลาออกจากงาน

ถ้าไม่กรอง false positive ออก → precision ต่ำมาก → campaign waste

**Why:** Session 2026-05-20 — `fuel_declining` เสนอไปก่อน แล้วต้องกลับมาเพิ่ม exclusion criteria (grab_dependent = FALSE, bts_mrt_user = FALSE) ทีหลัง ถ้าคิดตั้งแต่ต้นจะ present ได้ครบกว่า

**How to apply:**
```
Signal → ถาม: "confounding behaviors ที่ให้ false positive เหมือนกันคืออะไร?"
       → เพิ่ม exclusion ใน definition ทันที
       → ค่อย present
```
