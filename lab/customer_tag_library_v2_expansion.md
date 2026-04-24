# Customer Tag Library — Version 2.1
**Version**: 2.1 | **Updated**: 2026-04-18
**v1**: 151 | **v2**: +152 | **v2.1 (enrichment)**: +20 | **Total**: 323 tags

> `[A]` = ไม่ต้องรอ Enrichment | `[B]` = ต้องรอ Enrichment (direct mapping)
>
> **Source**: `Existing` = มีอยู่แล้ว (ไม่มี enrichment tag ตรงๆ) | `Overlap` = มีอยู่แล้ว + ตรงกับ enrichment tag ของทีม | `New` = เพิ่มใหม่จาก enrichment review
> **Enrichment Tag**: ชื่อ tag จากลิสต์ทีม 99 อัน ที่ตรงกับ customer tag นี้ (`-` = ไม่มี)

---

## หมวดที่ขยายจาก v1

---

### 🍽️ Food & Dining
> v1: 25 | v2: +8 | v2.1: +14 | รวม: 47 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `frequent_diner` | กินข้าวนอกบ้าน ≥ 10 txn/เดือน | MCC: Dining | A | Overlap | Food |
| `fast_food_regular` | fast food ≥ 4 ครั้ง/เดือน | Merchant: McDonald's, KFC | A | Overlap | QSR, Burgers/Sandwiches, Fried Chicken, Other Fastfood |
| `fine_dining_enthusiast` | avg ticket > P75 | MCC + Amount | A | Overlap | Fine Dine |
| `cafe_hopper` | ร้านกาแฟ ≥ 6 ครั้ง/เดือน หลาย merchant | MCC: Coffee | A | Overlap | Cafe/Bistro, Coffee |
| `bubble_tea_addict` | ชานมไข่มุก ≥ 8 ครั้ง/เดือน | Merchant: Gong Cha, ChaTraMue | A | Existing | - |
| `delivery_dependent` | ≥ 50% dining ผ่าน delivery app | Merchant: GrabFood, LINE MAN | A | Existing | - |
| `brunch_person` | dining Sat-Sun 09:00–13:00 บ่อย | MCC + Timestamp | A | Existing | - |
| `late_night_diner` | dining หลัง 22:00 ≥ 4 ครั้ง/เดือน | MCC + Timestamp | A | Existing | - |
| `bakery_lover` | ร้านเบเกอรี่บ่อย | Merchant: Yamazaki, BreadTalk | A | Overlap | Baked Pastry, Bakery (Savoury) |
| `budget_eater` | avg ticket dining < P25 | MCC + Amount | A | Existing | - |
| `solo_diner` | avg ticket ต่ำ + merchant ไม่ซ้ำ | Amount pattern | A | Existing | - |
| `street_food_lover` | ticket < 150 บาท ร้านขนาดเล็ก | Amount | A | Existing | - |
| `dessert_lover` | ร้านขนม/ไอศกรีม ≥ 6 ครั้ง/เดือน | Merchant: After You, Swensen's | A | Overlap | Dessert, Cakes, Donuts, Ice Cream/Bingsu |
| `group_diner` | avg ticket > 2x solo avg สม่ำเสมอ | Amount pattern | A | Existing | - |
| `work_lunch_regular` | dining weekday 11:00–14:00 ≥ 15 ครั้ง/เดือน | MCC + Timestamp | A | Existing | - |
| `coffee_loyalist` | ≥ 80% coffee txn ที่ร้านเดิม | Merchant concentration | A | Existing | - |
| `weekend_foodie` | dining spend Sat-Sun > 60% ของ dining ทั้งหมด | Timestamp | A | Existing | - |
| `japanese_food_lover` | ≥ 50% dining ที่ร้านญี่ปุ่น | cuisine = Japanese | B | Overlap | Japan, Sushi, Tonkatsu/Tempura |
| `korean_food_lover` | ≥ 50% dining ที่ร้านเกาหลี | cuisine = Korean | B | Overlap | Korea |
| `chinese_food_lover` | ≥ 50% dining ที่ร้านจีน | cuisine = Chinese | B | Overlap | China, Dimsum |
| `thai_food_loyalist` | ≥ 60% dining ที่ร้านไทย | cuisine = Thai | B | Overlap | Thai |
| `western_food_lover` | ≥ 50% dining ที่ร้านตะวันตก | cuisine = Western | B | Overlap | Other_Western |
| `italian_food_lover` | ≥ 50% dining ที่ร้านอิตาเลียน | cuisine = Italian | B | Overlap | Italy, Pasta |
| `seafood_lover` | ร้านอาหารทะเลบ่อย | cuisine = Seafood | B | Overlap | Seafood |
| `vegetarian_friendly` | ร้าน vegetarian / plant-based | diet = Vegetarian | B | Existing | - |
| `food_court_regular` | food court ในห้างบ่อย | venue_type = Food Court | B | Overlap | Food Court |
| `buffet_lover` | บุฟเฟ่ต์ ≥ 2 ครั้ง/เดือน | venue_type = Buffet | B | Overlap | Buffet |
| `family_restaurant_goer` | ร้าน family-friendly บ่อย | segment = Family | B | Overlap | Family/Kids |
| `healthy_eater` | ร้าน healthy food / salad | diet = Healthy | B | Overlap | Salad |
| `halal_restaurant_goer` | ร้านอาหาร halal certified บ่อย | cuisine_tag = Halal | B | Existing | - |
| `omakase_enthusiast` | omakase / chef's table ≥ 2 ครั้ง/ปี + high ticket | venue_type = Omakase | B | Existing | - |
| `rooftop_bar_goer` | rooftop bar / sky lounge บ่อย | venue_type = Rooftop | B | Existing | - |
| `plant_based_explorer` | สั่ง plant-based / vegan บ่อยขึ้น | diet = Vegan + Recency | B | Existing | - |
| `bbq_lover` | ร้าน BBQ ≥ 2 ครั้ง/เดือน | cuisine = BBQ | B | New | BBQ |
| `hot_pot_lover` | hot pot ≥ 2 ครั้ง/เดือน | cuisine = Hot Pot | B | New | Hot Pot |
| `noodle_lover` | ร้านก๋วยเตี๋ยว/noodle บ่อย ≥ 6 ครั้ง/เดือน | cuisine = Noodles | B | New | Noodles |
| `steak_lover` | steakhouse ≥ 2 ครั้ง/เดือน | cuisine = Steak | B | New | Steak |
| `french_food_lover` | ≥ 50% fine dining ที่ร้านฝรั่งเศส | cuisine = French | B | New | France |
| `american_food_lover` | burger/steak/American chain dominant | cuisine = American | B | New | US |
| `vietnamese_food_lover` | ร้านเวียดนามบ่อย ≥ 4 ครั้ง/เดือน | cuisine = Vietnamese | B | New | Vietnam |
| `thai_isan_lover` | ร้านอาหารอีสาน/ส้มตำบ่อย | cuisine = Thai_Isan | B | New | Thai_Isan, Somtum |
| `thai_northern_lover` | ร้านอาหารเหนือบ่อย | cuisine = Thai_Northern | B | New | Thai_Northern |
| `thai_southern_lover` | ร้านอาหารใต้บ่อย | cuisine = Thai_Southern | B | New | Thai_Southern |
| `alcohol_buyer` | bar/pub/liquor shop ≥ 3 ครั้ง/เดือน | merchant_type = Bar/Alcohol | B | New | Alcohol |
| `tea_house_regular` | tea house (ไม่ใช่ bubble tea) ≥ 4 ครั้ง/เดือน | venue_type = Tea House | B | New | Tea |
| `juice_bar_regular` | juice bar / health drink shop ≥ 4 ครั้ง/เดือน | venue_type = Juice Bar | B | New | Juice |
| `drinks_shop_regular` | standalone drink shop (non-cafe) ≥ 6 ครั้ง/เดือน | venue_type = Drinks Shop | B | New | Drinks |

