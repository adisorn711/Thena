# Customer Tag Library — Version 2.2
**Version**: 2.2 | **Updated**: 2026-04-27
**v1**: 151 | **v2**: +152 | **v2.1 (enrichment)**: +20 | **v2.2 (payment/card/momentum)**: +19 | **Total**: 342 tags

> `[A]` = ไม่ต้องรอ Enrichment | `[B]` = ต้องรอ Enrichment (direct mapping)
>
> **Stability Type:**
> `S` = **Stable** — พฤติกรรมหลัก ควร stable ตลอดเวลา | เกณฑ์: tag churn < 20%/เดือน
> `V` = **Variable** — event-based หรือ seasonal ที่ fluctuate ได้ตามธรรมชาติ — ไม่ใช่ bug
> `M` = **Momentum** — ออกแบบให้เปลี่ยนได้ แต่ค่อยๆ เปลี่ยน (transitional / trend-based)

> **Source**: `Existing` = มีอยู่แล้ว (ไม่มี enrichment tag ตรงๆ) | `Overlap` = มีอยู่แล้ว + ตรงกับ enrichment tag ของทีม | `New` = เพิ่มใหม่จาก enrichment review
> **Enrichment Tag**: ชื่อ tag จากลิสต์ทีม 99 อัน ที่ตรงกับ customer tag นี้ (`-` = ไม่มี)

---

## หมวดที่ขยายจาก v1

---

### 🍽️ Food & Dining
> v1: 25 | v2: +8 | v2.1: +14 | รวม: 47 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `frequent_diner` | กินข้าวนอกบ้าน ≥ 10 txn/เดือน | MCC: Dining | A | Overlap | Food | S |
| `fast_food_regular` | fast food ≥ 4 ครั้ง/เดือน | Merchant: McDonald's, KFC | A | Overlap | QSR, Burgers/Sandwiches, Fried Chicken, Other Fastfood | S |
| `fine_dining_enthusiast` | avg ticket > P75 | MCC + Amount | A | Overlap | Fine Dine | S |
| `cafe_hopper` | ร้านกาแฟ ≥ 6 ครั้ง/เดือน หลาย merchant | MCC: Coffee | A | Overlap | Cafe/Bistro, Coffee | S |
| `bubble_tea_addict` | ชานมไข่มุก ≥ 8 ครั้ง/เดือน | Merchant: Gong Cha, ChaTraMue | A | Existing | - | S |
| `delivery_dependent` | ≥ 50% dining ผ่าน delivery app | Merchant: GrabFood, LINE MAN | A | Existing | - | S |
| `brunch_person` | dining Sat-Sun 09:00–13:00 บ่อย | MCC + Timestamp | A | Existing | - | S |
| `late_night_diner` | dining หลัง 22:00 ≥ 4 ครั้ง/เดือน | MCC + Timestamp | A | Existing | - | S |
| `bakery_lover` | ร้านเบเกอรี่บ่อย | Merchant: Yamazaki, BreadTalk | A | Overlap | Baked Pastry, Bakery (Savoury) | S |
| `budget_eater` | avg ticket dining < P25 | MCC + Amount | A | Existing | - | S |
| `solo_diner` | avg ticket ต่ำ + merchant ไม่ซ้ำ | Amount pattern | A | Existing | - | S |
| `street_food_lover` | ticket < 150 บาท ร้านขนาดเล็ก | Amount | A | Existing | - | S |
| `dessert_lover` | ร้านขนม/ไอศกรีม ≥ 6 ครั้ง/เดือน | Merchant: After You, Swensen's | A | Overlap | Dessert, Cakes, Donuts, Ice Cream/Bingsu | S |
| `group_diner` | avg ticket > 2x solo avg สม่ำเสมอ | Amount pattern | A | Existing | - | S |
| `work_lunch_regular` | dining weekday 11:00–14:00 ≥ 15 ครั้ง/เดือน | MCC + Timestamp | A | Existing | - | S |
| `coffee_loyalist` | ≥ 80% coffee txn ที่ร้านเดิม | Merchant concentration | A | Existing | - | S |
| `weekend_foodie` | dining spend Sat-Sun > 60% ของ dining ทั้งหมด | Timestamp | A | Existing | - | S |
| `japanese_food_lover` | ≥ 50% dining ที่ร้านญี่ปุ่น | cuisine = Japanese | B | Overlap | Japan, Sushi, Tonkatsu/Tempura | S |
| `korean_food_lover` | ≥ 50% dining ที่ร้านเกาหลี | cuisine = Korean | B | Overlap | Korea | S |
| `chinese_food_lover` | ≥ 50% dining ที่ร้านจีน | cuisine = Chinese | B | Overlap | China, Dimsum | S |
| `thai_food_loyalist` | ≥ 60% dining ที่ร้านไทย | cuisine = Thai | B | Overlap | Thai | S |
| `western_food_lover` | ≥ 50% dining ที่ร้านตะวันตก | cuisine = Western | B | Overlap | Other_Western | S |
| `italian_food_lover` | ≥ 50% dining ที่ร้านอิตาเลียน | cuisine = Italian | B | Overlap | Italy, Pasta | S |
| `seafood_lover` | ร้านอาหารทะเลบ่อย | cuisine = Seafood | B | Overlap | Seafood | S |
| `vegetarian_friendly` | ร้าน vegetarian / plant-based | diet = Vegetarian | B | Existing | - | S |
| `food_court_regular` | food court ในห้างบ่อย | venue_type = Food Court | B | Overlap | Food Court | S |
| `buffet_lover` | บุฟเฟ่ต์ ≥ 2 ครั้ง/เดือน | venue_type = Buffet | B | Overlap | Buffet | S |
| `family_restaurant_goer` | ร้าน family-friendly บ่อย | segment = Family | B | Overlap | Family/Kids | S |
| `healthy_eater` | ร้าน healthy food / salad | diet = Healthy | B | Overlap | Salad | S |
| `halal_restaurant_goer` | ร้านอาหาร halal certified บ่อย | cuisine_tag = Halal | B | Existing | - | S |
| `omakase_enthusiast` | omakase / chef's table ≥ 2 ครั้ง/ปี + high ticket | venue_type = Omakase | B | Existing | - | V |
| `rooftop_bar_goer` | rooftop bar / sky lounge บ่อย | venue_type = Rooftop | B | Existing | - | V |
| `plant_based_explorer` | สั่ง plant-based / vegan บ่อยขึ้น | diet = Vegan + Recency | B | Existing | - | M |
| `bbq_lover` | ร้าน BBQ ≥ 2 ครั้ง/เดือน | cuisine = BBQ | B | New | BBQ | S |
| `hot_pot_lover` | hot pot ≥ 2 ครั้ง/เดือน | cuisine = Hot Pot | B | New | Hot Pot | S |
| `noodle_lover` | ร้านก๋วยเตี๋ยว/noodle บ่อย ≥ 6 ครั้ง/เดือน | cuisine = Noodles | B | New | Noodles | S |
| `steak_lover` | steakhouse ≥ 2 ครั้ง/เดือน | cuisine = Steak | B | New | Steak | S |
| `french_food_lover` | ≥ 50% fine dining ที่ร้านฝรั่งเศส | cuisine = French | B | New | France | S |
| `american_food_lover` | burger/steak/American chain dominant | cuisine = American | B | New | US | S |
| `vietnamese_food_lover` | ร้านเวียดนามบ่อย ≥ 4 ครั้ง/เดือน | cuisine = Vietnamese | B | New | Vietnam | S |
| `thai_isan_lover` | ร้านอาหารอีสาน/ส้มตำบ่อย | cuisine = Thai_Isan | B | New | Thai_Isan, Somtum | S |
| `thai_northern_lover` | ร้านอาหารเหนือบ่อย | cuisine = Thai_Northern | B | New | Thai_Northern | S |
| `thai_southern_lover` | ร้านอาหารใต้บ่อย | cuisine = Thai_Southern | B | New | Thai_Southern | S |
| `alcohol_buyer` | bar/pub/liquor shop ≥ 3 ครั้ง/เดือน | merchant_type = Bar/Alcohol | B | New | Alcohol | S |
| `tea_house_regular` | tea house (ไม่ใช่ bubble tea) ≥ 4 ครั้ง/เดือน | venue_type = Tea House | B | New | Tea | S |
| `juice_bar_regular` | juice bar / health drink shop ≥ 4 ครั้ง/เดือน | venue_type = Juice Bar | B | New | Juice | S |
| `drinks_shop_regular` | standalone drink shop (non-cafe) ≥ 6 ครั้ง/เดือน | venue_type = Drinks Shop | B | New | Drinks | S |

