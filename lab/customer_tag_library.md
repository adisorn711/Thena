# Customer Tag Library
**Version**: 1.0 Draft  
**Total**: 151 tags / 10 dimensions  
**Signal source**: MCC + Merchant Name + Timestamp + Amount

---

## Format
| Tag | Definition | Primary Signal |
|-----|-----------|----------------|

---

## 1. Food & Dining (25 tags)

| Tag | Definition | Primary Signal |
|-----|-----------|----------------|
| `frequent_diner` | กินข้าวนอกบ้านบ่อย ≥ 10 txn/เดือน | MCC: Food & Restaurant |
| `fast_food_regular` | ซื้อ fast food ≥ 4 ครั้ง/เดือน | Merchant: McDonald's, KFC, BK, MK |
| `fine_dining_enthusiast` | avg ticket ร้านอาหาร > P75 ของ portfolio | MCC + Amount |
| `japanese_food_lover` | ≥ 50% of dining txn ที่ร้านอาหารญี่ปุ่น | Merchant Enrichment: cuisine=Japanese |
| `korean_food_lover` | ≥ 50% of dining txn ที่ร้านอาหารเกาหลี | Merchant Enrichment: cuisine=Korean |
| `chinese_food_lover` | ≥ 50% of dining txn ที่ร้านอาหารจีน | Merchant Enrichment: cuisine=Chinese |
| `thai_food_loyalist` | ≥ 60% of dining txn ที่ร้านอาหารไทย | Merchant Enrichment: cuisine=Thai |
| `western_food_lover` | ≥ 50% of dining txn ที่ร้านอาหารตะวันตก | Merchant Enrichment: cuisine=Western |
| `italian_food_lover` | ≥ 50% of dining txn ที่ร้านอาหารอิตาเลียน | Merchant Enrichment: cuisine=Italian |
| `seafood_lover` | txn บ่อยที่ร้านอาหารทะเล | Merchant Enrichment: cuisine=Seafood |
| `vegetarian_friendly` | txn บ่อยที่ร้าน vegetarian / plant-based | Merchant Enrichment: diet=Vegetarian |
| `cafe_hopper` | ≥ 6 txn/เดือน ที่ร้านกาแฟ หลาย merchant | MCC: Coffee Shop |
| `bubble_tea_addict` | ≥ 8 txn/เดือน ที่ร้านชานมไข่มุก | Merchant: ChaTraMue, Tiger Sugar, Gong Cha |
| `delivery_dependent` | ≥ 50% of dining spend ผ่าน delivery app | Merchant: Grab Food, LINE MAN, Robinhood |
| `brunch_person` | dining txn ช่วง 09:00–13:00 วันเสาร์-อาทิตย์ บ่อย | MCC + Timestamp |
| `late_night_diner` | dining txn หลัง 22:00 บ่อย ≥ 4 ครั้ง/เดือน | MCC + Timestamp |
| `food_court_regular` | txn บ่อยที่ food court ในห้าง | Merchant Enrichment: type=Food Court |
| `bakery_lover` | txn บ่อยที่ร้านเบเกอรี่ / bread shop | Merchant: Yamazaki, BreadTalk, กูร์เมต์ |
| `buffet_lover` | txn ที่ร้านบุฟเฟ่ต์ ≥ 2 ครั้ง/เดือน | Merchant Enrichment: type=Buffet |
| `family_restaurant_goer` | dining txn ที่ร้าน family-friendly สูง | Merchant Enrichment: segment=Family |
| `budget_eater` | avg ticket dining < P25 ของ portfolio | MCC + Amount |
| `solo_diner` | avg ticket dining ต่ำ, txn ครั้งเดียวไม่บ่อยซ้ำ merchant | Amount pattern |
| `street_food_lover` | txn ที่ร้านอาหารขนาดเล็ก/รถเข็น, ticket ต่ำ | Amount + Merchant size |
| `dessert_lover` | ≥ 6 txn/เดือน ที่ร้านขนม/ไอศกรีม | Merchant: After You, Swensen's, Dairy Queen |
| `healthy_eater` | txn บ่อยที่ร้าน healthy food / salad | Merchant Enrichment: diet=Healthy |

---

## 2. Travel (18 tags)