---

### ✈️ Travel & Hotel
> v1: 18 | v2: +7 | รวม: 25 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `frequent_traveler` | airline + hotel ≥ 4 ครั้ง/ปี | MCC: Airlines + Hotel | A | Overlap | Travel |
| `international_traveler` | foreign currency ≥ 2 ครั้ง/ปี | Currency ≠ THB | A | Existing | - |
| `domestic_traveler` | airline/hotel ในประเทศ ไม่มี foreign | MCC + Currency | A | Existing | - |
| `budget_traveler` | LCC airline + hotel avg ต่ำ | Merchant: AirAsia + Amount | A | Existing | - |
| `luxury_traveler` | full-service airline + hotel > P75 | Merchant: TG, SQ + Amount | A | Overlap | Luxury |
| `business_traveler` | บินจันทร์-ศุกร์ + hotel weekday | Timestamp + MCC | A | Existing | - |
| `leisure_traveler` | airline/hotel ช่วง weekend/วันหยุด | Timestamp + MCC | A | Existing | - |
| `hotel_loyalist` | ≥ 70% hotel txn ที่ chain เดียว | Merchant concentration | A | Existing | - |
| `airbnb_user` | Airbnb ≥ 1 ครั้ง/ปี | Merchant: Airbnb | A | Existing | - |
| `frequent_flyer` | airline ≥ 6 ครั้ง/ปี | MCC: Airlines | A | Existing | - |
| `backpacker_style` | ท่องเที่ยวบ่อย + avg spend ต่ำ | Frequency + Low amount | A | Existing | - |
| `last_minute_booker` | booking < 7 วันก่อนเดินทาง | Date pattern | A | Existing | - |
| `early_planner` | booking > 30 วันล่วงหน้า | Date pattern | A | Existing | - |
| `staycation_lover` | hotel txn ในประเทศ ไม่มี airline ร่วม | Hotel + No airline | A | Existing | - |
| `duty_free_shopper` | duty free txn ≥ 2 ครั้ง/ปี | MCC: Duty Free | A | Existing | - |
| `long_stay_traveler` | hotel txn ≥ 5 คืนต่อ trip | Amount + duration proxy | A | Existing | - |
| `solo_traveler` | airline + hotel single avg | Amount proxy | A | Existing | - |
| `asia_traveler` | foreign txn ส่วนใหญ่ใน Asia | merchant_country = Asia | B | Existing | - |
| `europe_traveler` | foreign txn ที่ Europe | merchant_country = Europe | B | Existing | - |
| `resort_lover` | hotel txn ที่ resort | hotel_type = Resort | B | Existing | - |
| `city_traveler` | hotel txn ที่ city hotel | hotel_type = City | B | Existing | - |
| `japan_traveler` | foreign txn ที่ Japan บ่อย | merchant_country = Japan | B | Existing | - |
| `luxury_resort_seeker` | resort + avg > P90 | hotel_type = Resort + Amount | B | Existing | - |
| `cruise_passenger` | cruise line txn ≥ 1 ครั้ง/ปี | merchant_type = Cruise | B | Existing | - |
| `workcation_traveler` | hotel weekday ≥ 5 คืน + non-business pattern | Duration + non-Mon pattern | B | Existing | - |