---

### ✈️ Travel & Hotel
> v1: 18 | v2: +7 | รวม: 25 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `frequent_traveler` | airline + hotel ≥ 4 ครั้ง/ปี | MCC: Airlines + Hotel | A | Overlap | Travel | S |
| `international_traveler` | foreign currency ≥ 2 ครั้ง/ปี | Currency ≠ THB | A | Existing | - | V |
| `domestic_traveler` | airline/hotel ในประเทศ ไม่มี foreign | MCC + Currency | A | Existing | - | V |
| `budget_traveler` | LCC airline + hotel avg ต่ำ | Merchant: AirAsia + Amount | A | Existing | - | S |
| `luxury_traveler` | full-service airline + hotel > P75 | Merchant: TG, SQ + Amount | A | Overlap | Luxury | S |
| `business_traveler` | บินจันทร์-ศุกร์ + hotel weekday | Timestamp + MCC | A | Existing | - | S |
| `leisure_traveler` | airline/hotel ช่วง weekend/วันหยุด | Timestamp + MCC | A | Existing | - | V |
| `hotel_loyalist` | ≥ 70% hotel txn ที่ chain เดียว | Merchant concentration | A | Existing | - | S |
| `airbnb_user` | Airbnb ≥ 1 ครั้ง/ปี | Merchant: Airbnb | A | Existing | - | V |
| `frequent_flyer` | airline ≥ 6 ครั้ง/ปี | MCC: Airlines | A | Existing | - | S |
| `backpacker_style` | ท่องเที่ยวบ่อย + avg spend ต่ำ | Frequency + Low amount | A | Existing | - | S |
| `last_minute_booker` | booking < 7 วันก่อนเดินทาง | Date pattern | A | Existing | - | S |
| `early_planner` | booking > 30 วันล่วงหน้า | Date pattern | A | Existing | - | S |
| `staycation_lover` | hotel txn ในประเทศ ไม่มี airline ร่วม | Hotel + No airline | A | Existing | - | V |
| `duty_free_shopper` | duty free txn ≥ 2 ครั้ง/ปี | MCC: Duty Free | A | Existing | - | V |
| `long_stay_traveler` | hotel txn ≥ 5 คืนต่อ trip | Amount + duration proxy | A | Existing | - | V |
| `solo_traveler` | airline + hotel single avg | Amount proxy | A | Existing | - | S |
| `asia_traveler` | foreign txn ส่วนใหญ่ใน Asia | merchant_country = Asia | B | Existing | - | V |
| `europe_traveler` | foreign txn ที่ Europe | merchant_country = Europe | B | Existing | - | V |
| `resort_lover` | hotel txn ที่ resort | hotel_type = Resort | B | Existing | - | V |
| `city_traveler` | hotel txn ที่ city hotel | hotel_type = City | B | Existing | - | V |
| `japan_traveler` | foreign txn ที่ Japan บ่อย | merchant_country = Japan | B | Existing | - | V |
| `luxury_resort_seeker` | resort + avg > P90 | hotel_type = Resort + Amount | B | Existing | - | V |
| `cruise_passenger` | cruise line txn ≥ 1 ครั้ง/ปี | merchant_type = Cruise | B | Existing | - | V |
| `workcation_traveler` | hotel weekday ≥ 5 คืน + non-business pattern | Duration + non-Mon pattern | B | Existing | - | V |