| Tag | Definition | Primary Signal |
|-----|-----------|----------------|
| `frequent_traveler` | มี airline + hotel txn ≥ 4 ครั้ง/ปี | MCC: Airlines + Hotel |
| `international_traveler` | มี foreign currency txn ≥ 2 ครั้ง/ปี | Currency code ≠ THB |
| `domestic_traveler` | มี domestic airline/hotel txn ไม่มี foreign | MCC + Currency |
| `budget_traveler` | airline = LCC, hotel avg ticket ต่ำ | Merchant: AirAsia, Nok Air + Amount |
| `luxury_traveler` | airline = full-service, hotel avg ticket > P75 | Merchant: TG, SQ + Amount |
| `business_traveler` | airline txn วันจันทร์-ศุกร์ + hotel txn weekday | Timestamp + MCC |
| `leisure_traveler` | airline/hotel txn ช่วง weekend หรือวันหยุด | Timestamp + MCC |
| `hotel_loyalist` | ≥ 70% hotel txn ที่ chain เดียวกัน | Merchant concentration |
| `airbnb_user` | มี txn ที่ Airbnb ≥ 1 ครั้ง/ปี | Merchant: Airbnb |
| `frequent_flyer` | airline txn ≥ 6 ครั้ง/ปี | MCC: Airlines |
| `asia_traveler` | foreign txn ใน Asia timezone / Asian merchants | Merchant location |
| `asia_pacific_traveler` | foreign txn ครอบคลุม SEA + East Asia | Merchant location |
| `europe_traveler` | foreign txn ที่ European merchants | Merchant location |
| `backpacker_style` | ท่องเที่ยวบ่อย แต่ avg spend ต่ำมาก | Frequency + Low amount |
| `last_minute_booker` | booking txn ใกล้วันเดินทาง < 7 วัน | Booking pattern (inferred) |
| `early_planner` | booking txn ล่วงหน้า > 30 วัน | Booking pattern (inferred) |
| `resort_lover` | hotel txn ที่ resort / beach destination บ่อย | Merchant Enrichment: type=Resort |
| `city_traveler` | hotel txn ที่ city hotel มากกว่า resort | Merchant Enrichment: type=City Hotel |

---

## 3. Shopping (22 tags)

| Tag | Definition | Primary Signal |
|-----|-----------|----------------|
| `mall_shopper` | ≥ 60% of retail txn ที่ merchant ในห้างสรรพสินค้า | Merchant Enrichment: location=Mall |
| `online_first_shopper` | ≥ 50% of txn เป็น online channel | Channel: Online |
| `luxury_shopper` | txn ที่ luxury brand stores บ่อย หรือ avg ticket > P90 | Merchant + Amount |
| `fashion_lover` | ≥ 4 txn/เดือน ที่ร้านเสื้อผ้า/แฟชั่น | MCC: Apparel |
| `sneaker_enthusiast` | txn บ่อยที่ร้านรองเท้า/sneaker brands | Merchant: Nike, Adidas, New Balance |
| `beauty_conscious` | ≥ 3 txn/เดือน ที่ร้านเครื่องสำอาง/สกินแคร์ | MCC: Cosmetics + Merchant |
| `tech_gadget_buyer` | txn ที่ร้าน electronics ≥ 2 ครั้ง/ไตรมาส | MCC: Electronics |
| `home_decor_lover` | txn บ่อยที่ furniture / home goods stores | Merchant: IKEA, Index, HomePro |
| `book_lover` | txn ที่ bookstore ≥ 1 ครั้ง/เดือน | Merchant: Se-Ed, B2S, Kinokuniya |
| `sports_gear_buyer` | txn ที่ร้านอุปกรณ์กีฬา ≥ 2 ครั้ง/ไตรมาส | MCC: Sporting Goods |
| `bargain_hunter` | txn บ่อยที่ outlet / discount store | Merchant Enrichment: type=Outlet |
| `grocery_regular` | supermarket txn ≥ 3 ครั้ง/เดือน | Merchant: Tops, BigC, Lotus's |
| `convenience_store_addict` | convenience store txn ≥ 15 ครั้ง/เดือน | Merchant: 7-Eleven, FamilyMart |
| `department_store_loyal` | ≥ 70% of department txn ที่ chain เดียวกัน | Merchant concentration |
| `marketplace_shopper` | txn ที่ Shopee/Lazada ≥ 4 ครั้ง/เดือน | Merchant: Shopee, Lazada |
| `subscription_stacker` | มี recurring txn ≥ 3 บริการ/เดือน | Recurring pattern |
| `impulse_buyer` | txn สูง, หลาย merchant, pattern ไม่ consistent | Frequency + Merchant diversity |
| `brand_switcher` | merchant loyalty ต่ำ ชอบลองใหม่ | Low merchant concentration |
| `secondhand_buyer` | txn ที่ platform secondhand | Merchant: Carousell, etc. |
| `seasonal_shopper` | spike ช่วง sale season (11.11, 12.12, Songkran) | Timestamp + Amount spike |
| `gifting_regular` | txn ที่ gift shop / ช่วงเทศกาล สม่ำเสมอ | Merchant + Timestamp |
| `premium_brand_loyal` | txn ซ้ำที่ premium brand เดิม > 3 ครั้ง/ไตรมาส | Merchant + Amount |

