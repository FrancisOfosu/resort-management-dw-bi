import random
from datetime import date, timedelta
from collections import Counter

random.seed(42)

OUTPUT_FILE = "populate_resort_operational_db.sql"

# =====================================================
# MAIN SETTINGS
# =====================================================

PERSON_COUNT = 1500
RESORT_COUNT = 5
HOTEL_COUNT = 10
ROOM_COUNT = 100
WELLNESS_CENTER_COUNT = 8
SPECIFIC_SERVICE_COUNT = 35
SWIMMING_POOL_COUNT = 15
SOCIAL_MEDIA_COUNT = 15
STOCK_MARKET_TITLE_COUNT = 10
VALUE_TABLE_COUNT = 150
STOCK_VALUE_COUNT = 250
SPECIAL_OFFER_COUNT = 60

ROOM_RENTAL_COUNT = 900
SERVICE_RENTAL_COUNT = 500
POOL_RENTAL_COUNT = 300
INVESTMENT_COUNT = 250
FOLLOW_COUNT = 600
DISCOUNT_ROOM_COUNT = 80
DISCOUNT_SERVICE_COUNT = 70
FREE_ACCESS_COUNT = 50
PROVIDES_COUNT = 300

# PAYMENT is generated separately:
# each person makes 1 to 10 payments.

# =====================================================
# DATA LISTS
# =====================================================

countries = [
    "Germany", "United Kingdom", "France", "United States", "China", "Italy",
    "Spain", "Netherlands", "Belgium", "Switzerland", "Austria", "Sweden",
    "Norway", "Denmark", "Finland", "Ireland", "Portugal", "Poland",
    "Czech Republic", "Canada", "Australia", "Japan", "South Korea", "Brazil",
    "Mexico", "India", "United Arab Emirates", "Saudi Arabia", "Qatar",
    "South Africa", "Ghana", "Nigeria", "Kenya", "Egypt", "Morocco", "Turkey",
    "Greece", "Romania", "Hungary", "Croatia", "Slovenia", "Slovakia",
    "Argentina", "Chile", "Colombia", "Singapore", "Malaysia", "Thailand",
    "Indonesia", "New Zealand"
]

cities_by_country = {
    "Germany": "Berlin",
    "United Kingdom": "London",
    "France": "Paris",
    "United States": "New York",
    "China": "Beijing",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Switzerland": "Zurich",
    "Austria": "Vienna",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Denmark": "Copenhagen",
    "Finland": "Helsinki",
    "Ireland": "Dublin",
    "Portugal": "Lisbon",
    "Poland": "Warsaw",
    "Czech Republic": "Prague",
    "Canada": "Toronto",
    "Australia": "Sydney",
    "Japan": "Tokyo",
    "South Korea": "Seoul",
    "Brazil": "São Paulo",
    "Mexico": "Mexico City",
    "India": "Mumbai",
    "United Arab Emirates": "Dubai",
    "Saudi Arabia": "Riyadh",
    "Qatar": "Doha",
    "South Africa": "Cape Town",
    "Ghana": "Accra",
    "Nigeria": "Lagos",
    "Kenya": "Nairobi",
    "Egypt": "Cairo",
    "Morocco": "Casablanca",
    "Turkey": "Istanbul",
    "Greece": "Athens",
    "Romania": "Bucharest",
    "Hungary": "Budapest",
    "Croatia": "Zagreb",
    "Slovenia": "Ljubljana",
    "Slovakia": "Bratislava",
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Singapore": "Singapore",
    "Malaysia": "Kuala Lumpur",
    "Thailand": "Bangkok",
    "Indonesia": "Jakarta",
    "New Zealand": "Auckland"
}

first_names = [
    "Francis", "Maria", "John", "Linda", "Kwame", "Sophia", "Daniel", "Akosua",
    "Marco", "Emma", "Luca", "Aisha", "Chen", "Mei", "Carlos", "Anna", "Ahmed",
    "Fatima", "James", "Grace", "Hiroshi", "Yuki", "Peter", "Nora", "Miguel",
    "Elena", "Samuel", "Ruth", "Oliver", "Isabella", "Noah", "Mia", "Lucas",
    "Sofia", "David", "Sarah", "Youssef", "Nadia", "Amir", "Leila"
]

