"""
add_stability_column.py
เพิ่ม Stability column ให้ทุก tag table ใน customer_tag_library_v2_expansion.md

S = Stable       — พฤติกรรมหลัก ไม่ควรกระพือ (churn rate < 20%/เดือน)
V = Variable     — event-based หรือ seasonal ที่ fluctuate ได้ตามธรรมชาติ
M = Momentum     — ออกแบบให้เปลี่ยนได้ แต่ค่อยๆ เปลี่ยน (transitional)
"""
import re

TARGET = "/Users/adisornj/Desktop/Thena/lab/customer_tag_library_v2_expansion.md"

STABILITY = {
    # ── Food & Dining ──────────────────────────────────────────────────────────
    "frequent_diner": "S", "fast_food_regular": "S", "fine_dining_enthusiast": "S",
    "cafe_hopper": "S", "bubble_tea_addict": "S", "delivery_dependent": "S",
    "brunch_person": "S", "late_night_diner": "S", "bakery_lover": "S",
    "budget_eater": "S", "solo_diner": "S", "street_food_lover": "S",
    "dessert_lover": "S", "group_diner": "S", "work_lunch_regular": "S",
    "coffee_loyalist": "S", "weekend_foodie": "S",
    "japanese_food_lover": "S", "korean_food_lover": "S", "chinese_food_lover": "S",
    "thai_food_loyalist": "S", "western_food_lover": "S", "italian_food_lover": "S",
    "seafood_lover": "S", "vegetarian_friendly": "S", "food_court_regular": "S",
    "buffet_lover": "S", "family_restaurant_goer": "S", "healthy_eater": "S",
    "halal_restaurant_goer": "S",
    "omakase_enthusiast": "V",   # txn rare / sparse → กระพือตามโอกาส
    "rooftop_bar_goer": "V",     # occasion-based
    "plant_based_explorer": "M", # behavioral shift ที่ค่อยๆ เปลี่ยน
    "bbq_lover": "S", "hot_pot_lover": "S", "noodle_lover": "S",
    "steak_lover": "S", "french_food_lover": "S", "american_food_lover": "S",
    "vietnamese_food_lover": "S", "thai_isan_lover": "S", "thai_northern_lover": "S",
    "thai_southern_lover": "S", "alcohol_buyer": "S", "tea_house_regular": "S",
    "juice_bar_regular": "S", "drinks_shop_regular": "S",

    # ── Travel & Hotel ─────────────────────────────────────────────────────────
    "frequent_traveler": "S",
    "international_traveler": "V", "domestic_traveler": "V",
    "budget_traveler": "S", "luxury_traveler": "S", "business_traveler": "S",
    "leisure_traveler": "V",
    "hotel_loyalist": "S", "airbnb_user": "V", "frequent_flyer": "S",
    "backpacker_style": "S", "last_minute_booker": "S", "early_planner": "S",
    "staycation_lover": "V", "duty_free_shopper": "V", "long_stay_traveler": "V",
    "solo_traveler": "S",
    "asia_traveler": "V", "europe_traveler": "V", "resort_lover": "V",
    "city_traveler": "V", "japan_traveler": "V", "luxury_resort_seeker": "V",
    "cruise_passenger": "V", "workcation_traveler": "V",

    # ── Shopping ───────────────────────────────────────────────────────────────
    "online_first_shopper": "S", "luxury_shopper": "S", "fashion_lover": "S",
    "sneaker_enthusiast": "S", "beauty_conscious": "S",
    "tech_gadget_buyer": "V",   # episodic, ไม่บ่อย
    "home_decor_lover": "V",    # episodic
    "book_lover": "S", "sports_gear_buyer": "V",
    "grocery_regular": "S", "convenience_store_addict": "S",
    "department_store_loyal": "S", "marketplace_shopper": "S",
    "subscription_stacker": "S", "impulse_buyer": "S", "brand_switcher": "S",
    "secondhand_buyer": "V",
    "seasonal_shopper": "V",    # by definition seasonal
    "premium_brand_loyal": "S", "hypermarket_shopper": "S",
    "jewelry_buyer": "V",       # episodic
    "gold_accumulator": "S", "stationery_regular": "S",
    "home_office_buyer": "V",   # episodic
    "fast_fashion_buyer": "S", "accessories_collector": "S",
    "flash_sale_hunter": "V",   # event-driven
    "cross_border_shopper": "V",
    "mall_shopper": "S", "bargain_hunter": "S",
    "gifting_regular": "V",     # occasion-based
    "luxury_gifter": "V",       # occasion-based
    "eco_conscious_shopper": "S", "travel_bag_enthusiast": "V",

    # ── Entertainment & Lifestyle ──────────────────────────────────────────────
    "movie_lover": "S",
    "concert_goer": "V",        # event-based
    "gym_member": "S", "gamer": "S", "night_owl_entertainer": "S",
    "karaoke_regular": "S", "spa_lover": "S",
    "music_festival_goer": "V", # event-based
    "streaming_subscriber": "S", "outdoor_adventurer": "S",
    "theme_park_visitor": "V",  # episodic
    "nail_salon_regular": "S", "hair_salon_loyal": "S",
    "sport_event_goer": "V",    # event-based
    "esports_fan": "V",         # event-based
    "pet_friendly_lifestyle": "S",
    "sports_fan": "V",          # event-based
    "yoga_practitioner": "S", "golf_player": "S",
    "art_culture_enthusiast": "V", # event-based
    "escape_room_fan": "V",     # episodic
    "board_game_cafe_goer": "S", "bowling_regular": "S",
    "pilates_devotee": "S", "muay_thai_trainee": "S",
    "brow_treatment_regular": "S", "lash_extension_regular": "S",
    "waxing_regular": "S",

    # ── Transport & Commute ────────────────────────────────────────────────────
    "daily_commuter": "S", "car_owner": "S", "grab_dependent": "S",
    "taxi_user": "S", "fuel_brand_loyal": "S", "ev_driver": "S",
    "bts_mrt_user": "S", "motorbike_user": "S", "parking_heavy": "S",
    "long_distance_driver": "S", "car_enthusiast": "S",
    "car_maintenance_regular": "S", "high_fuel_spender": "S",
    "ride_share_switcher": "S", "van_pool_user": "S",
    "new_car_seeker": "V",      # one-time event

    # ── Health & Wellness ─────────────────────────────────────────────────────
    "health_conscious": "S", "pharmacy_regular": "S",
    "hospital_visitor": "V",    # event-based
    "supplement_buyer": "S", "organic_food_lover": "S",
    "dental_care_conscious": "S", "fitness_first_user": "S",
    "eye_care_regular": "S",
    "maternal_care": "M",       # life stage transition
    "regular_checkup_goer": "S", "mental_wellness_seeker": "S",
    "sports_nutrition_buyer": "S", "aesthetic_spender": "S",
    "high_medical_spender": "V", # event-based
    "weight_management_focused": "S", "beauty_clinic_visitor": "S",
    "mental_health_aware": "S", "traditional_medicine": "S",
    "specialized_treatment_seeker": "V", # episodic
    "fertility_aware": "V",     # life event

    # ── Financial Behavior ────────────────────────────────────────────────────
    "high_spender": "S", "mid_spender": "S", "low_spender": "S",
    "consistent_spender": "S",
    "seasonal_spender": "V",    # by definition
    "end_of_month_spender": "S", "paycheck_spender": "S",
    "installment_user": "S", "high_utilization": "S", "low_utilization": "S",
    "multi_card_user": "S", "cash_advance_user": "S",
    "reward_maximizer": "S", "single_category_user": "S",
    "investor": "S", "regular_investor": "S",
    "insurance_holder": "S", "multi_insurance_holder": "S",
    "high_installment_user": "S", "financially_disciplined": "S",
    "cash_flow_stressed": "M",  # สถานะที่อาจดีขึ้น/แย่ลงได้
    "wealth_builder": "S",
    "big_ticket_buyer": "V",    # episodic
    "small_business_spender": "S",
    "donation_giver": "V",      # occasion-based

    # ── Life Stage ────────────────────────────────────────────────────────────
    "parent": "S",
    "new_parent": "M",          # transition phase ~12 เดือน
    "pet_owner": "S", "homeowner": "S", "senior_lifestyle": "S",
    "empty_nester": "M",        # transition phase
    "teen_spender": "S", "career_starter": "S",
    "family_breadwinner": "S", "retiree_lifestyle": "S",
    "multi_pet_owner": "S",
    "home_renovator": "V",      # project-based
    "school_fee_payer": "S", "extracurricular_parent": "S",
    "sandwich_generation": "S",
    "newly_married": "M",       # transition phase ~24 เดือน
    "student": "S", "young_professional": "S", "college_age": "S",
    "digital_nomad": "S", "expat_lifestyle": "S",
    "tattoo_enthusiast": "V",   # episodic

    # ── Time Patterns ─────────────────────────────────────────────────────────
    "morning_person": "S", "night_owl_spender": "S", "weekend_warrior": "S",
    "weekday_spender": "S", "lunch_hour_regular": "S", "after_work_spender": "S",
    "holiday_spender": "V",     # by definition
    "payday_spike": "V",        # month-end event
    "monthly_planner": "S", "off_peak_shopper": "S",
    "songkran_spender": "V", "year_end_big_spender": "V",
    "ramadan_aware_spender": "V", "event_day_spender": "V",
    "early_bird_shopper": "S",

    # ── Digital Behavior ──────────────────────────────────────────────────────
    "online_native": "S", "contactless_payer": "S", "app_heavy_user": "S",
    "digital_subscription_heavy": "S", "streaming_only": "S",
    "social_commerce_buyer": "S",
    "crypto_curious": "V",      # episodic
    "fintech_user": "S", "high_telecom_spender": "S",
    "device_upgrader": "V",     # episodic
    "saas_subscriber": "S", "ai_tool_user": "S", "cashless_convert": "S",
    "social_ads_spender": "S", "e_wallet_heavy": "S",

    # ── Education & Learning ──────────────────────────────────────────────────
    "lifelong_learner": "S", "language_learner": "S",
    "professional_upskiller": "S", "tutor_seeker": "S",
    "school_supply_buyer": "V", # seasonal (ต้นปีการศึกษา)
    "university_student": "S", "education_investor": "S",
    "stem_enthusiast": "S", "arts_student": "S",

    # ── Real Estate & Housing ─────────────────────────────────────────────────
    "utility_payer": "S", "high_utility_user": "S", "condo_resident": "S",
    "home_appliance_buyer": "V", # episodic
    "diy_homeowner": "V",       # project-based
    "property_market_watcher": "V", # episodic
    "rental_income_owner": "V", # hard to measure + event-based

    # ── Investment & Financial Planning ───────────────────────────────────────
    "stock_market_participant": "S", "mutual_fund_investor": "S",
    "gold_investor": "S",
    "real_estate_investor": "V", # episodic
    "passive_income_seeker": "S", "financial_planner_client": "S",

    # ── Payment Behavior (v2.2) ───────────────────────────────────────────────
    "full_payer": "S", "minimum_payer": "S",
    "revolving_user": "M",      # สถานะที่เปลี่ยนได้ตามวินัยการเงิน
    "partial_payer": "S", "early_payer": "S",
    "late_payer_history": "M",  # อาจปรับพฤติกรรมดีขึ้นได้
    "autopay_enrolled": "S",
    "payment_irregular": "M",   # สามารถเปลี่ยนได้

    # ── Card Relationship (v2.2) ──────────────────────────────────────────────
    "primary_card_signal": "S", "secondary_card_signal": "S",
    "limit_approacher": "M",    # utilization เปลี่ยนตามพฤติกรรม
    "benefit_chaser": "V",      # campaign-driven
    "card_renewal_spiker": "V", # annual event
    "installment_converter": "S",

    # ── Spending Momentum (v2.2) ──────────────────────────────────────────────
    "accelerating_spender": "M", "decelerating_spender": "M",
    "stable_spender": "S",
    "recovering_spender": "M", "boom_bust_spender": "M",
}

