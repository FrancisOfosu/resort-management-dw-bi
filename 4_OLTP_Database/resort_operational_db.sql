-- =====================================================
-- RESORT OPERATIONAL DATABASE
-- FULL IMPLEMENTATION SCRIPT
-- QUESTION 6
-- =====================================================

CREATE DATABASE IF NOT EXISTS resort_operational_db;

USE resort_operational_db;

-- =====================================================
-- 1. PERSON
-- =====================================================

CREATE TABLE PERSON (
    CF VARCHAR(30) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(200),
    Gender VARCHAR(20),
    Age INT
);

-- =====================================================
-- 2. RESORT
-- =====================================================

CREATE TABLE RESORT (
    ResortID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(200)
);

-- =====================================================
-- 3. HOTEL
-- =====================================================

CREATE TABLE HOTEL (
    HotelID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Address VARCHAR(200),
    ResortID INT NOT NULL,

    FOREIGN KEY (ResortID)
        REFERENCES RESORT(ResortID)
);

-- =====================================================
-- 4. ROOM
-- =====================================================

CREATE TABLE ROOM (
    RoomID INT AUTO_INCREMENT PRIMARY KEY,
    Size VARCHAR(50),
    Type VARCHAR(50),
    Price DECIMAL(10,2),
    HotelID INT NOT NULL,

    FOREIGN KEY (HotelID)
        REFERENCES HOTEL(HotelID)
);

-- =====================================================
-- 5. WELLNESS_CENTER
-- =====================================================

CREATE TABLE WELLNESS_CENTER (
    WellnessCenterID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Address VARCHAR(200),
    ResortID INT NOT NULL,

    FOREIGN KEY (ResortID)
        REFERENCES RESORT(ResortID)
);

-- =====================================================
-- 6. SWIMMING_POOL
-- =====================================================

CREATE TABLE SWIMMING_POOL (
    SwimmingPoolID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Address VARCHAR(200),
    Price DECIMAL(10,2),
    ResortID INT NOT NULL,

    FOREIGN KEY (ResortID)
        REFERENCES RESORT(ResortID)
);

-- =====================================================
-- 7. SPECIFIC_SERVICE
-- =====================================================

CREATE TABLE SPECIFIC_SERVICE (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,
    Type VARCHAR(100),
    Duration INT,
    Price DECIMAL(10,2),
    WellnessCenterID INT NOT NULL,

    FOREIGN KEY (WellnessCenterID)
        REFERENCES WELLNESS_CENTER(WellnessCenterID)
);

-- =====================================================
-- 8. STOCK_MARKET_TITLE
-- =====================================================

CREATE TABLE STOCK_MARKET_TITLE (
    StockMarketTitleID INT AUTO_INCREMENT PRIMARY KEY,
    Type VARCHAR(100)
);

-- =====================================================
-- 9. VALUE
-- =====================================================

CREATE TABLE VALUE_TABLE (
    ValueID INT AUTO_INCREMENT PRIMARY KEY,
    Amount DECIMAL(15,2)
);

-- =====================================================
-- 10. STOCK_VALUE
-- =====================================================

CREATE TABLE STOCK_VALUE (
    StockValueID INT AUTO_INCREMENT PRIMARY KEY,
    StockMarketTitleID INT NOT NULL,
    ResortID INT NOT NULL,
    ValueID INT NOT NULL,
    Date DATE,
    IsChanged BOOLEAN,

    FOREIGN KEY (StockMarketTitleID)
        REFERENCES STOCK_MARKET_TITLE(StockMarketTitleID),

    FOREIGN KEY (ResortID)
        REFERENCES RESORT(ResortID),

    FOREIGN KEY (ValueID)
        REFERENCES VALUE_TABLE(ValueID)
);

-- =====================================================
-- 11. SOCIAL_MEDIA
-- =====================================================

CREATE TABLE SOCIAL_MEDIA (
    SocialMediaID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Type VARCHAR(100),
    ResortID INT NOT NULL,

    FOREIGN KEY (ResortID)
        REFERENCES RESORT(ResortID)
);

-- =====================================================
-- 12. SPECIAL_OFFER
-- =====================================================

CREATE TABLE SPECIAL_OFFER (
    SpecialOfferID INT AUTO_INCREMENT PRIMARY KEY
);

-- =====================================================
-- 13. PAYMENT
-- =====================================================

CREATE TABLE PAYMENT (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
    CF VARCHAR(30) NOT NULL,
    ResortID INT NOT NULL,
    Date DATE,
    Amount DECIMAL(10,2),

    FOREIGN KEY (CF)
        REFERENCES PERSON(CF),

    FOREIGN KEY (ResortID)
        REFERENCES RESORT(ResortID)
);

-- =====================================================
-- 14. INVESTMENT
-- =====================================================

CREATE TABLE INVESTMENT (
    InvestmentID INT AUTO_INCREMENT PRIMARY KEY,
    CF VARCHAR(30) NOT NULL,
    StockMarketTitleID INT NOT NULL,
    Date DATE,
    Amount DECIMAL(15,2),
    Duration INT,

    FOREIGN KEY (CF)
        REFERENCES PERSON(CF),

    FOREIGN KEY (StockMarketTitleID)
        REFERENCES STOCK_MARKET_TITLE(StockMarketTitleID)
);