last_names = [
    "Ofosu", "Rossi", "Smith", "Brown", "Mensah", "Bianchi", "Wilson", "Owusu",
    "Ricci", "Taylor", "Garcia", "Wang", "Khan", "Müller", "Silva", "Kim",
    "Yamamoto", "Anderson", "Dubois", "Nielsen", "Ahmed", "Santos", "Singh",
    "Boateng", "Moretti", "Johnson", "Martin", "Lopez", "Chen", "Ali"
]

resort_names = [
    "Royal Palm Resort",
    "Ocean Breeze Resort",
    "Mountain View Resort",
    "Lake Paradise Resort",
    "Sunset Bay Resort"
]

resort_addresses = [
    "Palermo, Italy",
    "Rome, Italy",
    "Milan, Italy",
    "Paris, France",
    "Barcelona, Spain"
]

hotel_names = [
    "Hotel Alpha",
    "Hotel Europa",
    "Hotel Beta",
    "Grand Palace Hotel",
    "Sea View Hotel",
    "Central Comfort Hotel",
    "Golden Horizon Hotel",
    "Blue Sky Hotel",
    "Royal Garden Hotel",
    "Urban Stay Hotel"
]

room_types = ["Suite", "Double", "Single", "Family", "Deluxe"]
room_sizes = ["Small", "Medium", "Large", "Extra Large"]

service_types = [
    "Massage", "Spa Treatment", "Sauna", "Facial Treatment", "Yoga",
    "Fitness Training", "Thermal Bath", "Aromatherapy", "Hair Treatment",
    "Physiotherapy", "Body Scrub", "Couples Massage"
]

pool_names = [
    "Blue Pool", "Sunset Pool", "Garden Pool", "Royal Pool",
    "Ocean Pool", "Palm Pool", "Crystal Pool"
]

social_platforms = [
    ("Instagram", "Instagram"),
    ("Facebook", "Facebook"),
    ("TikTok", "TikTok"),
    ("YouTube", "Video Platform"),
    ("X", "Microblogging")
]

stock_types = [
    "Technology", "Tourism", "Healthcare", "Finance", "Energy",
    "Real Estate", "Transport", "Retail", "Hospitality", "Manufacturing"
]

periods = ["1 day", "2 days", "3 days", "4 days", "5 days", "1 week", "2 weeks"]

seasons = [
    "Spring 2023", "Summer 2023", "Winter 2023",
    "Spring 2024", "Summer 2024", "Winter 2024",
    "Spring 2025", "Summer 2025", "Winter 2025"
]

# =====================================================
# HELPERS
# =====================================================

def sql_string(value):
    if value is None:
        return "NULL"
    return "'" + str(value).replace("'", "''") + "'"

def weighted_tourism_date():
    """
    Generates dates between 2023 and 2025.
    Summer months have the highest probability.
    """
    year = random.choice([2023, 2024, 2025])

    month = random.choices(
        population=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        weights=[3, 3, 4, 6, 8, 14, 18, 18, 10, 7, 5, 4],
        k=1
    )[0]

    if month == 2:
        day = random.randint(1, 28)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)

    return date(year, month, day)

def generate_age():
    return random.choices(
        population=list(range(18, 76)),
        weights=[
            3 if 26 <= age <= 45 else
            2 if 18 <= age <= 55 else
            1
            for age in range(18, 76)
        ],
        k=1
    )[0]

def business_season_from_date(dt):
    if dt.month in [6, 7, 8]:
        return "Summer"
    if dt.month in [12, 1, 2]:
        return "Winter"
    if dt.month in [3, 4, 5]:
        return "Spring"
    return "Autumn"

# =====================================================
# SQL GENERATION
# =====================================================

sql = []

sql.append("USE resort_operational_db;")
sql.append("SET FOREIGN_KEY_CHECKS = 0;")

