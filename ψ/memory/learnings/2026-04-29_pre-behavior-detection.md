---
name: Pre-behavior detection — leading tags over trend monitoring
description: ดักก่อนซื้อด้วย leading tag + lag corr ดีกว่ารอ trend ขาขึ้น
type: project
---

Trend ขาขึ้นของ tag = ลูกค้าซื้อไปแล้ว → too late to influence

**Why:** Tee ตั้งข้อสังเกตว่า "การรอ trend ขาขึ้นอาจ too late" เพราะ score สะท้อน behavior ที่เกิดขึ้นแล้ว ไม่ใช่ intention

**How to apply:** ใช้ lag correlation ระหว่าง tag pairs เพื่อหา leading tags ที่ขึ้นก่อน 1-3 สัปดาห์ แล้ว trigger campaign ในช่วง lag window นั้น ไม่ใช่หลังจาก target tag ขึ้นแล้ว pattern: corr(tag_A[t-lag], tag_B[t]) สูง → tag_A คือ leading indicator ของ tag_B
