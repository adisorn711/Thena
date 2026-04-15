# Path A — MCC Rule Table (No Enrichment)
**Version**: 1.0 Draft | Tags: 117 | Lookback: 12 months | Threshold: score ≥ 0.3

---

## โครงสร้าง Rule Table

merchant_tag format: `<mcc_prefix>_<merchant_name>` เช่น `dining_fuji`

### Signal Sub-types ใน Path A

| Sub-type | ใช้ signal อะไร | ตัวอย่าง tag |
|----------|----------------|-------------|
| **A1** | MCC prefix เท่านั้น | `frequent_diner` |
| **A2** | MCC prefix + Merchant keyword | `fast_food_regular`, `cafe_hopper` |
| **A3** | MCC prefix + Amount threshold | `fine_dining_enthusiast`, `budget_eater` |
| **A4** | MCC prefix + Timestamp | `brunch_person`, `late_night_diner` |
| **A5** | MCC combination (หลาย prefix) | `car_owner`, `health_conscious` |
| **A6** | Pure behavioral (ไม่ขึ้น MCC) | `high_spender`, `consistent_spender` |
| **A7** | Recurring pattern | `subscription_stacker`, `gym_member` |

---

## 🍽️ Food & Dining (13 tags)

| rule_id | customer_tag | sub_type | mcc_prefix | merchant_keywords | condition | threshold_12m |
|---------|-------------|----------|-----------|-------------------|-----------|--------------|
| D01 | `frequent_diner` | A1 | `dining` | — | txn_count ≥ 120 (avg 10/เดือน) | min 8 active_months |
| D02 | `fast_food_regular` | A2 | `dining`, `fastfood` | mcdonald, kfc, burger_king, subway | txn_count ≥ 48 (avg 4/เดือน) | min 6 active_months |
| D03 | `fine_dining_enthusiast` | A3 | `dining` | — | avg_amount > P75 ของ portfolio dining spend | min 4 txn |
| D04 | `cafe_hopper` | A2 | `cafe`, `coffee` | — | txn_count ≥ 72 AND distinct_merchant ≥ 3 | min 8 active_months |
| D05 | `bubble_tea_addict` | A2 | `dining`, `beverage` | chatramu, gong_cha, koi, tiger_sugar, machi | txn_count ≥ 96 (avg 8/เดือน) | min 8 active_months |
| D06 | `delivery_dependent` | A2 | `delivery`, `dining` | grabfood, lineman, foodpanda, robinhood | delivery_txn / total_dining_txn ≥ 0.5 | min 12 delivery txn |
| D07 | `brunch_person` | A4 | `dining` | — | txn_hour ∈ [09:00–13:00] AND day_of_week ∈ [Sat, Sun] ≥ 24 ครั้ง | min 8 qualifying_months |
| D08 | `late_night_diner` | A4 | `dining` | — | txn_hour ≥ 22:00, txn_count ≥ 48 | min 6 active_months |
| D09 | `bakery_lover` | A2 | `dining`, `bakery` | yamazaki, breadtalk, paris_baguette, red_ribbon | txn_count ≥ 12 (avg 1/เดือน) | min 6 active_months |
| D10 | `budget_eater` | A3 | `dining` | — | avg_amount < P25 ของ portfolio dining spend | min 24 txn |
| D11 | `solo_diner` | A3 | `dining` | — | avg_amount < 200 AND merchant_concentration < 0.3 | min 24 txn |
| D12 | `street_food_lover` | A3 | `dining`, `streetfood` | — | avg_amount < 150 per txn | min 36 txn |
| D13 | `dessert_lover` | A2 | `dining`, `dessert` | after_you, swensens, dairy_queen, baskin, haagen | txn_count ≥ 72 (avg 6/เดือน) | min 8 active_months |

---

## ✈️ Travel (13 tags)