truncate_order = [
    "PROVIDES",
    "FREE_ACCESS",
    "DISCOUNT_SERVICE",
    "DISCOUNT_ROOM",
    "FOLLOW_TABLE",
    "POOL_RENTAL",
    "SERVICE_RENTAL",
    "ROOM_RENTAL",
    "INVESTMENT",
    "PAYMENT",
    "SPECIAL_OFFER",
    "SOCIAL_MEDIA",
    "STOCK_VALUE",
    "VALUE_TABLE",
    "STOCK_MARKET_TITLE",
    "SPECIFIC_SERVICE",
    "SWIMMING_POOL",
    "WELLNESS_CENTER",
    "ROOM",
    "HOTEL",
    "RESORT",
    "PERSON"
]

for table in truncate_order:
    sql.append(f"TRUNCATE TABLE {table};")

sql.append("SET FOREIGN_KEY_CHECKS = 1;")

# =====================================================
# PERSON
# =====================================================

person_cfs = []
person_country_tracker = Counter()

for i in range(1, PERSON_COUNT + 1):
    cf = f"CF{i:05d}"
    person_cfs.append(cf)

    country = random.choice(countries)
    person_country_tracker[country] += 1

    city = cities_by_country[country]
    address = f"{city}, {country}"

    first = random.choice(first_names)
    last = random.choice(last_names)
    gender = random.choice(["Male", "Female"])
    age = generate_age()

    sql.append(
        "INSERT INTO PERSON (CF, Name, Address, Gender, Age) VALUES "
        f"({sql_string(cf)}, {sql_string(first + ' ' + last)}, "
        f"{sql_string(address)}, {sql_string(gender)}, {age});"
    )

# =====================================================
# RESORT
# =====================================================

for i in range(1, RESORT_COUNT + 1):
    sql.append(
        "INSERT INTO RESORT (ResortID, Name, Address) VALUES "
        f"({i}, {sql_string(resort_names[i - 1])}, {sql_string(resort_addresses[i - 1])});"
    )

# =====================================================
# HOTEL
# =====================================================

for i in range(1, HOTEL_COUNT + 1):
    resort_id = ((i - 1) % RESORT_COUNT) + 1
    sql.append(
        "INSERT INTO HOTEL (HotelID, Name, Address, ResortID) VALUES "
        f"({i}, {sql_string(hotel_names[i - 1])}, "
        f"{sql_string(resort_addresses[resort_id - 1])}, {resort_id});"
    )

# =====================================================
# ROOM
# =====================================================

for i in range(1, ROOM_COUNT + 1):
    hotel_id = random.randint(1, HOTEL_COUNT)
    room_type = random.choice(room_types)
    room_size = random.choice(room_sizes)

    base_price = {
        "Single": 80,
        "Double": 140,
        "Family": 210,
        "Suite": 280,
        "Deluxe": 350
    }[room_type]

    price = base_price + random.randint(0, 100)

    sql.append(
        "INSERT INTO ROOM (RoomID, Size, Type, Price, HotelID) VALUES "
        f"({i}, {sql_string(room_size)}, {sql_string(room_type)}, {price:.2f}, {hotel_id});"
    )

# =====================================================
# WELLNESS_CENTER
# =====================================================

for i in range(1, WELLNESS_CENTER_COUNT + 1):
    resort_id = ((i - 1) % RESORT_COUNT) + 1
    sql.append(
        "INSERT INTO WELLNESS_CENTER (WellnessCenterID, Name, Address, ResortID) VALUES "
        f"({i}, {sql_string('Wellness Center ' + str(i))}, "
        f"{sql_string(resort_addresses[resort_id - 1])}, {resort_id});"
    )

# =====================================================
# SWIMMING_POOL
# =====================================================

for i in range(1, SWIMMING_POOL_COUNT + 1):
    resort_id = random.randint(1, RESORT_COUNT)
    price = random.randint(25, 90)
    name = random.choice(pool_names) + f" {i}"

    sql.append(
        "INSERT INTO SWIMMING_POOL (SwimmingPoolID, Name, Address, Price, ResortID) VALUES "
        f"({i}, {sql_string(name)}, {sql_string(resort_addresses[resort_id - 1])}, "
        f"{price:.2f}, {resort_id});"
    )