---

### 🛍️ Shopping
> v1: 22 | v2: +10 | v2.1: +2 | รวม: 34 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `online_first_shopper` | ≥ 50% txn เป็น online | Channel | A | Existing | - |
| `luxury_shopper` | avg ticket > P90 หรือ luxury merchant | Merchant + Amount | A | Overlap | Luxury, Social Status |
| `fashion_lover` | apparel ≥ 4 ครั้ง/เดือน | MCC: Apparel | A | Overlap | Fashion, Clothing/Apparel |
| `sneaker_enthusiast` | ร้านรองเท้า/sneaker บ่อย | Merchant: Nike, Adidas | A | Overlap | Shoes/footwear |
| `beauty_conscious` | ร้านเครื่องสำอาง ≥ 3 ครั้ง/เดือน | MCC: Beauty | A | Overlap | Beauty/Feminine |
| `tech_gadget_buyer` | electronics ≥ 2 ครั้ง/ไตรมาส | MCC: Electronics | A | Existing | - |
| `home_decor_lover` | furniture/home goods บ่อย | Merchant: IKEA, HomePro | A | Overlap | Furniture & Home Decor |
| `book_lover` | bookstore ≥ 1 ครั้ง/เดือน | Merchant: Se-Ed, B2S | A | Existing | - |
| `sports_gear_buyer` | ร้านอุปกรณ์กีฬา ≥ 2 ครั้ง/ไตรมาส | MCC: Sporting Goods | A | Overlap | Sport & activewear |
| `grocery_regular` | supermarket ≥ 3 ครั้ง/เดือน | Merchant: Tops, BigC | A | Existing | - |
| `convenience_store_addict` | convenience store ≥ 15 ครั้ง/เดือน | Merchant: 7-Eleven | A | Overlap | Convenient Seekers, Fast Consumer/Convenience |
| `department_store_loyal` | ≥ 70% dept txn ที่ chain เดิม | Merchant concentration | A | Existing | - |
| `marketplace_shopper` | Shopee/Lazada ≥ 4 ครั้ง/เดือน | Merchant: Shopee, Lazada | A | Overlap | E-Commerce |
| `subscription_stacker` | recurring txn ≥ 3 บริการ/เดือน | Recurring pattern | A | Overlap | Subscription |
| `impulse_buyer` | txn สูง หลาย merchant pattern ไม่ consistent | Diversity + Variance | A | Existing | - |
| `brand_switcher` | merchant loyalty ต่ำ ชอบลองใหม่ | Low concentration | A | Existing | - |
| `secondhand_buyer` | platform secondhand | Merchant: Carousell | A | Existing | - |
| `seasonal_shopper` | spike ช่วง 11.11, 12.12, Songkran | Timestamp + Amount spike | A | Existing | - |
| `premium_brand_loyal` | repeat premium brand > 3 ครั้ง/ไตรมาส | Merchant + Amount | A | Overlap | Social Status |
| `hypermarket_shopper` | Makro/Lotus's ≥ 2 ครั้ง/เดือน + large basket | Merchant + High amount | A | Existing | - |
| `jewelry_buyer` | jewelry store txn ≥ 2 ครั้ง/ปี | MCC: Jewelry | A | Existing | - |
| `gold_accumulator` | gold shop txn recurring + consistent amount | Merchant: YLG, Aurora | A | Existing | - |
| `stationery_regular` | stationery store ≥ 1 ครั้ง/เดือน | MCC: Stationery | A | Existing | - |
| `home_office_buyer` | stationery + electronics combo ≥ 4 ครั้ง/ปี | MCC combo | A | Existing | - |
| `fast_fashion_buyer` | fashion MCC + low avg ticket + high frequency | MCC + Amount + Frequency | A | Existing | - |
| `accessories_collector` | jewelry + fashion accessory บ่อย | MCC: Jewelry + Apparel | A | Overlap | Handbags & accessories |
| `flash_sale_hunter` | e-commerce spike ช่วง 11.11, 12.12 > 3x avg | Timestamp + Amount | A | Existing | - |
| `cross_border_shopper` | foreign e-commerce ≥ 4 ครั้ง/ปี | Merchant: Amazon, ASOS | A | Existing | - |
| `mall_shopper` | ≥ 60% retail txn ที่ merchant ในห้าง | merchant_location = Mall | B | Existing | - |
| `bargain_hunter` | outlet/discount store บ่อย | venue_type = Outlet | B | Overlap | Value Economy |
| `gifting_regular` | gift shop ช่วงเทศกาลสม่ำเสมอ | merchant_type = Gift | B | Existing | - |
| `luxury_gifter` | jewelry + dept store spike ช่วง Valentine/Mother's Day | MCC combo + Timestamp | B | Existing | - |
| `eco_conscious_shopper` | sustainable/organic/eco brand บ่อย | merchant_type = Eco/Sustainable | B | New | Minimal/Sustainable |
| `travel_bag_enthusiast` | luggage/travel bag ≥ 2 ครั้ง/ปี + travel combo | MCC: Luggage + Travel | B | New | Travel & lifestyle bags |