| rule_id | customer_tag | sub_type | mcc_prefix | merchant_keywords | condition | threshold_12m |
|---------|-------------|----------|-----------|-------------------|-----------|--------------|
| T01 | `frequent_traveler` | A5 | `airline`, `hotel` | — | (airline_txn + hotel_txn) ≥ 4 | ครอบ ≥ 2 trip patterns |
| T02 | `international_traveler` | A6 | — | — | currency ≠ THB, txn ≥ 2 | min 1 foreign_merchant |
| T03 | `domestic_traveler` | A5 | `airline`, `hotel` | — | airline/hotel txn ≥ 2 AND currency = THB ทั้งหมด | min 2 txn |
| T04 | `budget_traveler` | A2 | `airline` | airasia, nokair, lion_air | avg hotel_amount < P50 OR airline = LCC | min 2 trips |
| T05 | `luxury_traveler` | A3 | `airline`, `hotel` | thai_airways, singapore_air, emirates | avg_amount > P75 ในทั้ง airline + hotel | min 2 trips |
| T06 | `business_traveler` | A4 | `airline`, `hotel` | — | airline_txn day_of_week ∈ [Mon–Fri] ≥ 60% AND hotel_txn weekday ≥ 60% | min 4 txn |
| T07 | `leisure_traveler` | A4 | `airline`, `hotel` | — | airline/hotel txn ∈ [Sat–Sun หรือ public holiday] ≥ 60% | min 2 trips |
| T08 | `hotel_loyalist` | A1 | `hotel` | — | merchant_concentration ≥ 0.7 (70% txn ที่ chain เดียว) | min 3 hotel_txn |
| T09 | `airbnb_user` | A2 | `hotel`, `accommodation` | airbnb | txn_count ≥ 1 | — |
| T10 | `frequent_flyer` | A1 | `airline` | — | txn_count ≥ 6 | min 6 active_months spread |
| T11 | `backpacker_style` | A3 | `airline`, `hotel`, `travel` | — | txn_count ≥ 4 AND avg_amount < P25 ของ travel spend | — |
| T12 | `last_minute_booker` | A4 | `airline`, `hotel` | — | days_between_booking_and_travel < 7 ใน ≥ 60% of trips | min 2 detectable trips |
| T13 | `early_planner` | A4 | `airline`, `hotel` | — | days_between_booking_and_travel > 30 ใน ≥ 60% of trips | min 2 detectable trips |

> **Note**: T12/T13 ต้องการ booking timestamp vs travel timestamp — อาจ approximate จาก txn_date

---

## 🛍️ Shopping (19 tags)

| rule_id | customer_tag | sub_type | mcc_prefix | merchant_keywords | condition | threshold_12m |
|---------|-------------|----------|-----------|-------------------|-----------|--------------|
| S01 | `online_first_shopper` | A6 | — | — | online_txn / total_txn ≥ 0.5 | min 12 txn |
| S02 | `luxury_shopper` | A3 | `retail`, `fashion` | — | avg_amount > P90 OR merchant ∈ luxury_list | min 2 txn |
| S03 | `fashion_lover` | A1 | `apparel`, `fashion` | — | txn_count ≥ 48 (avg 4/เดือน) | min 6 active_months |
| S04 | `sneaker_enthusiast` | A2 | `apparel`, `sport` | nike, adidas, new_balance, vans, converse | txn_count ≥ 4 | min 3 active_months |
| S05 | `beauty_conscious` | A2 | `beauty`, `cosmetics` | — | txn_count ≥ 36 (avg 3/เดือน) | min 6 active_months |
| S06 | `tech_gadget_buyer` | A1 | `electronics` | — | txn_count ≥ 2/ไตรมาส (≥ 8/ปี) | min 3 quarters active |
| S07 | `home_decor_lover` | A2 | `home`, `furniture` | ikea, homepro, index, robinson_home | txn_count ≥ 4 | min 3 active_months |
| S08 | `book_lover` | A2 | `bookstore`, `retail` | se_ed, b2s, kinokuniya, bookazine | txn_count ≥ 12 (avg 1/เดือน) | min 6 active_months |
| S09 | `sports_gear_buyer` | A1 | `sport`, `sporting_goods` | — | txn_count ≥ 2/ไตรมาส | min 3 quarters |
| S10 | `grocery_regular` | A2 | `supermarket`, `grocery` | tops, bigc, lotus, makro | txn_count ≥ 36 (avg 3/เดือน) | min 8 active_months |
| S11 | `convenience_store_addict` | A2 | `convenience` | 7eleven, familymart, lawson | txn_count ≥ 180 (avg 15/เดือน) | min 8 active_months |
| S12 | `department_store_loyal` | A1 | `department` | — | merchant_concentration ≥ 0.7 | min 6 txn |
| S13 | `marketplace_shopper` | A2 | `ecommerce`, `online` | shopee, lazada | txn_count ≥ 48 (avg 4/เดือน) | min 6 active_months |
| S14 | `subscription_stacker` | A7 | recurring | — | distinct_recurring_merchant ≥ 3/เดือน | min 6 consistent_months |
| S15 | `impulse_buyer` | A6 | — | — | high txn_count + high merchant_diversity + high spend_variance | min 24 txn |
| S16 | `brand_switcher` | A6 | — | — | merchant_concentration < 0.2 across all retail | min 24 retail_txn |
| S17 | `secondhand_buyer` | A2 | `marketplace` | carousell | txn_count ≥ 1 | — |
| S18 | `seasonal_shopper` | A4 | — | — | spend spike > 2x monthly_avg ช่วง 11.11, 12.12, Apr (Songkran) | min 1 spike detected |
| S19 | `premium_brand_loyal` | A3 | `retail`, `fashion` | — | avg_amount > P75 AND merchant_concentration ≥ 0.3 (repeat ≥ 3/ไตรมาส) | min 12 txn |