---

### 🛍️ Shopping
> v1: 22 | v2: +10 | v2.1: +2 | รวม: 34 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `online_first_shopper` | ≥ 50% txn เป็น online | Channel | A | Existing | - | S |
| `luxury_shopper` | avg ticket > P90 หรือ luxury merchant | Merchant + Amount | A | Overlap | Luxury, Social Status | S |
| `fashion_lover` | apparel ≥ 4 ครั้ง/เดือน | MCC: Apparel | A | Overlap | Fashion, Clothing/Apparel | S |
| `sneaker_enthusiast` | ร้านรองเท้า/sneaker บ่อย | Merchant: Nike, Adidas | A | Overlap | Shoes/footwear | S |
| `beauty_conscious` | ร้านเครื่องสำอาง ≥ 3 ครั้ง/เดือน | MCC: Beauty | A | Overlap | Beauty/Feminine | S |
| `tech_gadget_buyer` | electronics ≥ 2 ครั้ง/ไตรมาส | MCC: Electronics | A | Existing | - | V |
| `home_decor_lover` | furniture/home goods บ่อย | Merchant: IKEA, HomePro | A | Overlap | Furniture & Home Decor | V |
| `book_lover` | bookstore ≥ 1 ครั้ง/เดือน | Merchant: Se-Ed, B2S | A | Existing | - | S |
| `sports_gear_buyer` | ร้านอุปกรณ์กีฬา ≥ 2 ครั้ง/ไตรมาส | MCC: Sporting Goods | A | Overlap | Sport & activewear | V |
| `grocery_regular` | supermarket ≥ 3 ครั้ง/เดือน | Merchant: Tops, BigC | A | Existing | - | S |
| `convenience_store_addict` | convenience store ≥ 15 ครั้ง/เดือน | Merchant: 7-Eleven | A | Overlap | Convenient Seekers, Fast Consumer/Convenience | S |
| `department_store_loyal` | ≥ 70% dept txn ที่ chain เดิม | Merchant concentration | A | Existing | - | S |
| `marketplace_shopper` | Shopee/Lazada ≥ 4 ครั้ง/เดือน | Merchant: Shopee, Lazada | A | Overlap | E-Commerce | S |
| `subscription_stacker` | recurring txn ≥ 3 บริการ/เดือน | Recurring pattern | A | Overlap | Subscription | S |
| `impulse_buyer` | txn สูง หลาย merchant pattern ไม่ consistent | Diversity + Variance | A | Existing | - | S |
| `brand_switcher` | merchant loyalty ต่ำ ชอบลองใหม่ | Low concentration | A | Existing | - | S |
| `secondhand_buyer` | platform secondhand | Merchant: Carousell | A | Existing | - | V |
| `seasonal_shopper` | spike ช่วง 11.11, 12.12, Songkran | Timestamp + Amount spike | A | Existing | - | V |
| `premium_brand_loyal` | repeat premium brand > 3 ครั้ง/ไตรมาส | Merchant + Amount | A | Overlap | Social Status | S |
| `hypermarket_shopper` | Makro/Lotus's ≥ 2 ครั้ง/เดือน + large basket | Merchant + High amount | A | Existing | - | S |
| `jewelry_buyer` | jewelry store txn ≥ 2 ครั้ง/ปี | MCC: Jewelry | A | Existing | - | V |
| `gold_accumulator` | gold shop txn recurring + consistent amount | Merchant: YLG, Aurora | A | Existing | - | S |
| `stationery_regular` | stationery store ≥ 1 ครั้ง/เดือน | MCC: Stationery | A | Existing | - | S |
| `home_office_buyer` | stationery + electronics combo ≥ 4 ครั้ง/ปี | MCC combo | A | Existing | - | V |
| `fast_fashion_buyer` | fashion MCC + low avg ticket + high frequency | MCC + Amount + Frequency | A | Existing | - | S |
| `accessories_collector` | jewelry + fashion accessory บ่อย | MCC: Jewelry + Apparel | A | Overlap | Handbags & accessories | S |
| `flash_sale_hunter` | e-commerce spike ช่วง 11.11, 12.12 > 3x avg | Timestamp + Amount | A | Existing | - | V |
| `cross_border_shopper` | foreign e-commerce ≥ 4 ครั้ง/ปี | Merchant: Amazon, ASOS | A | Existing | - | V |
| `mall_shopper` | ≥ 60% retail txn ที่ merchant ในห้าง | merchant_location = Mall | B | Existing | - | S |
| `bargain_hunter` | outlet/discount store บ่อย | venue_type = Outlet | B | Overlap | Value Economy | S |
| `gifting_regular` | gift shop ช่วงเทศกาลสม่ำเสมอ | merchant_type = Gift | B | Existing | - | V |
| `luxury_gifter` | jewelry + dept store spike ช่วง Valentine/Mother's Day | MCC combo + Timestamp | B | Existing | - | V |
| `eco_conscious_shopper` | sustainable/organic/eco brand บ่อย | merchant_type = Eco/Sustainable | B | New | Minimal/Sustainable | S |
| `travel_bag_enthusiast` | luggage/travel bag ≥ 2 ครั้ง/ปี + travel combo | MCC: Luggage + Travel | B | New | Travel & lifestyle bags | V |