---

## 4. Entertainment & Lifestyle (18 tags)

| Tag | Definition | Primary Signal |
|-----|-----------|----------------|
| `movie_lover` | cinema txn ≥ 2 ครั้ง/เดือน | Merchant: SF, Major, Central Cinema |
| `concert_goer` | txn ที่ event/concert ticketing ≥ 3 ครั้ง/ปี | Merchant: Thai Ticket Major, Eventpop |
| `sports_fan` | txn ที่ stadium / sports event ≥ 2 ครั้ง/ปี | Merchant Enrichment: type=Stadium |
| `gym_member` | recurring txn ที่ fitness center รายเดือน | Merchant: Fitness First, Virgin Active |
| `yoga_practitioner` | txn ที่ yoga studio ≥ 2 ครั้ง/เดือน | Merchant Enrichment: type=Yoga |
| `gamer` | txn ที่ gaming platform / gaming store บ่อย | Merchant: Steam, PS Store, GameStop |
| `night_owl_entertainer` | entertainment txn หลัง 22:00 บ่อย | MCC + Timestamp |
| `karaoke_regular` | txn ที่ karaoke ≥ 2 ครั้ง/เดือน | Merchant: Tawandang, Zaa |
| `spa_lover` | txn ที่ spa/massage ≥ 2 ครั้ง/เดือน | MCC: Personal Care |
| `music_festival_goer` | txn ที่ festival ticketing ≥ 2 ครั้ง/ปี | Merchant + Large amount + Seasonal |
| `streaming_subscriber` | ≥ 2 streaming service subscriptions | Merchant: Netflix, Disney+, YouTube |
| `golf_player` | txn ที่ golf course / golf shop ≥ 1 ครั้ง/เดือน | Merchant Enrichment: sport=Golf |
| `outdoor_adventurer` | txn ที่ adventure/outdoor gear store | Merchant: Decathlon + travel combo |
| `art_culture_enthusiast` | txn ที่ museum / gallery / art event | Merchant Enrichment: type=Culture |
| `escape_room_fan` | txn ที่ escape room ≥ 2 ครั้ง/ไตรมาส | Merchant Enrichment: type=Escape Room |
| `theme_park_visitor` | txn ที่ theme park ≥ 1 ครั้ง/ปี | Merchant: Universal, Cartoon Network |
| `board_game_cafe_goer` | txn ที่ board game cafe บ่อย | Merchant Enrichment: type=Board Game |
| `bowling_regular` | txn ที่ bowling alley ≥ 1 ครั้ง/เดือน | Merchant Enrichment: type=Bowling |

---

## 5. Transport & Commute (10 tags)

| Tag | Definition | Primary Signal |
|-----|-----------|----------------|
| `daily_commuter` | txn ที่ fuel/transit ≥ 20 วัน/เดือน weekday | MCC + Frequency + Timestamp |
| `car_owner` | มี txn ครบ 3 อย่าง: fuel + parking + car service | MCC combination |
| `grab_dependent` | Grab txn ≥ 15 ครั้ง/เดือน | Merchant: Grab |
| `taxi_user` | taxi txn บ่อย แต่ไม่ใช้ Grab | MCC: Taxi |
| `fuel_brand_loyal` | ≥ 70% fuel txn ที่ปั๊มแบรนด์เดียวกัน | Merchant: PTT, Shell, Caltex |
| `ev_driver` | มี txn ที่ EV charging station | Merchant: EA Anywhere, PEA Volta |
| `bts_mrt_user` | txn ที่ BTS/MRT บ่อย | Merchant: Rabbit, MRT |
| `motorbike_user` | fuel txn amount ต่ำมาก < 200 บาท/ครั้ง | Amount pattern |
| `parking_heavy` | parking txn > 15 ครั้ง/เดือน | MCC: Parking |
| `long_distance_driver` | fuel txn ที่ต่างจังหวัด หรือ toll txn | Merchant location + MCC: Toll |