-- =====================================================
-- 15. ROOM_RENTAL
-- =====================================================

CREATE TABLE ROOM_RENTAL (
    RoomRentalID INT AUTO_INCREMENT PRIMARY KEY,
    CF VARCHAR(30) NOT NULL,
    RoomID INT NOT NULL,
    Date DATE,
    Period VARCHAR(100),

    FOREIGN KEY (CF)
        REFERENCES PERSON(CF),

    FOREIGN KEY (RoomID)
        REFERENCES ROOM(RoomID)
);

-- =====================================================
-- 16. SERVICE_RENTAL
-- =====================================================

CREATE TABLE SERVICE_RENTAL (
    ServiceRentalID INT AUTO_INCREMENT PRIMARY KEY,
    CF VARCHAR(30) NOT NULL,
    ServiceID INT NOT NULL,
    Date DATE,

    FOREIGN KEY (CF)
        REFERENCES PERSON(CF),

    FOREIGN KEY (ServiceID)
        REFERENCES SPECIFIC_SERVICE(ServiceID)
);

-- =====================================================
-- 17. POOL_RENTAL
-- =====================================================

CREATE TABLE POOL_RENTAL (
    PoolRentalID INT AUTO_INCREMENT PRIMARY KEY,
    CF VARCHAR(30) NOT NULL,
    SwimmingPoolID INT NOT NULL,
    Date DATE,

    FOREIGN KEY (CF)
        REFERENCES PERSON(CF),

    FOREIGN KEY (SwimmingPoolID)
        REFERENCES SWIMMING_POOL(SwimmingPoolID)
);

-- =====================================================
-- 18. FOLLOW
-- =====================================================

CREATE TABLE FOLLOW_TABLE (
    FollowID INT AUTO_INCREMENT PRIMARY KEY,
    CF VARCHAR(30) NOT NULL,
    ResortID INT NOT NULL,
    SocialMediaID INT NOT NULL,
    StartingDate DATE,

    FOREIGN KEY (CF)
        REFERENCES PERSON(CF),

    FOREIGN KEY (ResortID)
        REFERENCES RESORT(ResortID),

    FOREIGN KEY (SocialMediaID)
        REFERENCES SOCIAL_MEDIA(SocialMediaID)
);

-- =====================================================
-- 19. DISCOUNT_ROOM
-- =====================================================

CREATE TABLE DISCOUNT_ROOM (
    DiscountRoomID INT AUTO_INCREMENT PRIMARY KEY,
    SpecialOfferID INT NOT NULL,
    RoomID INT NOT NULL,
    Period VARCHAR(100),
    Percentage DECIMAL(5,2),

    FOREIGN KEY (SpecialOfferID)
        REFERENCES SPECIAL_OFFER(SpecialOfferID),

    FOREIGN KEY (RoomID)
        REFERENCES ROOM(RoomID)
);

-- =====================================================
-- 20. DISCOUNT_SERVICE
-- =====================================================

CREATE TABLE DISCOUNT_SERVICE (
    DiscountServiceID INT AUTO_INCREMENT PRIMARY KEY,
    SpecialOfferID INT NOT NULL,
    ServiceID INT NOT NULL,
    Period VARCHAR(100),
    Percentage DECIMAL(5,2),

    FOREIGN KEY (SpecialOfferID)
        REFERENCES SPECIAL_OFFER(SpecialOfferID),

    FOREIGN KEY (ServiceID)
        REFERENCES SPECIFIC_SERVICE(ServiceID)
);

-- =====================================================
-- 21. FREE_ACCESS
-- =====================================================

CREATE TABLE FREE_ACCESS (
    FreeAccessID INT AUTO_INCREMENT PRIMARY KEY,
    SpecialOfferID INT NOT NULL,
    SwimmingPoolID INT NOT NULL,
    Date DATE,
    Duration INT,

    FOREIGN KEY (SpecialOfferID)
        REFERENCES SPECIAL_OFFER(SpecialOfferID),

    FOREIGN KEY (SwimmingPoolID)
        REFERENCES SWIMMING_POOL(SwimmingPoolID)
);

-- =====================================================
-- 22. PROVIDES
-- =====================================================

CREATE TABLE PROVIDES (
    ProvidesID INT AUTO_INCREMENT PRIMARY KEY,
    SocialMediaID INT NOT NULL,
    SpecialOfferID INT NOT NULL,
    CF VARCHAR(30) NOT NULL,

    FOREIGN KEY (SocialMediaID)
        REFERENCES SOCIAL_MEDIA(SocialMediaID),

    FOREIGN KEY (SpecialOfferID)
        REFERENCES SPECIAL_OFFER(SpecialOfferID),

    FOREIGN KEY (CF)
        REFERENCES PERSON(CF)
);

-- =====================================================
-- END OF FULL IMPLEMENTATION SCRIPT
-- =====================================================discount_service