---

### 🎭 Entertainment & Lifestyle
> v1: 18 | v2: +7 | v2.1: +3 | รวม: 28 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `movie_lover` | cinema ≥ 2 ครั้ง/เดือน | Merchant: SF, Major | A | Overlap | Entertainment | S |
| `concert_goer` | ticketing ≥ 3 ครั้ง/ปี | Merchant: Eventpop | A | Overlap | Entertainment | V |
| `gym_member` | fitness center recurring ≥ 6 เดือน | Merchant: Fitness First | A | Existing | - | S |
| `gamer` | gaming platform บ่อย | Merchant: Steam, PS Store | A | Existing | - | S |
| `night_owl_entertainer` | entertainment หลัง 22:00 บ่อย | MCC + Timestamp | A | Overlap | Nightlife | S |
| `karaoke_regular` | karaoke ≥ 2 ครั้ง/เดือน | Merchant: Tawandang | A | Overlap | Nightlife | S |
| `spa_lover` | spa/massage ≥ 2 ครั้ง/เดือน | MCC: Personal Care | A | Overlap | Spa & Massage | S |
| `music_festival_goer` | festival ticketing ≥ 2 ครั้ง/ปี + high amount | Ticketing + Amount | A | Overlap | Entertainment | V |
| `streaming_subscriber` | ≥ 2 streaming subscriptions | Merchant: Netflix, Disney+ | A | Overlap | Subscription | S |
| `outdoor_adventurer` | outdoor gear + travel combo | Merchant: Decathlon + MCC | A | Overlap | Adventure | S |
| `theme_park_visitor` | theme park ≥ 1 ครั้ง/ปี | Merchant: Universal | A | Overlap | Entertainment | V |
| `nail_salon_regular` | nail salon ≥ 2 ครั้ง/เดือน | MCC: Beauty + Merchant | A | Overlap | Nail | S |
| `hair_salon_loyal` | ≥ 70% hair txn ที่ร้านเดิม + monthly | Merchant concentration | A | Overlap | Hair | S |
| `sport_event_goer` | stadium/sport event ≥ 3 ครั้ง/ปี | MCC: Ticket + Stadium | A | Existing | - | V |
| `esports_fan` | esports event ticketing + gaming spend combo | Merchant: RoV, PUBG event | A | Existing | - | V |
| `pet_friendly_lifestyle` | pet + travel + dining combo | MCC combo | A | Existing | - | S |
| `sports_fan` | stadium/sport event ≥ 2 ครั้ง/ปี | venue_type = Stadium | B | Existing | - | V |
| `yoga_practitioner` | yoga studio ≥ 2 ครั้ง/เดือน | activity_type = Yoga | B | Existing | - | S |
| `golf_player` | golf course ≥ 1 ครั้ง/เดือน | activity_type = Golf | B | Existing | - | S |
| `art_culture_enthusiast` | museum/gallery/art event | venue_type = Cultural | B | Existing | - | V |
| `escape_room_fan` | escape room ≥ 2 ครั้ง/ไตรมาส | venue_type = Escape Room | B | Existing | - | V |
| `board_game_cafe_goer` | board game cafe บ่อย | venue_type = Board Game | B | Existing | - | S |
| `bowling_regular` | bowling ≥ 1 ครั้ง/เดือน | venue_type = Bowling | B | Existing | - | S |
| `pilates_devotee` | pilates studio ≥ 3 ครั้ง/เดือน | activity_type = Pilates | B | Existing | - | S |
| `muay_thai_trainee` | muay thai gym txn recurring | activity_type = Muay Thai | B | Existing | - | S |
| `brow_treatment_regular` | brow specialist ≥ 1 ครั้ง/เดือน | venue_type = Brow Studio | B | New | Brow | S |
| `lash_extension_regular` | lash studio ≥ 1 ครั้ง/เดือน | venue_type = Lash Studio | B | New | Lash | S |
| `waxing_regular` | wax studio ≥ 1 ครั้ง/เดือน | venue_type = Wax Studio | B | New | Wax | S |

---

### 🚗 Transport & Commute
> v1: 10 | v2: +6 | รวม: 16 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `daily_commuter` | fuel/transit weekday ≥ 20 วัน/เดือน | MCC + Timestamp | A | Existing | - | S |
| `car_owner` | fuel + parking + auto service ครบ | MCC combo | A | Overlap | Car owners | S |
| `grab_dependent` | Grab ≥ 15 ครั้ง/เดือน | Merchant: Grab | A | Existing | - | S |
| `taxi_user` | taxi บ่อย + Grab น้อย | MCC: Taxi | A | Existing | - | S |
| `fuel_brand_loyal` | ≥ 70% fuel ที่ปั๊มแบรนด์เดียว | Merchant concentration | A | Existing | - | S |
| `ev_driver` | EV charging station | Merchant: EA Anywhere | A | Existing | - | S |
| `bts_mrt_user` | BTS/MRT บ่อย | Merchant: Rabbit, MRT | A | Existing | - | S |
| `motorbike_user` | fuel < 200 บาท/ครั้ง สม่ำเสมอ | Amount pattern | A | Existing | - | S |
| `parking_heavy` | parking > 15 ครั้ง/เดือน | MCC: Parking | A | Existing | - | S |
| `long_distance_driver` | toll บ่อย / fuel ต่างจังหวัด | MCC: Toll | A | Existing | - | S |
| `car_enthusiast` | auto accessories + car wash + detailing บ่อย | MCC: Auto Accessories | A | Existing | - | S |
| `car_maintenance_regular` | service center + tire + oil ≥ 4 ครั้ง/ปี | MCC: Auto Service | A | Existing | - | S |
| `high_fuel_spender` | fuel spend > P75 ของ portfolio | MCC: Petrol + Amount | A | Existing | - | S |
| `ride_share_switcher` | สลับ Grab / Bolt / InDriver บ่อย | Merchant diversity | A | Existing | - | S |
| `van_pool_user` | minibus/van service txn บ่อย ช่วง commute | MCC: Transportation + Time | A | Existing | - | S |
| `new_car_seeker` | auto showroom txn ≥ 1 ครั้ง | MCC: Automobile + High amount | A | Existing | - | V |

