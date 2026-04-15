# Aggregation Pipeline Design Patterns

**Date**: 2026-04-15
**Source**: Session กับ Tee — Customer Tag Aggregation Logic

## Lesson

การออกแบบ tag aggregation pipeline ที่ดีต้องแยก signal type ออกก่อน ไม่ใช่ apply formula เดียวทุก tag

## Pattern: Tag Signal Sub-types (A1–A7)

| Sub-type | Signal | Implementation |
|----------|--------|---------------|
| A1 | MCC prefix เท่านั้น | GROUP BY mcc_prefix |
| A2 | MCC + merchant keyword | LIKE match on merchant_name_part |
| A3 | MCC + amount | WHERE amount > percentile |
| A4 | MCC + timestamp | WHERE txn_hour / day_of_week |
| A5 | MCC combination | JOIN หลาย prefix, check co-occurrence |
| A6 | Pure behavioral | Aggregate stats, no MCC filter |
| A7 | Recurring pattern | Window function / subscription detection |

## Binary vs Scored Tags

- **Binary tag** = categorical feature (presence/absence) → score 0 or 1
- **Scored tag** = continuous feature → freq + recency + breadth formula

```
final_score = 0.4 × freq + 0.4 × recency + 0.2 × breadth
```

ทั้งสองใช้ร่วมกันใน ML feature set และ rule engine ได้โดยตรง ไม่ต้อง transform เพิ่ม

## Key Warning

Merchant keyword lists ต้อง validate กับ actual `merchant_name` ใน database ก่อน production
keyword assumption จากความรู้ทั่วไปอาจ mismatch กับ naming convention จริงของข้อมูล

## How to Apply

เมื่อออกแบบ tag aggregation pipeline:
1. Classify tags เป็น sub-type ก่อน
2. แยก binary vs scored
3. Validate merchant keywords กับ data จริง
4. ตั้ง global threshold แล้ว calibrate หลัง pilot run