# =====================================================
# SPECIFIC_SERVICE
# =====================================================

for i in range(1, SPECIFIC_SERVICE_COUNT + 1):
    wellness_id = random.randint(1, WELLNESS_CENTER_COUNT)
    service_type = random.choice(service_types)
    duration = random.choice([30, 45, 60, 75, 90, 120])
    price = duration * random.uniform(1.2, 2.5)

    sql.append(
        "INSERT INTO SPECIFIC_SERVICE (ServiceID, Type, Duration, Price, WellnessCenterID) VALUES "
        f"({i}, {sql_string(service_type)}, {duration}, {price:.2f}, {wellness_id});"
    )

# =====================================================
# STOCK_MARKET_TITLE
# =====================================================

for i in range(1, STOCK_MARKET_TITLE_COUNT + 1):
    sql.append(
        "INSERT INTO STOCK_MARKET_TITLE (StockMarketTitleID, Type) VALUES "
        f"({i}, {sql_string(stock_types[i - 1])});"
    )

# =====================================================
# VALUE_TABLE
# =====================================================

for i in range(1, VALUE_TABLE_COUNT + 1):
    amount = random.uniform(500, 6000)

    sql.append(
        "INSERT INTO VALUE_TABLE (ValueID, Amount) VALUES "
        f"({i}, {amount:.2f});"
    )

# =====================================================
# STOCK_VALUE
# =====================================================

for i in range(1, STOCK_VALUE_COUNT + 1):
    stock_id = random.randint(1, STOCK_MARKET_TITLE_COUNT)
    resort_id = random.randint(1, RESORT_COUNT)
    value_id = random.randint(1, VALUE_TABLE_COUNT)
    dt = weighted_tourism_date()
    changed = random.choice([0, 1])

    sql.append(
        "INSERT INTO STOCK_VALUE (StockValueID, StockMarketTitleID, ResortID, ValueID, `Date`, IsChanged) VALUES "
        f"({i}, {stock_id}, {resort_id}, {value_id}, {sql_string(dt)}, {changed});"
    )

# =====================================================
# SOCIAL_MEDIA
# =====================================================

social_media_resort = {}

for i in range(1, SOCIAL_MEDIA_COUNT + 1):
    resort_id = ((i - 1) % RESORT_COUNT) + 1
    social_media_resort[i] = resort_id

    platform_name, platform_type = random.choice(social_platforms)
    name = f"{resort_names[resort_id - 1].replace(' ', '')}_{platform_name}_{i}"

    sql.append(
        "INSERT INTO SOCIAL_MEDIA (SocialMediaID, Name, Type, ResortID) VALUES "
        f"({i}, {sql_string(name)}, {sql_string(platform_type)}, {resort_id});"
    )

# =====================================================
# SPECIAL_OFFER
# =====================================================

for i in range(1, SPECIAL_OFFER_COUNT + 1):
    sql.append(f"INSERT INTO SPECIAL_OFFER (SpecialOfferID) VALUES ({i});")

# =====================================================
# PAYMENT
# Each unique person makes 1 to 10 payments.
# Summer is strongly represented because dates are weighted.
# =====================================================

payment_id = 1
payments_per_person = {}

for cf in person_cfs:
    number_of_payments = random.randint(1, 10)
    payments_per_person[cf] = number_of_payments

    for _ in range(number_of_payments):
        resort_id = random.randint(1, RESORT_COUNT)
        dt = weighted_tourism_date()

        season = business_season_from_date(dt)

        if season == "Summer":
            amount = random.uniform(250, 1800)
        elif season == "Spring":
            amount = random.uniform(150, 1200)
        elif season == "Autumn":
            amount = random.uniform(120, 1000)
        else:
            amount = random.uniform(100, 900)

        sql.append(
            "INSERT INTO PAYMENT (PaymentID, CF, ResortID, `Date`, Amount) VALUES "
            f"({payment_id}, {sql_string(cf)}, {resort_id}, {sql_string(dt)}, {amount:.2f});"
        )

        payment_id += 1