---

### 💊 Health & Wellness
> v1: 12 | v2: +8 | รวม: 20 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `health_conscious` | gym + pharmacy + health food ≥ 2 จาก 3 | MCC combo | A | Overlap | Health | S |
| `pharmacy_regular` | pharmacy ≥ 3 ครั้ง/เดือน | MCC: Drug Store | A | Existing | - | S |
| `hospital_visitor` | hospital ≥ 2 ครั้ง/ไตรมาส | MCC: Hospital | A | Existing | - | V |
| `supplement_buyer` | Watsons/Boots บ่อย | Merchant: Watsons | A | Existing | - | S |
| `organic_food_lover` | organic/health food store | Merchant: Lemon Farm | A | Existing | - | S |
| `dental_care_conscious` | dental clinic ≥ 2 ครั้ง/ปี | MCC: Dental | A | Existing | - | S |
| `fitness_first_user` | Fitness First recurring | Merchant: Fitness First | A | Existing | - | S |
| `eye_care_regular` | optician ≥ 2 ครั้ง/ปี | MCC: Optical | A | Existing | - | S |
| `maternal_care` | OB/GYN + baby products ช่วงเวลาเดียวกัน | MCC combo + Timing | A | Existing | - | M |
| `regular_checkup_goer` | hospital/clinic txn recurring ≥ 1 ครั้ง/ไตรมาส | MCC: Hospital + Recurring | A | Existing | - | S |
| `mental_wellness_seeker` | meditation app + wellness center + spa combo | Merchant: Headspace + MCC | A | Overlap | Wellness and Longevity | S |
| `sports_nutrition_buyer` | protein supplement + sports gear combo | Merchant: Supersports + Nutrition | A | Existing | - | S |
| `aesthetic_spender` | beauty clinic + cosmetics high spend | MCC: Beauty + Amount | A | Overlap | Derma/Aesthetic | S |
| `high_medical_spender` | hospital/clinic spend > P75 | MCC: Hospital + Amount | A | Existing | - | V |
| `weight_management_focused` | gym + low dining spend + supplement combo | MCC combo | A | Existing | - | S |
| `beauty_clinic_visitor` | aesthetic clinic บ่อย | clinic_type = Aesthetic | B | Overlap | Derma/Aesthetic, Treatment | S |
| `mental_health_aware` | therapy/wellness center | clinic_type = Mental Health | B | Existing | - | S |
| `traditional_medicine` | ยาแผนโบราณ / แพทย์แผนจีน | clinic_type = TCM | B | Existing | - | S |
| `specialized_treatment_seeker` | specialist clinic ≥ 4 ครั้ง/ปี (non-GP) | clinic_type = Specialist | B | Existing | - | V |
| `fertility_aware` | fertility clinic / OB txn + baby product combo | clinic_type = Fertility | B | Existing | - | V |

---

### 💳 Financial Behavior
> v1: 14 | v2: +10 | v2.1: +1 | รวม: 25 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `high_spender` | total spend > P75 | Amount | A | Existing | - | S |
| `mid_spender` | total spend P25–P75 | Amount | A | Existing | - | S |
| `low_spender` | total spend < P25 | Amount | A | Existing | - | S |
| `consistent_spender` | CV monthly spend ต่ำ | Variance | A | Existing | - | S |
| `seasonal_spender` | spike > 2x avg ≥ 2 ครั้ง/ปี | Timestamp + Amount | A | Existing | - | V |
| `end_of_month_spender` | ≥ 40% spend วันที่ 25–31 | Timestamp | A | Existing | - | S |
| `paycheck_spender` | spike ต้นเดือน (1–5) | Timestamp + Amount | A | Existing | - | S |
| `installment_user` | installment ≥ 1 ครั้ง/ไตรมาส | Installment flag | A | Existing | - | S |
| `high_utilization` | credit utilization > 70% สม่ำเสมอ | Utilization | A | Existing | - | S |
| `low_utilization` | credit utilization < 20% | Utilization | A | Existing | - | S |
| `multi_card_user` | spend pattern บ่งชี้หลายบัตร | Spend pattern | A | Existing | - | S |
| `cash_advance_user` | cash advance ≥ 1 ครั้ง/ปี | Txn type | A | Existing | - | S |
| `reward_maximizer` | ≥ 50% spend ที่ high-points merchant | Merchant + Reward | A | Existing | - | S |
| `single_category_user` | ≥ 80% spend ใน MCC เดียว | MCC concentration | A | Existing | - | S |
| `investor` | investment platform / บล. txn ≥ 4 ครั้ง/ปี | MCC: Investment | A | Existing | - | S |
| `regular_investor` | investment txn recurring รายเดือน | MCC: Investment + Recurring | A | Existing | - | S |
| `insurance_holder` | insurance premium txn recurring | MCC: Insurance | A | Existing | - | S |
| `multi_insurance_holder` | ≥ 2 insurance products recurring | MCC: Insurance + Diverse | A | Existing | - | S |
| `high_installment_user` | installment txn ≥ 3 active พร้อมกัน | Installment count | A | Existing | - | S |
| `financially_disciplined` | low utilization + no cash advance + consistent | Combined behavioral | A | Existing | - | S |
| `cash_flow_stressed` | high utilization + cash advance + end-of-month heavy | Combined behavioral | A | Existing | - | M |
| `wealth_builder` | investor + insurance + low impulse combo | MCC combo | A | Existing | - | S |
| `big_ticket_buyer` | single txn > P95 ≥ 2 ครั้ง/ปี | Amount spike | A | Existing | - | V |
| `small_business_spender` | telecom + ads + supplies + irregular high amount | MCC combo pattern | A | Overlap | Biz Owner | S |
| `donation_giver` | donation/charity txn ≥ 2 ครั้ง/ปี | MCC: Donation/Charity | A | New | Donation | V |

