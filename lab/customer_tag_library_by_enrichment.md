# Customer Tag Library — จัดกลุ่มตาม Enrichment Requirement
**Version**: 1.0 Draft | Total: 151 tags

---

## กลุ่ม A — ไม่ต้องใช้ Merchant Enrichment (117 tags)
> ทำได้เลยจาก **MCC + Merchant Name + Timestamp + Amount**
> เริ่ม build ได้ทันที — ไม่รอ Enrichment

---

### 🍽️ Food & Dining (13 tags)

| Tag | Definition | Signal |
|-----|-----------|--------|
| `frequent_diner` | กินข้าวนอกบ้าน ≥ 10 txn/เดือน | MCC: Restaurant |
| `fast_food_regular` | ซื้อ fast food ≥ 4 ครั้ง/เดือน | Merchant: McDonald's, KFC, BK |
| `fine_dining_enthusiast` | avg ticket ร้านอาหาร > P75 | MCC + Amount |
| `cafe_hopper` | ≥ 6 txn/เดือน ที่ร้านกาแฟ หลาย merchant | MCC: Coffee Shop |
| `bubble_tea_addict` | ≥ 8 txn/เดือน ที่ร้านชานมไข่มุก | Merchant: ChaTraMue, Gong Cha |
| `delivery_dependent` | ≥ 50% of dining spend ผ่าน delivery app | Merchant: GrabFood, LINE MAN |
| `brunch_person` | dining txn ช่วง 09:00–13:00 วันเสาร์-อาทิตย์ บ่อย | MCC + Timestamp |
| `late_night_diner` | dining txn หลัง 22:00 ≥ 4 ครั้ง/เดือน | MCC + Timestamp |
| `bakery_lover` | txn บ่อยที่ร้านเบเกอรี่ | Merchant: Yamazaki, BreadTalk |
| `budget_eater` | avg ticket dining < P25 | MCC + Amount |
| `solo_diner` | avg ticket ต่ำ, ไม่ซ้ำ merchant บ่อย | Amount pattern |
| `street_food_lover` | txn ร้านขนาดเล็ก ticket < 150 บาท | Amount + Merchant size |
| `dessert_lover` | ≥ 6 txn/เดือน ที่ร้านขนม/ไอศกรีม | Merchant: After You, Swensen's |

---

### ✈️ Travel (13 tags)

| Tag | Definition | Signal |
|-----|-----------|--------|
| `frequent_traveler` | airline + hotel txn ≥ 4 ครั้ง/ปี | MCC: Airlines + Hotel |
| `international_traveler` | foreign currency txn ≥ 2 ครั้ง/ปี | Currency ≠ THB |
| `domestic_traveler` | airline/hotel txn ในประเทศ ไม่มี foreign | MCC + Currency |
| `budget_traveler` | airline = LCC, hotel avg ticket ต่ำ | Merchant: AirAsia, Nok Air + Amount |
| `luxury_traveler` | airline = full-service, hotel avg ticket > P75 | Merchant: TG, SQ + Amount |
| `business_traveler` | airline txn วันจันทร์-ศุกร์ + hotel weekday | Timestamp + MCC |
| `leisure_traveler` | airline/hotel txn ช่วง weekend หรือวันหยุด | Timestamp + MCC |
| `hotel_loyalist` | ≥ 70% hotel txn ที่ chain เดียวกัน | Merchant concentration |
| `airbnb_user` | มี txn ที่ Airbnb ≥ 1 ครั้ง/ปี | Merchant: Airbnb |
| `frequent_flyer` | airline txn ≥ 6 ครั้ง/ปี | MCC: Airlines |
| `backpacker_style` | ท่องเที่ยวบ่อย แต่ avg spend ต่ำมาก | Frequency + Low amount |
| `last_minute_booker` | booking txn ก่อนวันเดินทาง < 7 วัน | Booking date pattern |
| `early_planner` | booking txn ล่วงหน้า > 30 วัน | Booking date pattern |

---

### 🛍️ Shopping (19 tags)

