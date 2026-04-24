# Parked Topics — Customer Tagging

บันทึก: 2026-04-16 | ฝากโดย Tee

---

## Topic 1: วิธีหา Customer Tags เพิ่ม

**คำถาม**: Customer Tags มีวิธีการหาเพิ่มได้อย่างไรบ้าง?
Hyundai Card สร้าง Tags ไปทั้งหมดกี่อัน?

**ทิศทางที่น่าคุย**:
- Hyundai UNIVERSE D-Tag — จำนวน tags และ methodology
- วิธี expand tags จาก 151 → มากขึ้น: survey data, external data, behavioral signals ใหม่
- Tag discovery pipeline: ควรมีกระบวนการอะไรในการ propose tags ใหม่อย่างเป็นระบบ

---

## Topic 2: Customer Tags × AI/ML

**คำถาม**: Tags ไปต่อยอดใน AI/ML ได้มุมไหนบ้าง?
มีวิธีคิด Tags ใหม่แบบ Unsupervised ได้ไหม?

**ทิศทางที่น่าคุย**:
- Tags เป็น feature สำหรับ churn prediction, LTV model, product recommendation
- Unsupervised tag discovery: clustering (k-means, DBSCAN), behavioral embeddings
- Tag co-occurrence mining: tags ไหนมักเกิดพร้อมกัน → อาจบอก segment ที่ยังไม่รู้จัก
- Sequence modeling: ลำดับ tag ที่เปลี่ยนไปบอกอะไร (lifecycle patterns)
- Anomaly detection: ลูกค้าที่ tag เปลี่ยนผิดปกติ → early signal

---

---

## Topic 3: Persona Layer — Clustering on 303 Tag Scores

**คำถาม**: ออกแบบ Persona Layer บน 303 tag scores ได้อย่างไร?

**Context**: Customer tags ที่ derive มาจาก merchant context จะมี high correlation กันอย่างหลีกเลี่ยงไม่ได้ (Hierarchical, Lifestyle Bundle, Instrument Correlation) → Persona Layer คือ solution ที่จัดการ correlation นี้โดยตรง

**ทิศทางที่น่าคุย**:
- Feature vector: customer × 303 tag scores (0.0–1.0 สำหรับ scored tags, 0/1 สำหรับ binary tags)
- Dimensionality reduction: PCA หรือ UMAP ก่อน cluster เพื่อจัดการ correlated dimensions
- Clustering: k-means หรือ DBSCAN → target 10–20 personas
- Interpretation: ดู dominant tags ของแต่ละ cluster บน original feature space
- Output: `persona_id` + `persona_name` (เช่น "Urban Foodie", "Family Builder") per customer
- Refresh schedule: รัน re-cluster ราย quarter หรือ trigger-based

---

---

## Topic 4: End-to-End Big Picture — Stakeholder Presentation

**คำถาม**: เรียบเรียงเนื้อหา end-to-end ของโปรเจค Customer Tagging ให้อยู่ใน format ที่ present stakeholder ได้ แบบ high level

**Context**: Big picture ที่กำลังร่างมี 5 layers:
- Layer 1: Data Foundation ✅ draft แล้ว
- Layer 2: Tag Engine ✅ draft แล้ว (Signal Extractor A1–A7, Score Calculator, Profile Builder)
- Layer 3: Customer Tag Profiles — ยังไม่ได้ draft
- Layer 4: Persona Layer — ยังไม่ได้ draft
- Layer 5: Applications — ยังไม่ได้ draft

**สิ่งที่ต้องทำ**:
1. Draft Layer 3–5 ให้ครบ
2. เรียบเรียงทั้ง 5 layers เป็น high-level stakeholder presentation
3. Format: เริ่ม markdown ก่อน → ทำ PowerPoint ทีหลัง (Format C)

---

*Parked — จะคุยใน session ถัดไปที่มีเวลา*
