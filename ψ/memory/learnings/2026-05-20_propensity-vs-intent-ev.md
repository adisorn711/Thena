---
name: Propensity vs Intent — EV Detection
description: ความต่างระหว่าง intent detection (ต้องการ direct signal) กับ propensity profiling (ใช้ behavioral proxy) — critical ก่อนออกแบบ tag ใดๆ ที่เป็น "pre-behavior"
type: feedback
---

## Rule

ก่อนออกแบบ "early warning" หรือ "intent" tag ทุกตัว ต้องถามก่อนว่า: **เรามี direct behavioral signal ไหม?**

- ถ้ามี (เช่น showroom visit, search behavior) → Intent Detection ได้จริง
- ถ้าไม่มี → ทำได้แค่ Propensity Profiling เท่านั้น

ต้องแยก 2 อันนี้ให้ชัดกับ stakeholder ก่อนเริ่ม เพราะ use case ต่างกัน:
- Intent → trigger-based, act เร็ว 1-2 เดือนก่อนซื้อ
- Propensity → awareness segment, protect share-of-wallet

**Why:** Session 2026-05-20 — EV intention detection สำหรับ credit card issuer ทำไม่ได้เป็น true intent เพราะ EV dealership ยังไม่รับบัตรเครดิต จึงไม่มี direct signal ต้อง fallback เป็น combo tag (ev_likely_profile) แทน

**How to apply:** ทุกครั้งที่มีคำถาม "จะดัก X intent ยังไง?" ให้ถามก่อนว่า "มี direct txn signal สำหรับ X ไหม?" ถ้าไม่มี → frame ให้ถูกว่าจะทำ propensity ไม่ใช่ intent
