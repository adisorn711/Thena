# Automation via Existing System — TODO

**สถานะ**: inbox — ยังไม่ได้คุย, เด๋วมาต่อ

---

## โจทย์หลัก

การนำ Customer Tag ไปใช้งานจริงผ่าน existing system ขององค์กร
= สร้างระบบ **automation** เพื่อลดงาน campaign manager

---

## คำถามที่ต้องตอบก่อนออกแบบ

1. **existing system คืออะไร** — campaign tool ที่ใช้คืออะไร? มี CDP หรือ CRM กลางไหม?

2. **bottleneck จริงอยู่ที่ไหน**
   - ตอน query SQL?
   - ตอน approve list?
   - ตอน set up campaign ใน tool?

3. **scope ของ automation — level ไหน**
   - A: tag พร้อม → query ง่ายขึ้น (ลด SQL complexity)
   - B: กำหนด rule → ระบบ trigger campaign เองเมื่อ customer เข้า condition
   - C: A + B + alerting เมื่อ segment เปลี่ยน

---

## Context ที่มีอยู่แล้ว

- Layer 2 ชื่อ "Personalized Trigger" — เป็น layer ที่ตั้งใจจะ address โจทย์นี้
- SQL table `customer_tag_profile` พร้อมใช้: tier, trending, recency_status, spend_intensity
- Pre-built bundle (`customer_segment` table) สำหรับ named segment

---

## สิ่งที่ต้องทำต่อ

- [ ] ตอบ 3 คำถามข้างบน (ทีม/Tee)
- [ ] ออกแบบ workflow automation จาก Tag → Campaign trigger
- [ ] ทำเป็น slides สำหรับ Layer 2 detail (เทียบกับ Layer 1 detail ที่ทำไปแล้ว)