---

## 🎭 Entertainment & Lifestyle (11 tags)

| rule_id | customer_tag | sub_type | mcc_prefix | merchant_keywords | condition | threshold_12m |
|---------|-------------|----------|-----------|-------------------|-----------|--------------|
| E01 | `movie_lover` | A2 | `cinema`, `entertainment` | sf_cinema, major_cineplex, central_cinema | txn_count ≥ 24 (avg 2/เดือน) | min 6 active_months |
| E02 | `concert_goer` | A2 | `ticketing`, `event` | thai_ticket_major, eventpop, ticketmelon | txn_count ≥ 3 | — |
| E03 | `gym_member` | A7 | `fitness`, `gym` | fitness_first, virgin_active, jetts | recurring_txn สม่ำเสมอ ≥ 6 เดือน | min 6 months |
| E04 | `gamer` | A2 | `gaming`, `digital` | steam, playstation, xbox, garena | txn_count ≥ 12 | min 6 active_months |
| E05 | `night_owl_entertainer` | A4 | `entertainment`, `bar`, `cinema` | — | txn_hour ≥ 22:00, txn_count ≥ 24 | min 6 active_months |
| E06 | `karaoke_regular` | A2 | `entertainment`, `karaoke` | tawandang, zaa, red_star | txn_count ≥ 24 (avg 2/เดือน) | min 6 active_months |
| E07 | `spa_lover` | A1 | `spa`, `massage`, `personal_care` | — | txn_count ≥ 24 (avg 2/เดือน) | min 6 active_months |
| E08 | `music_festival_goer` | A2 | `ticketing`, `event` | thai_ticket_major, eventpop | txn_count ≥ 2 AND avg_amount > 1500 | — |
| E09 | `streaming_subscriber` | A7 | `digital`, `subscription` | netflix, disney_plus, youtube, hbo | distinct_streaming_merchant ≥ 2 recurring | min 6 months |
| E10 | `outdoor_adventurer` | A5 | `sport`, `travel` | decathlon | sport_txn ≥ 4 AND travel_txn ≥ 2 | — |
| E11 | `theme_park_visitor` | A2 | `entertainment`, `amusement` | universal, cartoon_network, dream_world | txn_count ≥ 1 | — |

---

## 🚗 Transport & Commute (10 tags)