| Tag | Definition | Signal |
|-----|-----------|--------|
| `online_first_shopper` | ≥ 50% of txn เป็น online channel | Channel |
| `luxury_shopper` | txn ที่ luxury brand stores บ่อย หรือ avg ticket > P90 | Merchant + Amount |
| `fashion_lover` | ≥ 4 txn/เดือน ที่ร้านเสื้อผ้า/แฟชั่น | MCC: Apparel |
| `sneaker_enthusiast` | txn บ่อยที่ร้านรองเท้า/sneaker | Merchant: Nike, Adidas, New Balance |
| `beauty_conscious` | ≥ 3 txn/เดือน ที่ร้านเครื่องสำอาง | MCC: Cosmetics + Merchant |
| `tech_gadget_buyer` | txn ที่ร้าน electronics ≥ 2 ครั้ง/ไตรมาส | MCC: Electronics |
| `home_decor_lover` | txn บ่อยที่ furniture / home goods | Merchant: IKEA, HomePro |
| `book_lover` | txn ที่ bookstore ≥ 1 ครั้ง/เดือน | Merchant: Se-Ed, B2S, Kinokuniya |
| `sports_gear_buyer` | txn ที่ร้านอุปกรณ์กีฬา ≥ 2 ครั้ง/ไตรมาส | MCC: Sporting Goods |
| `grocery_regular` | supermarket txn ≥ 3 ครั้ง/เดือน | Merchant: Tops, BigC, Lotus's |
| `convenience_store_addict` | convenience store txn ≥ 15 ครั้ง/เดือน | Merchant: 7-Eleven, FamilyMart |
| `department_store_loyal` | ≥ 70% of dept txn ที่ chain เดียวกัน | Merchant concentration |
| `marketplace_shopper` | txn ที่ Shopee/Lazada ≥ 4 ครั้ง/เดือน | Merchant: Shopee, Lazada |
| `subscription_stacker` | recurring txn ≥ 3 บริการ/เดือน | Recurring pattern |
| `impulse_buyer` | txn สูง, หลาย merchant, pattern ไม่ consistent | Frequency + Merchant diversity |
| `brand_switcher` | merchant loyalty ต่ำ ชอบลองใหม่ | Low merchant concentration |
| `secondhand_buyer` | txn ที่ platform secondhand | Merchant: Carousell |
| `seasonal_shopper` | spike ช่วง sale season (11.11, 12.12, Songkran) | Timestamp + Amount spike |
| `premium_brand_loyal` | txn ซ้ำที่ premium brand เดิม > 3 ครั้ง/ไตรมาส | Merchant + Amount + Concentration |

---

### 🎭 Entertainment & Lifestyle (11 tags)

| Tag | Definition | Signal |
|-----|-----------|--------|
| `movie_lover` | cinema txn ≥ 2 ครั้ง/เดือน | Merchant: SF, Major, Central Cinema |
| `concert_goer` | event/concert ticketing ≥ 3 ครั้ง/ปี | Merchant: Thai Ticket Major, Eventpop |
| `gym_member` | recurring txn ที่ fitness center รายเดือน | Merchant: Fitness First, Virgin Active |
| `gamer` | txn ที่ gaming platform บ่อย | Merchant: Steam, PS Store |
| `night_owl_entertainer` | entertainment txn หลัง 22:00 บ่อย | MCC + Timestamp |
| `karaoke_regular` | txn ที่ karaoke ≥ 2 ครั้ง/เดือน | Merchant: Tawandang, Zaa |
| `spa_lover` | txn ที่ spa/massage ≥ 2 ครั้ง/เดือน | MCC: Personal Care |
| `music_festival_goer` | festival ticketing ≥ 2 ครั้ง/ปี | Merchant: ticketing + large amount |
| `streaming_subscriber` | ≥ 2 streaming subscriptions | Merchant: Netflix, Disney+, YouTube |
| `outdoor_adventurer` | txn ที่ outdoor gear + travel combo | Merchant: Decathlon + MCC combo |
| `theme_park_visitor` | txn ที่ theme park ≥ 1 ครั้ง/ปี | Merchant: Universal, Cartoon Network |

---

### 🚗 Transport & Commute (10 tags)