---

### 🎭 Entertainment & Lifestyle
> v1: 18 | v2: +7 | v2.1: +3 | รวม: 28 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `movie_lover` | cinema ≥ 2 ครั้ง/เดือน | Merchant: SF, Major | A | Overlap | Entertainment |
| `concert_goer` | ticketing ≥ 3 ครั้ง/ปี | Merchant: Eventpop | A | Overlap | Entertainment |
| `gym_member` | fitness center recurring ≥ 6 เดือน | Merchant: Fitness First | A | Existing | - |
| `gamer` | gaming platform บ่อย | Merchant: Steam, PS Store | A | Existing | - |
| `night_owl_entertainer` | entertainment หลัง 22:00 บ่อย | MCC + Timestamp | A | Overlap | Nightlife |
| `karaoke_regular` | karaoke ≥ 2 ครั้ง/เดือน | Merchant: Tawandang | A | Overlap | Nightlife |
| `spa_lover` | spa/massage ≥ 2 ครั้ง/เดือน | MCC: Personal Care | A | Overlap | Spa & Massage |
| `music_festival_goer` | festival ticketing ≥ 2 ครั้ง/ปี + high amount | Ticketing + Amount | A | Overlap | Entertainment |
| `streaming_subscriber` | ≥ 2 streaming subscriptions | Merchant: Netflix, Disney+ | A | Overlap | Subscription |
| `outdoor_adventurer` | outdoor gear + travel combo | Merchant: Decathlon + MCC | A | Overlap | Adventure |
| `theme_park_visitor` | theme park ≥ 1 ครั้ง/ปี | Merchant: Universal | A | Overlap | Entertainment |
| `nail_salon_regular` | nail salon ≥ 2 ครั้ง/เดือน | MCC: Beauty + Merchant | A | Overlap | Nail |
| `hair_salon_loyal` | ≥ 70% hair txn ที่ร้านเดิม + monthly | Merchant concentration | A | Overlap | Hair |
| `sport_event_goer` | stadium/sport event ≥ 3 ครั้ง/ปี | MCC: Ticket + Stadium | A | Existing | - |
| `esports_fan` | esports event ticketing + gaming spend combo | Merchant: RoV, PUBG event | A | Existing | - |
| `pet_friendly_lifestyle` | pet + travel + dining combo | MCC combo | A | Existing | - |
| `sports_fan` | stadium/sport event ≥ 2 ครั้ง/ปี | venue_type = Stadium | B | Existing | - |
| `yoga_practitioner` | yoga studio ≥ 2 ครั้ง/เดือน | activity_type = Yoga | B | Existing | - |
| `golf_player` | golf course ≥ 1 ครั้ง/เดือน | activity_type = Golf | B | Existing | - |
| `art_culture_enthusiast` | museum/gallery/art event | venue_type = Cultural | B | Existing | - |
| `escape_room_fan` | escape room ≥ 2 ครั้ง/ไตรมาส | venue_type = Escape Room | B | Existing | - |
| `board_game_cafe_goer` | board game cafe บ่อย | venue_type = Board Game | B | Existing | - |
| `bowling_regular` | bowling ≥ 1 ครั้ง/เดือน | venue_type = Bowling | B | Existing | - |
| `pilates_devotee` | pilates studio ≥ 3 ครั้ง/เดือน | activity_type = Pilates | B | Existing | - |
| `muay_thai_trainee` | muay thai gym txn recurring | activity_type = Muay Thai | B | Existing | - |
| `brow_treatment_regular` | brow specialist ≥ 1 ครั้ง/เดือน | venue_type = Brow Studio | B | New | Brow |
| `lash_extension_regular` | lash studio ≥ 1 ครั้ง/เดือน | venue_type = Lash Studio | B | New | Lash |
| `waxing_regular` | wax studio ≥ 1 ครั้ง/เดือน | venue_type = Wax Studio | B | New | Wax |