| rule_id | customer_tag | sub_type | mcc_prefix | merchant_keywords | condition | threshold_12m |
|---------|-------------|----------|-----------|-------------------|-----------|--------------|
| TR01 | `daily_commuter` | A4 | `fuel`, `transit`, `bts`, `mrt` | — | txn_count weekday ≥ 240 วัน (avg 20/เดือน) | min 8 active_months |
| TR02 | `car_owner` | A5 | `fuel`, `parking`, `auto_service` | — | ครบ 3 MCC prefix: fuel + parking + auto_service | min 2 txn ต่อ prefix |
| TR03 | `grab_dependent` | A2 | `rideshare`, `transport` | grab | txn_count ≥ 180 (avg 15/เดือน) | min 8 active_months |
| TR04 | `taxi_user` | A1 | `taxi` | — | txn_count ≥ 24 AND grab_txn < taxi_txn | min 6 active_months |
| TR05 | `fuel_brand_loyal` | A2 | `fuel` | — | merchant_concentration ≥ 0.7 ใน fuel | min 12 fuel_txn |
| TR06 | `ev_driver` | A2 | `ev_charging`, `fuel` | ea_anywhere, pea_volta | txn_count ≥ 2 | — |
| TR07 | `bts_mrt_user` | A2 | `transit` | rabbit, mrt | txn_count ≥ 24 | min 6 active_months |
| TR08 | `motorbike_user` | A3 | `fuel` | — | avg_fuel_amount < 200 บาท AND txn_count ≥ 24 | min 8 active_months |
| TR09 | `parking_heavy` | A1 | `parking` | — | txn_count ≥ 180 (avg 15/เดือน) | min 6 active_months |
| TR10 | `long_distance_driver` | A2 | `fuel`, `toll` | — | toll_txn ≥ 12 OR fuel_txn_distinct_province ≥ 4 | — |

---

## 💊 Health & Wellness (9 tags)

| rule_id | customer_tag | sub_type | mcc_prefix | merchant_keywords | condition | threshold_12m |
|---------|-------------|----------|-----------|-------------------|-----------|--------------|
| H01 | `health_conscious` | A5 | `gym`, `pharmacy`, `health_food` | — | txn ≥ 2+ MCC prefix จาก [gym, pharmacy, health_food] | min 4 txn/prefix |
| H02 | `pharmacy_regular` | A1 | `pharmacy`, `drug_store` | — | txn_count ≥ 36 (avg 3/เดือน) | min 6 active_months |
| H03 | `hospital_visitor` | A1 | `hospital`, `clinic` | — | txn_count ≥ 2/ไตรมาส (≥ 8/ปี) | min 3 quarters |
| H04 | `supplement_buyer` | A2 | `pharmacy`, `health` | watsons, boots, vitaminclub | txn_count ≥ 12 (avg 1/เดือน) | min 6 active_months |
| H05 | `organic_food_lover` | A2 | `supermarket`, `grocery` | lemon_farm, villa_market, gourmet | txn_count ≥ 12 | min 6 active_months |
| H06 | `dental_care_conscious` | A1 | `dental` | — | txn_count ≥ 2 | — |
| H07 | `fitness_first_user` | A2 | `fitness`, `gym` | fitness_first | txn_count ≥ 6 recurring | min 3 months |
| H08 | `eye_care_regular` | A1 | `optician` | — | txn_count ≥ 2 | — |
| H09 | `maternal_care` | A5 | `hospital`, `baby`, `pharmacy` | mothercare | hospital_txn ≥ 2 AND baby_txn ≥ 4 ในช่วง 12 เดือนเดียวกัน | co-occurrence required |

---

## 💳 Financial Behavior (14 tags)

| rule_id | customer_tag | sub_type | mcc_prefix | merchant_keywords | condition | threshold_12m |
|---------|-------------|----------|-----------|-------------------|-----------|--------------|
| F01 | `high_spender` | A6 | — | — | total_spend_12m > P75 ของ portfolio | min 6 active_months |
| F02 | `mid_spender` | A6 | — | — | total_spend_12m ∈ [P25, P75] | min 6 active_months |
| F03 | `low_spender` | A6 | — | — | total_spend_12m < P25 ของ portfolio | min 6 active_months |
| F04 | `consistent_spender` | A6 | — | — | CV ของ monthly_spend < 0.3 | min 8 active_months |
| F05 | `seasonal_spender` | A6 | — | — | monthly_spend spike > 2x avg ≥ 2 ครั้ง/ปี | — |
| F06 | `end_of_month_spender` | A4 | — | — | ≥ 40% of monthly_spend วันที่ 25–31 | min 8 consistent_months |
| F07 | `paycheck_spender` | A4 | — | — | spend spike วันที่ 1–5 ≥ 40% of monthly, consistent | min 8 months |
| F08 | `installment_user` | A6 | — | — | installment_flag = true ≥ 1 txn/ไตรมาส | — |
| F09 | `high_utilization` | A6 | — | — | avg credit_utilization > 70% ≥ 6 months | — |
| F10 | `low_utilization` | A6 | — | — | avg credit_utilization < 20% ≥ 6 months | — |
| F11 | `multi_card_user` | A6 | — | — | avg_monthly_spend < P25 (บ่งชี้ว่ากระจายหลายบัตร) | — |
| F12 | `cash_advance_user` | A6 | — | — | txn_type = cash_advance ≥ 1 | — |
| F13 | `reward_maximizer` | A6 | — | — | ≥ 50% of spend ที่ MCC ที่ให้ points สูง (airline, dining, dept) | min 12 txn |
| F14 | `single_category_user` | A6 | — | — | top_mcc_share ≥ 0.8 ของ total spend | min 24 txn |