| Tag | Definition | Signal |
|-----|-----------|--------|
| `daily_commuter` | fuel/transit txn ≥ 20 วัน/เดือน weekday | MCC + Frequency + Timestamp |
| `car_owner` | ครบ 3 อย่าง: fuel + parking + car service | MCC combination |
| `grab_dependent` | Grab txn ≥ 15 ครั้ง/เดือน | Merchant: Grab |
| `taxi_user` | taxi txn บ่อย ไม่ใช้ Grab | MCC: Taxi |
| `fuel_brand_loyal` | ≥ 70% fuel txn ที่ปั๊มแบรนด์เดียวกัน | Merchant: PTT, Shell, Caltex |
| `ev_driver` | txn ที่ EV charging station | Merchant: EA Anywhere, PEA Volta |
| `bts_mrt_user` | txn ที่ BTS/MRT บ่อย | Merchant: Rabbit, MRT |
| `motorbike_user` | fuel txn amount < 200 บาท/ครั้ง สม่ำเสมอ | Amount pattern |
| `parking_heavy` | parking txn > 15 ครั้ง/เดือน | MCC: Parking |
| `long_distance_driver` | fuel txn ต่างจังหวัด หรือ toll txn บ่อย | Merchant location + MCC: Toll |

---

### 💊 Health & Wellness (9 tags)

| Tag | Definition | Signal |
|-----|-----------|--------|
| `health_conscious` | txn ครบ 2+ ใน: gym + pharmacy + health food | MCC combination |
| `pharmacy_regular` | pharmacy txn ≥ 3 ครั้ง/เดือน | MCC: Drug Store |
| `hospital_visitor` | hospital txn ≥ 2 ครั้ง/ไตรมาส | MCC: Hospital |
| `supplement_buyer` | txn ที่ร้าน health supplement บ่อย | Merchant: Watsons, Boots |
| `organic_food_lover` | txn ที่ organic/health food store | Merchant: Lemon Farm, Villa Market |
| `dental_care_conscious` | dental clinic txn ≥ 2 ครั้ง/ปี | MCC: Dental |
| `fitness_first_user` | gym txn ที่ Fitness First โดยเฉพาะ | Merchant: Fitness First |
| `eye_care_regular` | optician txn ≥ 2 ครั้ง/ปี | MCC: Opticians |
| `maternal_care` | txn ที่ OB/GYN + baby products ช่วงเวลาเดียวกัน | MCC combination + Timing |

---

### 💳 Financial Behavior (14 tags)

| Tag | Definition | Signal |
|-----|-----------|--------|
| `high_spender` | total monthly spend > P75 ของ portfolio | Amount |
| `mid_spender` | total monthly spend P25–P75 | Amount |
| `low_spender` | total monthly spend < P25 ของ portfolio | Amount |
| `consistent_spender` | coefficient of variation ของ monthly spend ต่ำ | Variance |
| `seasonal_spender` | spike > 2x avg spend ในช่วงเทศกาล | Timestamp + Amount |
| `end_of_month_spender` | ≥ 40% of monthly spend วันที่ 25–31 | Timestamp |
| `paycheck_spender` | spike spend ต้นเดือน (1–5) ทุกเดือน | Timestamp + Amount |
| `installment_user` | มี installment txn ≥ 1 ครั้ง/ไตรมาส | Installment flag |
| `high_utilization` | credit utilization > 70% สม่ำเสมอ | Utilization rate |
| `low_utilization` | credit utilization < 20% สม่ำเสมอ | Utilization rate |
| `multi_card_user` | spend pattern บ่งชี้มีบัตรหลายใบ (low spend ต่อใบ) | Spend pattern |
| `cash_advance_user` | มี cash advance txn ≥ 1 ครั้ง/ปี | Transaction type |
| `reward_maximizer` | txn กระจุกที่ merchant ที่ให้ points สูง | Merchant + Reward pattern |
| `single_category_user` | ≥ 80% of spend อยู่ใน MCC เดียว | MCC concentration |

---

### 👨‍👩‍👧 Life Stage — inferred (10 tags)

| Tag | Definition | Signal |
|-----|-----------|--------|
| `parent` | txn บ่อยที่ baby/kids products + family restaurant | Merchant: Mothercare + Family MCC |
| `new_parent` | spike ที่ baby products ใน 12 เดือนที่ผ่านมา | Merchant + Recency |
| `pet_owner` | txn ที่ pet shop / vet clinic ≥ 1 ครั้ง/เดือน | Merchant: Pet Planet, สัตวแพทย์ |
| `homeowner` | txn ที่ home improvement / utility ≥ 1 ครั้ง/ไตรมาส | Merchant: HomePro, SCG |
| `senior_lifestyle` | txn เน้น pharmacy + hospital + traditional market | MCC combination |
| `empty_nester` | ลดลงที่ children merchant + เพิ่มที่ travel/leisure | Merchant trend |
| `teen_spender` | gaming + fast food + convenience store dominant | MCC combination |
| `career_starter` | low overall spend + professional attire purchase | Amount + MCC |
| `family_breadwinner` | high spend + diverse category ครอบคลุม family needs | Amount + Category diversity |
| `retiree_lifestyle` | txn pattern เสมอกันทั้งวันธรรมดา/หยุด + pharmacy heavy | Timestamp uniformity + MCC |