PAYMENT_COUNT = payment_id - 1

# =====================================================
# INVESTMENT
# =====================================================

for i in range(1, INVESTMENT_COUNT + 1):
    cf = random.choice(person_cfs)
    stock_id = random.randint(1, STOCK_MARKET_TITLE_COUNT)
    dt = weighted_tourism_date()
    amount = random.uniform(500, 25000)
    duration = random.choice([6, 12, 18, 24, 36])

    sql.append(
        "INSERT INTO INVESTMENT (InvestmentID, CF, StockMarketTitleID, `Date`, Amount, Duration) VALUES "
        f"({i}, {sql_string(cf)}, {stock_id}, {sql_string(dt)}, {amount:.2f}, {duration});"
    )

# =====================================================
# ROOM_RENTAL
# =====================================================

for i in range(1, ROOM_RENTAL_COUNT + 1):
    cf = random.choice(person_cfs)
    room_id = random.randint(1, ROOM_COUNT)
    dt = weighted_tourism_date()
    period = random.choice(periods)

    sql.append(
        "INSERT INTO ROOM_RENTAL (RoomRentalID, CF, RoomID, `Date`, Period) VALUES "
        f"({i}, {sql_string(cf)}, {room_id}, {sql_string(dt)}, {sql_string(period)});"
    )

# =====================================================
# SERVICE_RENTAL
# =====================================================

for i in range(1, SERVICE_RENTAL_COUNT + 1):
    cf = random.choice(person_cfs)
    service_id = random.randint(1, SPECIFIC_SERVICE_COUNT)
    dt = weighted_tourism_date()

    sql.append(
        "INSERT INTO SERVICE_RENTAL (ServiceRentalID, CF, ServiceID, `Date`) VALUES "
        f"({i}, {sql_string(cf)}, {service_id}, {sql_string(dt)});"
    )

# =====================================================
# POOL_RENTAL
# =====================================================

for i in range(1, POOL_RENTAL_COUNT + 1):
    cf = random.choice(person_cfs)
    pool_id = random.randint(1, SWIMMING_POOL_COUNT)
    dt = weighted_tourism_date()

    sql.append(
        "INSERT INTO POOL_RENTAL (PoolRentalID, CF, SwimmingPoolID, `Date`) VALUES "
        f"({i}, {sql_string(cf)}, {pool_id}, {sql_string(dt)});"
    )

# =====================================================
# FOLLOW_TABLE
# =====================================================

used_follow_pairs = set()

for i in range(1, FOLLOW_COUNT + 1):
    while True:
        cf = random.choice(person_cfs)
        social_id = random.randint(1, SOCIAL_MEDIA_COUNT)
        key = (cf, social_id)

        if key not in used_follow_pairs:
            used_follow_pairs.add(key)
            break

    resort_id = social_media_resort[social_id]
    dt = weighted_tourism_date()

    sql.append(
        "INSERT INTO FOLLOW_TABLE (FollowID, CF, ResortID, SocialMediaID, StartingDate) VALUES "
        f"({i}, {sql_string(cf)}, {resort_id}, {social_id}, {sql_string(dt)});"
    )

# =====================================================
# DISCOUNT_ROOM
# =====================================================

for i in range(1, DISCOUNT_ROOM_COUNT + 1):
    offer_id = random.randint(1, SPECIAL_OFFER_COUNT)
    room_id = random.randint(1, ROOM_COUNT)
    period = random.choice(seasons)
    percentage = random.choice([5, 10, 15, 20, 25, 30])

    sql.append(
        "INSERT INTO DISCOUNT_ROOM (DiscountRoomID, SpecialOfferID, RoomID, Period, Percentage) VALUES "
        f"({i}, {offer_id}, {room_id}, {sql_string(period)}, {percentage:.2f});"
    )

# =====================================================
# DISCOUNT_SERVICE
# =====================================================