---

## 👨‍👩‍👧 Life Stage (10 tags)

| rule_id | customer_tag | sub_type | mcc_prefix | merchant_keywords | condition | threshold_12m |
|---------|-------------|----------|-----------|-------------------|-----------|--------------|
| L01 | `parent` | A5 | `baby`, `kids`, `dining` | mothercare, toys_r_us | baby_txn ≥ 12 AND family_dining_txn ≥ 12 | min 6 active_months |
| L02 | `new_parent` | A2 | `baby`, `pharmacy` | mothercare, enfamil | baby_txn spike ใน 12 เดือน (เทียบกับ prior period) | — |
| L03 | `pet_owner` | A2 | `pet` | pet_planet, petfriend | txn_count ≥ 12 (avg 1/เดือน) | min 6 active_months |
| L04 | `homeowner` | A5 | `home`, `utility` | homepro, scg, global_house | home_txn ≥ 4 AND utility_txn ≥ 4 | min 3 quarters |
| L05 | `senior_lifestyle` | A5 | `pharmacy`, `hospital`, `market` | — | pharmacy_share ≥ 30% AND hospital_txn ≥ 4 AND market_txn ≥ 24 | min 8 months |
| L06 | `empty_nester` | A6 | — | — | kids_merchant trend ลดลง YoY ≥ 50% AND travel/leisure เพิ่ม | trend detection |
| L07 | `teen_spender` | A5 | `gaming`, `fastfood`, `convenience` | — | ≥ 3 MCC dominant: gaming + fastfood + convenience, low avg_amount | min 24 txn |
| L08 | `career_starter` | A5 | `apparel`, `professional` | — | overall_spend < P25 AND apparel_txn ≥ 4 | — |
| L09 | `family_breadwinner` | A6 | — | — | total_spend > P75 AND mcc_diversity ≥ 6 distinct MCC prefix | min 8 active_months |
| L10 | `retiree_lifestyle` | A5 | `pharmacy`, `hospital`, `market` | — | txn_count weekday ≈ weekend (ratio 0.8–1.2) AND pharmacy_share > 20% | min 8 months |

---

## ⏰ Time Patterns (10 tags)

| rule_id | customer_tag | sub_type | condition |
|---------|-------------|----------|-----------|
| TP01 | `morning_person` | A4 | ≥ 40% of daily txn ก่อน 09:00 consistently |
| TP02 | `night_owl_spender` | A4 | ≥ 30% of txn หลัง 22:00 consistently |
| TP03 | `weekend_warrior` | A4 | ≥ 60% of total spend วันเสาร์-อาทิตย์ |
| TP04 | `weekday_spender` | A4 | ≥ 70% of total spend วันจันทร์-ศุกร์ |
| TP05 | `lunch_hour_regular` | A4 | spike txn ช่วง 12:00–14:00 ทุก weekday ≥ 48 txn ใน window นี้ |
| TP06 | `after_work_spender` | A4 | spike txn ช่วง 18:00–21:00 ≥ 30% of weekday txn |
| TP07 | `holiday_spender` | A4 | spend เพิ่ม > 50% ช่วงวันหยุดยาว ≥ 2 ครั้ง |
| TP08 | `payday_spike` | A4 | spend spike วันที่ 25–5 ต้นเดือน ≥ 30% consistently |
| TP09 | `monthly_planner` | A6 | CV ของ daily_spend ต่ำ, ไม่มี spike ชัดเจน |
| TP10 | `off_peak_shopper` | A4 | retail txn ≥ 60% ช่วง 09:00–12:00 วันจันทร์-ศุกร์ |