---

## 6. Health & Wellness (12 tags)

| Tag | Definition | Primary Signal |
|-----|-----------|----------------|
| `health_conscious` | txn ครบ 2+ ใน: gym + pharmacy + health food | MCC combination |
| `pharmacy_regular` | pharmacy txn ≥ 3 ครั้ง/เดือน | MCC: Drug Store |
| `hospital_visitor` | hospital txn ≥ 2 ครั้ง/ไตรมาส | MCC: Hospital |
| `supplement_buyer` | txn ที่ร้าน health supplement บ่อย | Merchant: Watsons, Boots health section |
| `organic_food_lover` | txn ที่ organic / health food store | Merchant: Lemon Farm, Villa Market |
| `dental_care_conscious` | dental clinic txn ≥ 2 ครั้ง/ปี | MCC: Dental |
| `beauty_clinic_visitor` | aesthetic/beauty clinic txn บ่อย | Merchant Enrichment: type=Aesthetic Clinic |
| `mental_health_aware` | txn ที่ therapy / wellness center | Merchant Enrichment: type=Mental Health |
| `fitness_first_user` | gym txn เฉพาะ Fitness First chain | Merchant: Fitness First |
| `traditional_medicine` | txn ที่ร้านยาแผนโบราณ / แพทย์แผนจีน | Merchant Enrichment: type=TCM |
| `eye_care_regular` | optician txn ≥ 2 ครั้ง/ปี | MCC: Opticians |
| `maternal_care` | txn ที่ OB/GYN + baby products ในช่วงเวลาเดียวกัน | MCC combination + Timing |

---

## 7. Financial Behavior (14 tags)

| Tag | Definition | Primary Signal |
|-----|-----------|----------------|
| `high_spender` | total monthly spend > P75 ของ portfolio | Amount |
| `mid_spender` | total monthly spend P25–P75 | Amount |
| `low_spender` | total monthly spend < P25 ของ portfolio | Amount |
| `consistent_spender` | coefficient of variation ของ monthly spend ต่ำ | Variance |
| `seasonal_spender` | spike > 2x avg spend ในช่วงเทศกาล | Timestamp + Amount |
| `end_of_month_spender` | ≥ 40% of monthly spend เกิดวันที่ 25–31 | Timestamp |
| `paycheck_spender` | spike spend ต้นเดือน (1–5) ทุกเดือน | Timestamp + Amount |
| `installment_user` | มี installment txn ≥ 1 ครั้ง/ไตรมาส | Installment flag |
| `high_utilization` | credit utilization > 70% สม่ำเสมอ | Utilization rate |
| `low_utilization` | credit utilization < 20% สม่ำเสมอ | Utilization rate |
| `multi_card_user` | txn pattern บ่งชี้ว่ามีบัตรหลายใบ (low spend ต่อใบ) | Spend pattern |
| `cash_advance_user` | มี cash advance txn ≥ 1 ครั้ง/ปี | Transaction type |
| `reward_maximizer` | txn กระจุกตัวที่ merchant ที่ให้ points สูง | Merchant + Reward pattern |
| `single_category_user` | ≥ 80% of spend อยู่ใน MCC เดียว | MCC concentration |

---

## 8. Life Stage — inferred (14 tags)