---

### 🚗 Transport & Commute
> v1: 10 | v2: +6 | รวม: 16 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `daily_commuter` | fuel/transit weekday ≥ 20 วัน/เดือน | MCC + Timestamp | A | Existing | - |
| `car_owner` | fuel + parking + auto service ครบ | MCC combo | A | Overlap | Car owners |
| `grab_dependent` | Grab ≥ 15 ครั้ง/เดือน | Merchant: Grab | A | Existing | - |
| `taxi_user` | taxi บ่อย + Grab น้อย | MCC: Taxi | A | Existing | - |
| `fuel_brand_loyal` | ≥ 70% fuel ที่ปั๊มแบรนด์เดียว | Merchant concentration | A | Existing | - |
| `ev_driver` | EV charging station | Merchant: EA Anywhere | A | Existing | - |
| `bts_mrt_user` | BTS/MRT บ่อย | Merchant: Rabbit, MRT | A | Existing | - |
| `motorbike_user` | fuel < 200 บาท/ครั้ง สม่ำเสมอ | Amount pattern | A | Existing | - |
| `parking_heavy` | parking > 15 ครั้ง/เดือน | MCC: Parking | A | Existing | - |
| `long_distance_driver` | toll บ่อย / fuel ต่างจังหวัด | MCC: Toll | A | Existing | - |
| `car_enthusiast` | auto accessories + car wash + detailing บ่อย | MCC: Auto Accessories | A | Existing | - |
| `car_maintenance_regular` | service center + tire + oil ≥ 4 ครั้ง/ปี | MCC: Auto Service | A | Existing | - |
| `high_fuel_spender` | fuel spend > P75 ของ portfolio | MCC: Petrol + Amount | A | Existing | - |
| `ride_share_switcher` | สลับ Grab / Bolt / InDriver บ่อย | Merchant diversity | A | Existing | - |
| `van_pool_user` | minibus/van service txn บ่อย ช่วง commute | MCC: Transportation + Time | A | Existing | - |
| `new_car_seeker` | auto showroom txn ≥ 1 ครั้ง | MCC: Automobile + High amount | A | Existing | - |

---