---

### 👨‍👩‍👧 Life Stage
> v1: 14 | v2: +8 | v2.1: +1 | รวม: 23 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `parent` | baby/kids + family restaurant บ่อย | Merchant + MCC | A | Overlap | Family/Kids | S |
| `new_parent` | spike baby products ใน 12 เดือน | Merchant + Recency | A | Existing | - | M |
| `pet_owner` | pet shop/vet ≥ 1 ครั้ง/เดือน | Merchant: Pet Planet | A | Existing | - | S |
| `homeowner` | home improvement + utility ≥ 1 ครั้ง/ไตรมาส | Merchant: HomePro | A | Overlap | Home Center | S |
| `senior_lifestyle` | pharmacy + hospital + market dominant | MCC combo | A | Existing | - | S |
| `empty_nester` | kids merchant ลดลง + travel/leisure เพิ่ม | Trend | A | Existing | - | M |
| `teen_spender` | gaming + fastfood + convenience dominant | MCC combo | A | Existing | - | S |
| `career_starter` | low spend + professional attire | Amount + MCC | A | Existing | - | S |
| `family_breadwinner` | high spend + diverse category | Amount + Diversity | A | Existing | - | S |
| `retiree_lifestyle` | weekday ≈ weekend ratio + pharmacy heavy | Timestamp + MCC | A | Existing | - | S |
| `multi_pet_owner` | pet txn diverse (vet + grooming + food + toys) | MCC + Merchant diversity | A | Existing | - | S |
| `home_renovator` | high spend HomePro/contractor ≥ 3 ครั้ง/ปี | Merchant: HomePro + Amount | A | Overlap | Home Services, Building Materials Store | V |
| `school_fee_payer` | school/tuition txn recurring รายเทอม | MCC: Education + Recurring | A | Existing | - | S |
| `extracurricular_parent` | music school + art class + sports academy txn | MCC: Education + Kids | A | Existing | - | S |
| `sandwich_generation` | ทั้ง kids txn และ senior care txn พร้อมกัน | MCC combo | A | Existing | - | S |
| `newly_married` | jewelry + wedding vendor + honeymoon travel combo | MCC combo + Timeline | A | Existing | - | M |
| `student` | ใกล้มหาวิทยาลัย + stationery + low spend | merchant_location = Uni | B | Existing | - | S |
| `young_professional` | coffee weekday เช้า + lunch ใกล้ office | merchant_location = Office | B | Overlap | Professional | S |
| `college_age` | ใกล้มหาวิทยาลัย + delivery + low ticket | merchant_location = Uni | B | Existing | - | S |
| `digital_nomad` | co-working space + coffee + travel combo | venue_type = Co-working | B | Existing | - | S |
| `expat_lifestyle` | foreign cuisine + international market + foreign transfer | merchant_type = International | B | Existing | - | S |
| `tattoo_enthusiast` | tattoo studio txn ≥ 1 ครั้ง/ปี | venue_type = Tattoo Studio | B | New | Tatto | V |

---

### ⏰ Time Patterns
> v1: 10 | v2: +5 | รวม: 15 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `morning_person` | ≥ 40% txn ก่อน 09:00 | Timestamp | A | Existing | - | S |
| `night_owl_spender` | ≥ 30% txn หลัง 22:00 | Timestamp | A | Existing | - | S |
| `weekend_warrior` | ≥ 60% spend Sat-Sun | Timestamp | A | Existing | - | S |
| `weekday_spender` | ≥ 70% spend Mon-Fri | Timestamp | A | Existing | - | S |
| `lunch_hour_regular` | spike 12:00–14:00 ทุก weekday | Timestamp | A | Existing | - | S |
| `after_work_spender` | spike 18:00–21:00 | Timestamp | A | Existing | - | S |
| `holiday_spender` | spend +50% ช่วงวันหยุดยาว | Timestamp + Amount | A | Existing | - | V |
| `payday_spike` | spike วันที่ 25–5 ต้นเดือน | Timestamp + Amount | A | Existing | - | V |
| `monthly_planner` | spend กระจาย consistent ไม่มี spike | Variance | A | Existing | - | S |
| `off_peak_shopper` | retail 09:00–12:00 วันธรรมดา | Timestamp | A | Existing | - | S |
| `songkran_spender` | spend spike ช่วง Songkran (เม.ย.) ทุกปี | Timestamp + Amount | A | Existing | - | V |
| `year_end_big_spender` | spend spike ธ.ค. > 2x avg ทุกปี | Timestamp + Amount | A | Existing | - | V |
| `ramadan_aware_spender` | dining pattern เปลี่ยนช่วง Ramadan | Timestamp + Dining | A | Existing | - | V |
| `event_day_spender` | spend spike ตรงกับ major event | Timestamp + Amount spike | A | Existing | - | V |
| `early_bird_shopper` | ≥ 40% retail txn ก่อน 10:00 | Timestamp | A | Existing | - | S |