LEGEND = """> **Stability Type:**
> `S` = **Stable** — พฤติกรรมหลัก ควร stable ตลอดเวลา | เกณฑ์: tag churn < 20%/เดือน
> `V` = **Variable** — event-based หรือ seasonal ที่ fluctuate ได้ตามธรรมชาติ — ไม่ใช่ bug
> `M` = **Momentum** — ออกแบบให้เปลี่ยนได้ แต่ค่อยๆ เปลี่ยน (transitional / trend-based)

"""

def add_stability(content: str) -> str:
    lines = content.split("\n")
    result = []
    in_tag_table = False

    for line in lines:
        # ตรวจว่าเป็น header row ของ tag table (มี "| Tag |")
        if re.match(r"\|\s*Tag\s*\|", line):
            in_tag_table = True
            line = line.rstrip(" |") + " Stability |"

        # separator row
        elif in_tag_table and re.match(r"\|[-| :]+\|", line):
            line = line.rstrip(" |") + "---|"

        # data row: ขึ้นต้นด้วย | `tag_name`
        elif in_tag_table and re.match(r"\|\s*`", line):
            m = re.match(r"\|\s*`([^`]+)`", line)
            if m:
                tag = m.group(1)
                stab = STABILITY.get(tag, "?")
                line = line.rstrip(" |") + f" {stab} |"

        # ออกจาก table ถ้าบรรทัดไม่ใช่ table row
        elif in_tag_table and not line.startswith("|"):
            in_tag_table = False

        result.append(line)

    return "\n".join(result)


with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# เพิ่ม legend หลัง > line แรก (Path/Source legend)
legend_marker = "> **Source**:"
content = content.replace(legend_marker, LEGEND + legend_marker)

content = add_stability(content)

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(content)

# count
s_count = sum(1 for v in STABILITY.values() if v == "S")
v_count = sum(1 for v in STABILITY.values() if v == "V")
m_count = sum(1 for v in STABILITY.values() if v == "M")
q_count = sum(1 for v in STABILITY.values() if v == "?")

print(f"✅  Stability column added to all tag tables")
print(f"   S (Stable):   {s_count} tags")
print(f"   V (Variable): {v_count} tags")
print(f"   M (Momentum): {m_count} tags")
if q_count:
    print(f"   ? (Unknown):  {q_count} tags — ต้องไปแก้เพิ่ม")
print(f"   Total mapped: {len(STABILITY)} / 342")