---

### ⏰ Time Patterns (10 tags)

| Tag | Definition | Signal |
|-----|-----------|--------|
| `morning_person` | ≥ 40% of daily txn ก่อน 09:00 | Timestamp |
| `night_owl_spender` | ≥ 30% of txn หลัง 22:00 | Timestamp |
| `weekend_warrior` | ≥ 60% of spend วันเสาร์-อาทิตย์ | Timestamp |
| `weekday_spender` | ≥ 70% of spend วันจันทร์-ศุกร์ | Timestamp |
| `lunch_hour_regular` | spike txn ช่วง 12:00–14:00 ทุก weekday | Timestamp |
| `after_work_spender` | spike txn ช่วง 18:00–21:00 | Timestamp |
| `holiday_spender` | spend เพิ่ม > 50% ช่วงวันหยุดยาว | Timestamp + Amount |
| `payday_spike` | spend spike ต้นเดือน แล้วลดลง | Timestamp + Amount pattern |
| `monthly_planner` | txn กระจาย consistent ตลอดเดือน ไม่มี spike | Variance |
| `off_peak_shopper` | retail txn ส่วนใหญ่ช่วงเช้าวันธรรมดา | Timestamp |

---

### 📱 Digital Behavior (8 tags)

| Tag | Definition | Signal |
|-----|-----------|--------|
| `online_native` | ≥ 70% of all txn เป็น online channel | Channel |
| `contactless_payer` | ≥ 80% of in-store txn เป็น tap/NFC | Payment method |
| `app_heavy_user` | ≥ 50% of txn ผ่าน mobile app | Channel |
| `digital_subscription_heavy` | ≥ 4 recurring digital subscriptions/เดือน | Recurring + Digital merchant |
| `streaming_only` | entertainment spend เกือบทั้งหมดเป็น streaming ไม่มี cinema | Merchant pattern |
| `social_commerce_buyer` | txn ผ่าน TikTok Shop | Merchant: TikTok Shop |
| `crypto_curious` | txn ที่ crypto exchange ≥ 1 ครั้ง | Merchant: Bitkub, Satang |
| `fintech_user` | txn ผ่าน fintech platform บ่อย | Merchant: TrueMoney, Rabbit LINE Pay |

---
---

## กลุ่ม B — ต้องใช้ Merchant Enrichment (34 tags)
> ต้องมี attribute เพิ่มเติมใน merchant table ก่อน เช่น cuisine type, venue type, location tag
> ทำได้เมื่อ Enrichment พร้อม

---

### 🍽️ Food & Dining (12 tags)

| Tag | Definition | Enrichment ที่ต้องการ |
|-----|-----------|----------------------|
| `japanese_food_lover` | ≥ 50% of dining txn ที่ร้านอาหารญี่ปุ่น | cuisine = Japanese |
| `korean_food_lover` | ≥ 50% of dining txn ที่ร้านอาหารเกาหลี | cuisine = Korean |
| `chinese_food_lover` | ≥ 50% of dining txn ที่ร้านอาหารจีน | cuisine = Chinese |
| `thai_food_loyalist` | ≥ 60% of dining txn ที่ร้านอาหารไทย | cuisine = Thai |
| `western_food_lover` | ≥ 50% of dining txn ที่ร้านอาหารตะวันตก | cuisine = Western |
| `italian_food_lover` | ≥ 50% of dining txn ที่ร้านอาหารอิตาเลียน | cuisine = Italian |
| `seafood_lover` | txn บ่อยที่ร้านอาหารทะเล | cuisine = Seafood |
| `vegetarian_friendly` | txn บ่อยที่ร้าน vegetarian / plant-based | diet = Vegetarian |
| `food_court_regular` | txn บ่อยที่ food court ในห้าง | venue_type = Food Court |
| `buffet_lover` | txn ที่ร้านบุฟเฟ่ต์ ≥ 2 ครั้ง/เดือน | venue_type = Buffet |
| `family_restaurant_goer` | dining txn ที่ร้าน family-friendly สูง | segment = Family |
| `healthy_eater` | txn บ่อยที่ร้าน healthy food / salad | diet = Healthy |

