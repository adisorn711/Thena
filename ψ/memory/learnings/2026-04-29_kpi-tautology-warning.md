---
name: KPI tautology — downstream vs independent KPIs
description: แยก KPI ที่ trivially corr กับ tag ออกจาก KPI ที่ meaningful ก่อนทำ analysis
type: feedback
---

ก่อนทำ tag × KPI correlation ต้องแยก KPI สองกลุ่มก่อนเสมอ

**Why:** Tag คำนวณจาก txn data → corr กับ Active Rate หรือ Spend per Card จะสูงเสมอเพราะมาจากแหล่งเดียวกัน ไม่ใช่ insight แต่เป็น circular logic

**How to apply:**
- Downstream KPIs (ตัด): Active Rate, Spend per Card, Transaction Count, Avg Ticket Size
- Independent KPIs (ใช้): Revolving Rate, Attrition, Delinquency, Credit Utilization, Revenue per Card
- corr กับ independent KPIs เท่านั้นที่ meaningful