### 💊 Health & Wellness
> v1: 12 | v2: +8 | รวม: 20 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `health_conscious` | gym + pharmacy + health food ≥ 2 จาก 3 | MCC combo | A | Overlap | Health |
| `pharmacy_regular` | pharmacy ≥ 3 ครั้ง/เดือน | MCC: Drug Store | A | Existing | - |
| `hospital_visitor` | hospital ≥ 2 ครั้ง/ไตรมาส | MCC: Hospital | A | Existing | - |
| `supplement_buyer` | Watsons/Boots บ่อย | Merchant: Watsons | A | Existing | - |
| `organic_food_lover` | organic/health food store | Merchant: Lemon Farm | A | Existing | - |
| `dental_care_conscious` | dental clinic ≥ 2 ครั้ง/ปี | MCC: Dental | A | Existing | - |
| `fitness_first_user` | Fitness First recurring | Merchant: Fitness First | A | Existing | - |
| `eye_care_regular` | optician ≥ 2 ครั้ง/ปี | MCC: Optical | A | Existing | - |
| `maternal_care` | OB/GYN + baby products ช่วงเวลาเดียวกัน | MCC combo + Timing | A | Existing | - |
| `regular_checkup_goer` | hospital/clinic txn recurring ≥ 1 ครั้ง/ไตรมาส | MCC: Hospital + Recurring | A | Existing | - |
| `mental_wellness_seeker` | meditation app + wellness center + spa combo | Merchant: Headspace + MCC | A | Overlap | Wellness and Longevity |
| `sports_nutrition_buyer` | protein supplement + sports gear combo | Merchant: Supersports + Nutrition | A | Existing | - |
| `aesthetic_spender` | beauty clinic + cosmetics high spend | MCC: Beauty + Amount | A | Overlap | Derma/Aesthetic |
| `high_medical_spender` | hospital/clinic spend > P75 | MCC: Hospital + Amount | A | Existing | - |
| `weight_management_focused` | gym + low dining spend + supplement combo | MCC combo | A | Existing | - |
| `beauty_clinic_visitor` | aesthetic clinic บ่อย | clinic_type = Aesthetic | B | Overlap | Derma/Aesthetic, Treatment |
| `mental_health_aware` | therapy/wellness center | clinic_type = Mental Health | B | Existing | - |
| `traditional_medicine` | ยาแผนโบราณ / แพทย์แผนจีน | clinic_type = TCM | B | Existing | - |
| `specialized_treatment_seeker` | specialist clinic ≥ 4 ครั้ง/ปี (non-GP) | clinic_type = Specialist | B | Existing | - |
| `fertility_aware` | fertility clinic / OB txn + baby product combo | clinic_type = Fertility | B | Existing | - |

---

### 💳 Financial Behavior
> v1: 14 | v2: +10 | v2.1: +1 | รวม: 25 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `high_spender` | total spend > P75 | Amount | A | Existing | - |
| `mid_spender` | total spend P25–P75 | Amount | A | Existing | - |
| `low_spender` | total spend < P25 | Amount | A | Existing | - |
| `consistent_spender` | CV monthly spend ต่ำ | Variance | A | Existing | - |
| `seasonal_spender` | spike > 2x avg ≥ 2 ครั้ง/ปี | Timestamp + Amount | A | Existing | - |
| `end_of_month_spender` | ≥ 40% spend วันที่ 25–31 | Timestamp | A | Existing | - |
| `paycheck_spender` | spike ต้นเดือน (1–5) | Timestamp + Amount | A | Existing | - |
| `installment_user` | installment ≥ 1 ครั้ง/ไตรมาส | Installment flag | A | Existing | - |
| `high_utilization` | credit utilization > 70% สม่ำเสมอ | Utilization | A | Existing | - |
| `low_utilization` | credit utilization < 20% | Utilization | A | Existing | - |
| `multi_card_user` | spend pattern บ่งชี้หลายบัตร | Spend pattern | A | Existing | - |
| `cash_advance_user` | cash advance ≥ 1 ครั้ง/ปี | Txn type | A | Existing | - |
| `reward_maximizer` | ≥ 50% spend ที่ high-points merchant | Merchant + Reward | A | Existing | - |
| `single_category_user` | ≥ 80% spend ใน MCC เดียว | MCC concentration | A | Existing | - |
| `investor` | investment platform / บล. txn ≥ 4 ครั้ง/ปี | MCC: Investment | A | Existing | - |
| `regular_investor` | investment txn recurring รายเดือน | MCC: Investment + Recurring | A | Existing | - |
| `insurance_holder` | insurance premium txn recurring | MCC: Insurance | A | Existing | - |
| `multi_insurance_holder` | ≥ 2 insurance products recurring | MCC: Insurance + Diverse | A | Existing | - |
| `high_installment_user` | installment txn ≥ 3 active พร้อมกัน | Installment count | A | Existing | - |
| `financially_disciplined` | low utilization + no cash advance + consistent | Combined behavioral | A | Existing | - |
| `cash_flow_stressed` | high utilization + cash advance + end-of-month heavy | Combined behavioral | A | Existing | - |
| `wealth_builder` | investor + insurance + low impulse combo | MCC combo | A | Existing | - |
| `big_ticket_buyer` | single txn > P95 ≥ 2 ครั้ง/ปี | Amount spike | A | Existing | - |
| `small_business_spender` | telecom + ads + supplies + irregular high amount | MCC combo pattern | A | Overlap | Biz Owner |
| `donation_giver` | donation/charity txn ≥ 2 ครั้ง/ปี | MCC: Donation/Charity | A | New | Donation |

---