for i in range(1, DISCOUNT_SERVICE_COUNT + 1):
    offer_id = random.randint(1, SPECIAL_OFFER_COUNT)
    service_id = random.randint(1, SPECIFIC_SERVICE_COUNT)
    period = random.choice(seasons)
    percentage = random.choice([5, 10, 15, 20, 25])

    sql.append(
        "INSERT INTO DISCOUNT_SERVICE (DiscountServiceID, SpecialOfferID, ServiceID, Period, Percentage) VALUES "
        f"({i}, {offer_id}, {service_id}, {sql_string(period)}, {percentage:.2f});"
    )

# =====================================================
# FREE_ACCESS
# =====================================================

for i in range(1, FREE_ACCESS_COUNT + 1):
    offer_id = random.randint(1, SPECIAL_OFFER_COUNT)
    pool_id = random.randint(1, SWIMMING_POOL_COUNT)
    dt = weighted_tourism_date()
    duration = random.choice([1, 2, 3, 4, 5])

    sql.append(
        "INSERT INTO FREE_ACCESS (FreeAccessID, SpecialOfferID, SwimmingPoolID, `Date`, Duration) VALUES "
        f"({i}, {offer_id}, {pool_id}, {sql_string(dt)}, {duration});"
    )

# =====================================================
# PROVIDES
# =====================================================

for i in range(1, PROVIDES_COUNT + 1):
    social_id = random.randint(1, SOCIAL_MEDIA_COUNT)
    offer_id = random.randint(1, SPECIAL_OFFER_COUNT)
    cf = random.choice(person_cfs)

    sql.append(
        "INSERT INTO PROVIDES (ProvidesID, SocialMediaID, SpecialOfferID, CF) VALUES "
        f"({i}, {social_id}, {offer_id}, {sql_string(cf)});"
    )

# =====================================================
# VALIDATION QUERIES
# =====================================================

sql.append("")
sql.append("-- =====================================================")
sql.append("-- VALIDATION QUERIES")
sql.append("-- =====================================================")
sql.append("SELECT COUNT(*) AS TotalPersons FROM PERSON;")
sql.append("SELECT COUNT(*) AS TotalPayments FROM PAYMENT;")
sql.append("SELECT COUNT(*) AS TotalRoomRentals FROM ROOM_RENTAL;")
sql.append("SELECT COUNT(*) AS TotalServiceRentals FROM SERVICE_RENTAL;")
sql.append("SELECT COUNT(*) AS TotalPoolRentals FROM POOL_RENTAL;")
sql.append("SELECT COUNT(*) AS TotalInvestments FROM INVESTMENT;")
sql.append("SELECT COUNT(*) AS TotalFollows FROM FOLLOW_TABLE;")

# =====================================================
# WRITE FILE
# =====================================================

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(sql))

transaction_count = (
    PAYMENT_COUNT
    + ROOM_RENTAL_COUNT
    + SERVICE_RENTAL_COUNT
    + POOL_RENTAL_COUNT
    + INVESTMENT_COUNT
    + FOLLOW_COUNT
    + PROVIDES_COUNT
    + DISCOUNT_ROOM_COUNT
    + DISCOUNT_SERVICE_COUNT
    + FREE_ACCESS_COUNT
)

total_tuple_count = (
    PERSON_COUNT
    + RESORT_COUNT
    + HOTEL_COUNT
    + ROOM_COUNT
    + WELLNESS_CENTER_COUNT
    + SPECIFIC_SERVICE_COUNT
    + SWIMMING_POOL_COUNT
    + SOCIAL_MEDIA_COUNT
    + STOCK_MARKET_TITLE_COUNT
    + VALUE_TABLE_COUNT
    + STOCK_VALUE_COUNT
    + SPECIAL_OFFER_COUNT
    + transaction_count
)

print("Generated:", OUTPUT_FILE)
print("Unique persons:", PERSON_COUNT)
print("Payments generated:", PAYMENT_COUNT)
print("Total transaction/event rows:", transaction_count)
print("Approximate total operational tuples:", total_tuple_count)
print("Minimum payments per person:", min(payments_per_person.values()))
print("Maximum payments per person:", max(payments_per_person.values()))
print("Top 10 customer countries:")
for country, count in person_country_tracker.most_common(10):
    print(country, count)