---

### 📱 Digital Behavior
> v1: 8 | v2: +7 | รวม: 15 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `online_native` | ≥ 70% txn เป็น online | Channel | A | Existing | - | S |
| `contactless_payer` | ≥ 80% in-store เป็น tap/NFC | Payment method | A | Existing | - | S |
| `app_heavy_user` | ≥ 50% txn ผ่าน mobile app | Channel | A | Existing | - | S |
| `digital_subscription_heavy` | ≥ 4 recurring digital/เดือน | Recurring + Digital | A | Existing | - | S |
| `streaming_only` | streaming ≥ 2 + cinema = 0 | Merchant pattern | A | Existing | - | S |
| `social_commerce_buyer` | TikTok Shop txn ≥ 4 ครั้ง | Merchant: TikTok Shop | A | Existing | - | S |
| `crypto_curious` | crypto exchange ≥ 1 ครั้ง | Merchant: Bitkub | A | Existing | - | V |
| `fintech_user` | fintech platform บ่อย | Merchant: TrueMoney | A | Existing | - | S |
| `high_telecom_spender` | telecom spend > P75 | MCC: Telecom + Amount | A | Existing | - | S |
| `device_upgrader` | new device txn ≥ 1/ปี + high telecom | MCC: Electronics + Telecom | A | Existing | - | V |
| `saas_subscriber` | software/SaaS recurring ≥ 3 | Merchant: Adobe, Notion | A | Existing | - | S |
| `ai_tool_user` | AI platform txn (ChatGPT Plus, Midjourney) | Merchant: OpenAI | A | Existing | - | S |
| `cashless_convert` | contactless + online combo > 90% | Payment + Channel | A | Existing | - | S |
| `social_ads_spender` | Facebook/Google/TikTok Ads txn ≥ 4 ครั้ง/ปี | Merchant: Meta, Google Ads | A | Existing | - | S |
| `e_wallet_heavy` | e-wallet > 30% ของ txn | Merchant: E-wallet | A | Existing | - | S |

---

## หมวดใหม่ที่ยังไม่มีใน v1

---

### 🎓 Education & Learning

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `lifelong_learner` | online course platform ≥ 4 ครั้ง/ปี | Merchant: Coursera, Udemy | A | Overlap | Skill Development & Training | S |
| `language_learner` | language school/app txn recurring | Merchant: British Council | A | Existing | - | S |
| `professional_upskiller` | certification / professional course ≥ 2 ครั้ง/ปี | MCC: Education + Amount | A | Overlap | Skill Development & Training | S |
| `tutor_seeker` | tutoring center txn recurring รายเดือน | MCC: Education + Recurring | A | Existing | - | S |
| `school_supply_buyer` | stationery + kids spike ต้นปีการศึกษา | MCC combo + Timestamp | A | Existing | - | V |
| `university_student` | student merchant + dining + convenience + low spend | MCC combo + Amount | A | Existing | - | S |
| `education_investor` | high education spend > P75 across family | MCC: Education + Amount | A | Existing | - | S |
| `stem_enthusiast` | electronics + coding subscription + stationery combo | MCC combo | A | Existing | - | S |
| `arts_student` | art supplies + music instrument + performance txn | MCC: Stationery + Entertainment | A | Existing | - | S |

---

### 🏠 Real Estate & Housing

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `utility_payer` | utility txn recurring รายเดือน | MCC: Utility + Recurring | A | Existing | - | S |
| `high_utility_user` | utility spend > P75 | MCC: Utility + Amount | A | Existing | - | S |
| `condo_resident` | utility + condo management fee recurring | MCC: Utility + Pattern | A | Existing | - | S |
| `home_appliance_buyer` | white goods ≥ 1 ครั้ง/ปี + high amount | MCC: Electronics/Household | A | Existing | - | V |
| `diy_homeowner` | hardware store + home improvement บ่อย | Merchant: Global House | A | Overlap | Building Materials Store, Home Center | V |
| `property_market_watcher` | real estate agent txn / property expo ≥ 1 ครั้ง/ปี | MCC: Real Estate | A | Existing | - | V |
| `rental_income_owner` | irregular large incoming + utility multi-unit | Amount + Utility pattern | A | Existing | - | V |

---

### 📊 Investment & Financial Planning

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `stock_market_participant` | brokerage txn ≥ 4 ครั้ง/ปี | Merchant: Settrade, Jitta | A | Existing | - | S |
| `mutual_fund_investor` | fund platform txn recurring | Merchant: FINNOMENA | A | Existing | - | S |
| `gold_investor` | gold shop / gold ETF txn ≥ 4 ครั้ง/ปี | Merchant: YLG, MTS Gold | A | Existing | - | S |
| `real_estate_investor` | real estate agent + property expo + large amount | MCC: Real Estate + Amount | A | Existing | - | V |
| `passive_income_seeker` | investment + insurance + low consumption | MCC combo | A | Existing | - | S |
| `financial_planner_client` | insurance + investment + consistent saving | MCC combo | A | Existing | - | S |

---