### 👨‍👩‍👧 Life Stage
> v1: 14 | v2: +8 | v2.1: +1 | รวม: 23 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `parent` | baby/kids + family restaurant บ่อย | Merchant + MCC | A | Overlap | Family/Kids |
| `new_parent` | spike baby products ใน 12 เดือน | Merchant + Recency | A | Existing | - |
| `pet_owner` | pet shop/vet ≥ 1 ครั้ง/เดือน | Merchant: Pet Planet | A | Existing | - |
| `homeowner` | home improvement + utility ≥ 1 ครั้ง/ไตรมาส | Merchant: HomePro | A | Overlap | Home Center |
| `senior_lifestyle` | pharmacy + hospital + market dominant | MCC combo | A | Existing | - |
| `empty_nester` | kids merchant ลดลง + travel/leisure เพิ่ม | Trend | A | Existing | - |
| `teen_spender` | gaming + fastfood + convenience dominant | MCC combo | A | Existing | - |
| `career_starter` | low spend + professional attire | Amount + MCC | A | Existing | - |
| `family_breadwinner` | high spend + diverse category | Amount + Diversity | A | Existing | - |
| `retiree_lifestyle` | weekday ≈ weekend ratio + pharmacy heavy | Timestamp + MCC | A | Existing | - |
| `multi_pet_owner` | pet txn diverse (vet + grooming + food + toys) | MCC + Merchant diversity | A | Existing | - |
| `home_renovator` | high spend HomePro/contractor ≥ 3 ครั้ง/ปี | Merchant: HomePro + Amount | A | Overlap | Home Services, Building Materials Store |
| `school_fee_payer` | school/tuition txn recurring รายเทอม | MCC: Education + Recurring | A | Existing | - |
| `extracurricular_parent` | music school + art class + sports academy txn | MCC: Education + Kids | A | Existing | - |
| `sandwich_generation` | ทั้ง kids txn และ senior care txn พร้อมกัน | MCC combo | A | Existing | - |
| `newly_married` | jewelry + wedding vendor + honeymoon travel combo | MCC combo + Timeline | A | Existing | - |
| `student` | ใกล้มหาวิทยาลัย + stationery + low spend | merchant_location = Uni | B | Existing | - |
| `young_professional` | coffee weekday เช้า + lunch ใกล้ office | merchant_location = Office | B | Overlap | Professional |
| `college_age` | ใกล้มหาวิทยาลัย + delivery + low ticket | merchant_location = Uni | B | Existing | - |
| `digital_nomad` | co-working space + coffee + travel combo | venue_type = Co-working | B | Existing | - |
| `expat_lifestyle` | foreign cuisine + international market + foreign transfer | merchant_type = International | B | Existing | - |
| `tattoo_enthusiast` | tattoo studio txn ≥ 1 ครั้ง/ปี | venue_type = Tattoo Studio | B | New | Tatto |

---

### ⏰ Time Patterns
> v1: 10 | v2: +5 | รวม: 15 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `morning_person` | ≥ 40% txn ก่อน 09:00 | Timestamp | A | Existing | - |
| `night_owl_spender` | ≥ 30% txn หลัง 22:00 | Timestamp | A | Existing | - |
| `weekend_warrior` | ≥ 60% spend Sat-Sun | Timestamp | A | Existing | - |
| `weekday_spender` | ≥ 70% spend Mon-Fri | Timestamp | A | Existing | - |
| `lunch_hour_regular` | spike 12:00–14:00 ทุก weekday | Timestamp | A | Existing | - |
| `after_work_spender` | spike 18:00–21:00 | Timestamp | A | Existing | - |
| `holiday_spender` | spend +50% ช่วงวันหยุดยาว | Timestamp + Amount | A | Existing | - |
| `payday_spike` | spike วันที่ 25–5 ต้นเดือน | Timestamp + Amount | A | Existing | - |
| `monthly_planner` | spend กระจาย consistent ไม่มี spike | Variance | A | Existing | - |
| `off_peak_shopper` | retail 09:00–12:00 วันธรรมดา | Timestamp | A | Existing | - |
| `songkran_spender` | spend spike ช่วง Songkran (เม.ย.) ทุกปี | Timestamp + Amount | A | Existing | - |
| `year_end_big_spender` | spend spike ธ.ค. > 2x avg ทุกปี | Timestamp + Amount | A | Existing | - |
| `ramadan_aware_spender` | dining pattern เปลี่ยนช่วง Ramadan | Timestamp + Dining | A | Existing | - |
| `event_day_spender` | spend spike ตรงกับ major event | Timestamp + Amount spike | A | Existing | - |
| `early_bird_shopper` | ≥ 40% retail txn ก่อน 10:00 | Timestamp | A | Existing | - |

---