---

### ✈️ Travel (5 tags)

| Tag | Definition | Enrichment ที่ต้องการ |
|-----|-----------|----------------------|
| `asia_traveler` | foreign txn ส่วนใหญ่ใน Asia | merchant_country = Asia |
| `asia_pacific_traveler` | foreign txn ครอบคลุม SEA + East Asia | merchant_country = APAC |
| `europe_traveler` | foreign txn ที่ European merchants | merchant_country = Europe |
| `resort_lover` | hotel txn ที่ resort บ่อย | hotel_type = Resort |
| `city_traveler` | hotel txn ที่ city hotel มากกว่า resort | hotel_type = City Hotel |

---

### 🛍️ Shopping (3 tags)

| Tag | Definition | Enrichment ที่ต้องการ |
|-----|-----------|----------------------|
| `mall_shopper` | ≥ 60% of retail txn ที่ merchant ในห้าง | merchant_location = Mall |
| `bargain_hunter` | txn บ่อยที่ outlet / discount store | venue_type = Outlet |
| `gifting_regular` | txn ที่ gift shop / ช่วงเทศกาล สม่ำเสมอ | merchant_type = Gift Shop |

---

### 🎭 Entertainment & Lifestyle (7 tags)

| Tag | Definition | Enrichment ที่ต้องการ |
|-----|-----------|----------------------|
| `sports_fan` | txn ที่ stadium / sports event ≥ 2 ครั้ง/ปี | venue_type = Stadium |
| `yoga_practitioner` | txn ที่ yoga studio ≥ 2 ครั้ง/เดือน | activity_type = Yoga |
| `golf_player` | txn ที่ golf course ≥ 1 ครั้ง/เดือน | activity_type = Golf |
| `art_culture_enthusiast` | txn ที่ museum / gallery / art event | venue_type = Cultural |
| `escape_room_fan` | txn ที่ escape room ≥ 2 ครั้ง/ไตรมาส | venue_type = Escape Room |
| `board_game_cafe_goer` | txn ที่ board game cafe บ่อย | venue_type = Board Game Cafe |
| `bowling_regular` | txn ที่ bowling alley ≥ 1 ครั้ง/เดือน | venue_type = Bowling |

---

### 💊 Health & Wellness (3 tags)

| Tag | Definition | Enrichment ที่ต้องการ |
|-----|-----------|----------------------|
| `beauty_clinic_visitor` | aesthetic/beauty clinic txn บ่อย | clinic_type = Aesthetic |
| `mental_health_aware` | txn ที่ therapy / wellness center | clinic_type = Mental Health |
| `traditional_medicine` | txn ที่ร้านยาแผนโบราณ / แพทย์แผนจีน | clinic_type = TCM |

---

### 👨‍👩‍👧 Life Stage (4 tags)

| Tag | Definition | Enrichment ที่ต้องการ |
|-----|-----------|----------------------|
| `student` | txn ใกล้มหาวิทยาลัย + stationery + low spend | merchant_location = University Area |
| `young_professional` | coffee weekday เช้า + lunch ใกล้ office district | merchant_location = Office District |
| `newly_married` | spike ที่ wedding vendor + honeymoon travel | merchant_type = Wedding |
| `college_age` | txn ใกล้มหาวิทยาลัย + delivery + low ticket | merchant_location = University Area |

---

## สรุปภาพรวม

| | Tags | สัดส่วน |
|---|---|---|
| **กลุ่ม A** — ไม่ต้อง Enrichment | **117 tags** | 78% |
| **กลุ่ม B** — ต้อง Enrichment | **34 tags** | 22% |
| **รวม** | **151 tags** | 100% |

**แนะนำ**: เริ่ม implement กลุ่ม A ก่อน — ได้ 78% ของ tag library โดยไม่รอ Enrichment

---

*Draft v1.0 — Thena × Data Science Team*