| Tag | Definition | Primary Signal |
|-----|-----------|----------------|
| `parent` | txn ที่ baby/kids products + family restaurant บ่อย | Merchant: Mothercare + Family MCC |
| `new_parent` | spike ที่ baby products ใน 12 เดือนที่ผ่านมา | Merchant + Recency |
| `student` | txn ที่ university area + stationery + low overall spend | Merchant location + Amount |
| `young_professional` | coffee weekday ช่วงเช้า + lunch ใกล้ office district | Merchant + Timestamp + Location |
| `pet_owner` | txn ที่ pet shop / vet clinic ≥ 1 ครั้ง/เดือน | Merchant: Pet Planet, สัตวแพทย์ |
| `homeowner` | txn ที่ home improvement / utility ≥ 1 ครั้ง/ไตรมาส | Merchant: HomePro, SCG, GlobalHouse |
| `senior_lifestyle` | txn เน้น pharmacy + hospital + traditional market | MCC combination |
| `newly_married` | spike ที่ wedding vendor + honeymoon travel ใน 12 เดือน | Merchant + Timing |
| `empty_nester` | ลดลงที่ children-related merchant + เพิ่มที่ travel/leisure | Merchant trend |
| `teen_spender` | gaming + fast food + convenience store dominant | MCC combination |
| `college_age` | txn ใกล้มหาวิทยาลัย + low avg ticket + delivery | Location + Amount |
| `career_starter` | low overall spend + professional attire purchase | Amount + MCC |
| `family_breadwinner` | high spend + diverse category ครอบคลุม family needs | Amount + Category diversity |
| `retiree_lifestyle` | txn pattern ไม่ต่างวันธรรมดา/หยุด + pharmacy heavy | Timestamp uniformity + MCC |

---

## 9. Time Patterns (10 tags)

| Tag | Definition | Primary Signal |
|-----|-----------|----------------|
| `morning_person` | ≥ 40% of daily txn ก่อน 09:00 | Timestamp |
| `night_owl_spender` | ≥ 30% of txn หลัง 22:00 | Timestamp |
| `weekend_warrior` | ≥ 60% of spend เกิดวันเสาร์-อาทิตย์ | Timestamp |
| `weekday_spender` | ≥ 70% of spend เกิดวันจันทร์-ศุกร์ | Timestamp |
| `lunch_hour_regular` | spike txn ช่วง 12:00–14:00 ทุก weekday | Timestamp |
| `after_work_spender` | spike txn ช่วง 18:00–21:00 | Timestamp |
| `holiday_spender` | spend เพิ่ม > 50% ช่วงวันหยุดยาว | Timestamp + Amount |
| `payday_spike` | spend spike ต้นเดือน แล้วลดลง | Timestamp + Amount pattern |
| `monthly_planner` | txn กระจาย consistent ตลอดเดือน ไม่มี spike | Variance |
| `off_peak_shopper` | retail txn ส่วนใหญ่ช่วงเช้าวันธรรมดา (ไม่ใช่ rush hour) | Timestamp |

---

## 10. Digital Behavior (8 tags)

| Tag | Definition | Primary Signal |
|-----|-----------|----------------|
| `online_native` | ≥ 70% of all txn เป็น online channel | Channel |
| `contactless_payer` | ≥ 80% of in-store txn เป็น tap/NFC | Payment method |
| `app_heavy_user` | ≥ 50% of txn ผ่าน mobile app | Channel |
| `digital_subscription_heavy` | ≥ 4 recurring digital subscriptions/เดือน | Recurring + Digital merchant |
| `streaming_only` | entertainment spend เกือบทั้งหมดเป็น streaming ไม่มี cinema | Merchant pattern |
| `social_commerce_buyer` | txn ผ่าน platform ที่มาจาก social (TikTok Shop) | Merchant: TikTok Shop |
| `crypto_curious` | มี txn ที่ crypto exchange ≥ 1 ครั้ง | Merchant: Bitkub, Satang |
| `fintech_user` | txn ผ่าน fintech platform บ่อย | Merchant: TrueMoney, Rabbit LINE Pay |

---

## Summary

| Dimension | Tags | Requires Enrichment? |
|-----------|------|---------------------|
| Food & Dining | 25 | บางส่วน (cuisine type) |
| Travel | 18 | น้อย (MCC + Currency) |
| Shopping | 22 | บางส่วน (location, type) |
| Entertainment | 18 | บางส่วน |
| Transport | 10 | น้อยมาก |
| Health & Wellness | 12 | บางส่วน |
| Financial Behavior | 14 | ไม่ต้อง |
| Life Stage | 14 | บางส่วน |
| Time Patterns | 10 | ไม่ต้อง |
| Digital Behavior | 8 | ไม่ต้อง |
| **Total** | **151** | |

---

*Draft v1.0 — Thena × Data Science Team*