### 💳 Payment Behavior *(มิติใหม่ — v2.2)*
> ข้อมูลจาก payment record ของ CC issuer — Path A ทั้งหมด ไม่ต้องรอ enrichment

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `full_payer` | จ่ายยอดเต็ม ≥ 10 จาก 12 เดือนล่าสุด | Payment record vs statement | A | New | - | S |
| `minimum_payer` | จ่ายขั้นต่ำเท่านั้น ≥ 6 เดือน | Payment amount = min due | A | New | - | S |
| `revolving_user` | carry balance ข้ามเดือน ≥ 3 เดือนติด | Outstanding balance > 0 | A | New | - | M |
| `partial_payer` | จ่าย > min แต่ < full สม่ำเสมอ ≥ 6 เดือน | Payment amount pattern | A | New | - | S |
| `early_payer` | จ่ายก่อน due date > 5 วัน สม่ำเสมอ ≥ 8 เดือน | Payment date delta | A | New | - | S |
| `late_payer_history` | จ่ายหลัง due date ≥ 2 ครั้งใน 12 เดือน | Payment date delta | A | New | - | M |
| `autopay_enrolled` | ตั้ง autopay (full หรือ minimum) | System flag | A | New | - | S |
| `payment_irregular` | วันจ่ายและ amount แปรผันสูง — ไม่มี pattern | Payment date + amount variance | A | New | - | M |

---

### 🃏 Card Relationship *(มิติใหม่ — v2.2)*
> วัด "ความสัมพันธ์" ของลูกค้ากับบัตรใบนี้โดยเฉพาะ — ต่างจาก spending behavior

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `primary_card_signal` | spend > P75 + ≥ 8 MCC category/เดือน สม่ำเสมอ | Spend breadth + amount | A | New | - | S |
| `secondary_card_signal` | spend < P25 + ≤ 2 MCC category + sporadic | Low breadth + low frequency | A | New | - | S |
| `limit_approacher` | utilization 80–95% ≥ 4 เดือน (ไม่ถึง limit แต่ใกล้) | Utilization pattern | A | New | - | M |
| `benefit_chaser` | spend spike ช่วง point multiplier / campaign period ≥ 3 ครั้ง/ปี | Spend timing vs campaign calendar | A | New | - | V |
| `card_renewal_spiker` | spend เพิ่ม > 30% ช่วง 1 เดือนก่อน anniversary | Spend trend + card age | A | New | - | V |
| `installment_converter` | ≥ 40% ของ large txn (> P75) แปลงเป็น installment | Installment conversion rate | A | New | - | S |

---

### 📈 Spending Momentum *(มิติใหม่ — v2.2)*
> ภาพรวม spend ของลูกค้า กำลังขึ้น ลง หรือ stable — ต่างจาก per-category trending

| Tag | Definition | Signal | Path | Source | Enrichment Tag | Stability |
|-----|-----------|--------|------|--------|----------------|---|
| `accelerating_spender` | total monthly spend เพิ่ม ≥ 15% ต่อเนื่อง 3 เดือน | Month-over-month spend delta | A | New | - | M |
| `decelerating_spender` | total monthly spend ลด ≥ 15% ต่อเนื่อง 3 เดือน | Month-over-month spend delta | A | New | - | M |
| `stable_spender` | CV of monthly spend < 0.15 ≥ 6 เดือน | Spend coefficient of variation | A | New | - | S |
| `recovering_spender` | inactive ≥ 2 เดือน แล้วกลับมา active ≥ 2 เดือนติด | Spend gap + recovery pattern | A | New | - | M |
| `boom_bust_spender` | สลับ high/low month ≥ 4 รอบ/ปี (oscillation pattern) | Spend alternation pattern | A | New | - | M |

---

## สรุป Tags ทั้งหมด

| หมวด | Existing | Overlap | New | รวม |
|------|---------|---------|-----|-----|
| Food & Dining | 17 | 16 | 14 | 47 |
| Travel & Hotel | 23 | 2 | 0 | 25 |
| Shopping | 19 | 13 | 2 | 34 |
| Entertainment & Lifestyle | 13 | 12 | 3 | 28 |
| Transport & Commute | 15 | 1 | 0 | 16 |
| Health & Wellness | 15 | 5 | 0 | 20 |
| Financial Behavior | 23 | 1 | 1 | 25 |
| Life Stage | 14 | 4 | 1 | 23 |
| Time Patterns | 15 | 0 | 0 | 15 |
| Digital Behavior | 15 | 0 | 0 | 15 |
| Education & Learning | 7 | 2 | 0 | 9 |
| Real Estate & Housing | 5 | 2 | 0 | 7 |
| Investment & Financial Planning | 6 | 0 | 0 | 6 |
| **Payment Behavior** *(v2.2)* | 0 | 0 | **8** | **8** |
| **Card Relationship** *(v2.2)* | 0 | 0 | **6** | **6** |
| **Spending Momentum** *(v2.2)* | 0 | 0 | **5** | **5** |
| **รวม** | **187** | **58** | **40** | **342** |

### Enrichment Tag Coverage Summary
จาก 99 enrichment tags ของทีม:
- **58 tags → Overlap** กับ customer tag ที่มีอยู่แล้ว → implement ได้ทันทีหลัง enrichment พร้อม
- **21 tags → New** เพิ่มเข้า library
- **~20 tags** → Merchant classification tier ใช้เป็น enrichment attribute (ไม่ใช่ customer tag โดยตรง)

---

### Path Distribution

| Path | Count |
|------|-------|
| **A** — ไม่ต้องรอ Enrichment | 254 |
| **B** — รอ Enrichment (direct map) | 69 |
| **รวม** | **323** |

---

*v2.2 — Thena × Tee | 2026-04-27 | 342 tags | 58 overlap กับ enrichment tags ของทีม | +19 tags: Payment Behavior, Card Relationship, Spending Momentum*