---

## 📱 Digital Behavior (8 tags)

| rule_id | customer_tag | sub_type | mcc_prefix | merchant_keywords | condition | threshold_12m |
|---------|-------------|----------|-----------|-------------------|-----------|--------------|
| DG01 | `online_native` | A6 | — | — | online_channel_txn / total_txn ≥ 0.7 | min 24 txn |
| DG02 | `contactless_payer` | A6 | — | — | tap_or_nfc_txn / in_store_txn ≥ 0.8 | min 24 in_store_txn |
| DG03 | `app_heavy_user` | A6 | — | — | mobile_app_txn / total_txn ≥ 0.5 | min 24 txn |
| DG04 | `digital_subscription_heavy` | A7 | `subscription` | — | distinct_digital_recurring_merchant ≥ 4/เดือน | min 6 months |
| DG05 | `streaming_only` | A7 | `digital` | netflix, disney_plus, youtube | streaming_txn ≥ 2 recurring AND cinema_txn = 0 | min 6 months |
| DG06 | `social_commerce_buyer` | A2 | `ecommerce` | tiktok_shop | txn_count ≥ 4 | — |
| DG07 | `crypto_curious` | A2 | `crypto`, `fintech` | bitkub, satang, zipmex | txn_count ≥ 1 | — |
| DG08 | `fintech_user` | A2 | `fintech`, `ewallet` | truemoney, rabbit_line_pay, promptpay | txn_count ≥ 24 (avg 2/เดือน) | min 6 active_months |

---

## สรุป Implementation Notes

### Columns ที่ต้องมีใน Transaction Table

| Column | ใช้ใน sub-type |
|--------|---------------|
| `customer_id` | ทุก rule |
| `merchant_tag` (format: mcc_prefix_merchant) | A1, A2 |
| `merchant_name` (raw) | A2 |
| `amount` | A3, F-tags |
| `txn_date` | ทุก rule (12m filter) |
| `txn_hour` | A4 |
| `txn_day_of_week` | A4 |
| `currency` | T02 |
| `channel` (online/in-store/app) | DG-tags |
| `payment_method` (tap/chip/etc.) | DG02 |
| `installment_flag` | F08 |
| `txn_type` (purchase/cash_advance) | F12 |
| `credit_utilization` | F09, F10 |

### Tags ที่ต้องระวัง

| Tag | ความซับซ้อน | หมายเหตุ |
|-----|------------|---------|
| `last_minute_booker`, `early_planner` | สูง | ต้องมี booking date ≠ travel date |
| `empty_nester` | สูง | ต้องการ YoY trend comparison |
| `new_parent` | กลาง | ต้องการ spike detection |
| `maternal_care` | กลาง | co-occurrence timing ซับซ้อน |
| `multi_card_user` | กลาง | inference จาก pattern ไม่แม่นยำ 100% |

### Tags ที่ทำได้เร็วที่สุด (Quick Win Phase 1)

Tags ที่ signal ชัด, ไม่ต้องการ column พิเศษ:

1. `frequent_diner` — aggregate dining MCC
2. `convenience_store_addict` — 7-Eleven/FamilyMart count
3. `grocery_regular` — supermarket count
4. `grab_dependent` — Grab count
5. `high_spender` / `mid_spender` / `low_spender` — pure spend percentile
6. `marketplace_shopper` — Shopee/Lazada count
7. `streaming_subscriber` — Netflix/Disney+ recurring
8. `frequent_traveler` — airline + hotel combo
9. `car_owner` — fuel + parking + auto_service combo
10. `pharmacy_regular` — pharmacy MCC count

---

*Draft v1.0 — Thena × Tee | 2026-04-15*
*Lookback: 12 months | Score threshold: ≥ 0.3 | Refresh: Daily (Option A)*