### 📱 Digital Behavior
> v1: 8 | v2: +7 | รวม: 15 tags

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `online_native` | ≥ 70% txn เป็น online | Channel | A | Existing | - |
| `contactless_payer` | ≥ 80% in-store เป็น tap/NFC | Payment method | A | Existing | - |
| `app_heavy_user` | ≥ 50% txn ผ่าน mobile app | Channel | A | Existing | - |
| `digital_subscription_heavy` | ≥ 4 recurring digital/เดือน | Recurring + Digital | A | Existing | - |
| `streaming_only` | streaming ≥ 2 + cinema = 0 | Merchant pattern | A | Existing | - |
| `social_commerce_buyer` | TikTok Shop txn ≥ 4 ครั้ง | Merchant: TikTok Shop | A | Existing | - |
| `crypto_curious` | crypto exchange ≥ 1 ครั้ง | Merchant: Bitkub | A | Existing | - |
| `fintech_user` | fintech platform บ่อย | Merchant: TrueMoney | A | Existing | - |
| `high_telecom_spender` | telecom spend > P75 | MCC: Telecom + Amount | A | Existing | - |
| `device_upgrader` | new device txn ≥ 1/ปี + high telecom | MCC: Electronics + Telecom | A | Existing | - |
| `saas_subscriber` | software/SaaS recurring ≥ 3 | Merchant: Adobe, Notion | A | Existing | - |
| `ai_tool_user` | AI platform txn (ChatGPT Plus, Midjourney) | Merchant: OpenAI | A | Existing | - |
| `cashless_convert` | contactless + online combo > 90% | Payment + Channel | A | Existing | - |
| `social_ads_spender` | Facebook/Google/TikTok Ads txn ≥ 4 ครั้ง/ปี | Merchant: Meta, Google Ads | A | Existing | - |
| `e_wallet_heavy` | e-wallet > 30% ของ txn | Merchant: E-wallet | A | Existing | - |

---

## หมวดใหม่ที่ยังไม่มีใน v1

---

### 🎓 Education & Learning

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `lifelong_learner` | online course platform ≥ 4 ครั้ง/ปี | Merchant: Coursera, Udemy | A | Overlap | Skill Development & Training |
| `language_learner` | language school/app txn recurring | Merchant: British Council | A | Existing | - |
| `professional_upskiller` | certification / professional course ≥ 2 ครั้ง/ปี | MCC: Education + Amount | A | Overlap | Skill Development & Training |
| `tutor_seeker` | tutoring center txn recurring รายเดือน | MCC: Education + Recurring | A | Existing | - |
| `school_supply_buyer` | stationery + kids spike ต้นปีการศึกษา | MCC combo + Timestamp | A | Existing | - |
| `university_student` | student merchant + dining + convenience + low spend | MCC combo + Amount | A | Existing | - |
| `education_investor` | high education spend > P75 across family | MCC: Education + Amount | A | Existing | - |
| `stem_enthusiast` | electronics + coding subscription + stationery combo | MCC combo | A | Existing | - |
| `arts_student` | art supplies + music instrument + performance txn | MCC: Stationery + Entertainment | A | Existing | - |

---

### 🏠 Real Estate & Housing

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `utility_payer` | utility txn recurring รายเดือน | MCC: Utility + Recurring | A | Existing | - |
| `high_utility_user` | utility spend > P75 | MCC: Utility + Amount | A | Existing | - |
| `condo_resident` | utility + condo management fee recurring | MCC: Utility + Pattern | A | Existing | - |
| `home_appliance_buyer` | white goods ≥ 1 ครั้ง/ปี + high amount | MCC: Electronics/Household | A | Existing | - |
| `diy_homeowner` | hardware store + home improvement บ่อย | Merchant: Global House | A | Overlap | Building Materials Store, Home Center |
| `property_market_watcher` | real estate agent txn / property expo ≥ 1 ครั้ง/ปี | MCC: Real Estate | A | Existing | - |
| `rental_income_owner` | irregular large incoming + utility multi-unit | Amount + Utility pattern | A | Existing | - |

---

### 📊 Investment & Financial Planning

| Tag | Definition | Signal | Path | Source | Enrichment Tag |
|-----|-----------|--------|------|--------|----------------|
| `stock_market_participant` | brokerage txn ≥ 4 ครั้ง/ปี | Merchant: Settrade, Jitta | A | Existing | - |
| `mutual_fund_investor` | fund platform txn recurring | Merchant: FINNOMENA | A | Existing | - |
| `gold_investor` | gold shop / gold ETF txn ≥ 4 ครั้ง/ปี | Merchant: YLG, MTS Gold | A | Existing | - |
| `real_estate_investor` | real estate agent + property expo + large amount | MCC: Real Estate + Amount | A | Existing | - |
| `passive_income_seeker` | investment + insurance + low consumption | MCC combo | A | Existing | - |
| `financial_planner_client` | insurance + investment + consistent saving | MCC combo | A | Existing | - |

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
| **รวม** | **187** | **58** | **21** | **323** |

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

*v2.1 — Thena × Tee | 2026-04-18 | 323 tags | 58 overlap กับ enrichment tags ของทีม*
