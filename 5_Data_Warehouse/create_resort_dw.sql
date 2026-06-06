DROP DATABASE IF EXISTS resort_dw;
CREATE DATABASE resort_dw;
USE resort_dw;

CREATE TABLE DIM_DATE (
    DateID INT AUTO_INCREMENT PRIMARY KEY,
    FullDate DATE NOT NULL UNIQUE,
    DayOfWeek VARCHAR(20),
    MonthNumber INT,
    MonthName VARCHAR(20),
    QuarterNumber INT,
    YearNumber INT,
    BusinessSeason VARCHAR(20)
);

CREATE TABLE DIM_CUSTOMER (
    CustomerDimID INT AUTO_INCREMENT PRIMARY KEY,
    CF VARCHAR(30) NOT NULL UNIQUE,
    Name VARCHAR(100),
    Gender VARCHAR(20),
    Age INT,
    AgeGroup VARCHAR(20),
    City VARCHAR(100),
    Country VARCHAR(100)
);

CREATE TABLE DIM_RESORT (
    ResortDimID INT AUTO_INCREMENT PRIMARY KEY,
    SourceResortID INT NOT NULL UNIQUE,
    ResortName VARCHAR(100),
    ResortAddress VARCHAR(200),
    ResortCity VARCHAR(100),
    ResortCountry VARCHAR(100)
);

CREATE TABLE DIM_HOTEL (
    HotelDimID INT AUTO_INCREMENT PRIMARY KEY,
    SourceHotelID INT NOT NULL UNIQUE,
    HotelName VARCHAR(100),
    HotelAddress VARCHAR(200),
    HotelCity VARCHAR(100),
    HotelCountry VARCHAR(100),
    ResortDimID INT NOT NULL,
    FOREIGN KEY (ResortDimID) REFERENCES DIM_RESORT(ResortDimID)
);

CREATE TABLE DIM_ROOM (
    RoomDimID INT AUTO_INCREMENT PRIMARY KEY,
    SourceRoomID INT NOT NULL UNIQUE,
    RoomSize VARCHAR(50),
    RoomType VARCHAR(50),
    RoomPrice DECIMAL(10,2),
    HotelDimID INT NOT NULL,
    FOREIGN KEY (HotelDimID) REFERENCES DIM_HOTEL(HotelDimID)
);

CREATE TABLE FACT_PAYMENT (
    PaymentFactID INT AUTO_INCREMENT PRIMARY KEY,
    SourcePaymentID INT NOT NULL UNIQUE,
    DateID INT NOT NULL,
    CustomerDimID INT NOT NULL,
    ResortDimID INT NOT NULL,
    Amount DECIMAL(10,2),
    PaymentCount INT DEFAULT 1,
    FOREIGN KEY (DateID) REFERENCES DIM_DATE(DateID),
    FOREIGN KEY (CustomerDimID) REFERENCES DIM_CUSTOMER(CustomerDimID),
    FOREIGN KEY (ResortDimID) REFERENCES DIM_RESORT(ResortDimID)
);

CREATE TABLE FACT_ROOM_RENTAL (
    RoomRentalFactID INT AUTO_INCREMENT PRIMARY KEY,
    SourceRoomRentalID INT NOT NULL UNIQUE,
    DateID INT NOT NULL,
    CustomerDimID INT NOT NULL,
    RoomDimID INT NOT NULL,
    HotelDimID INT NOT NULL,
    ResortDimID INT NOT NULL,
    Period VARCHAR(100),
    RentalDays INT,
    RoomPrice DECIMAL(10,2),
    RentalRevenue DECIMAL(12,2),
    RentalCount INT DEFAULT 1,
    FOREIGN KEY (DateID) REFERENCES DIM_DATE(DateID),
    FOREIGN KEY (CustomerDimID) REFERENCES DIM_CUSTOMER(CustomerDimID),
    FOREIGN KEY (RoomDimID) REFERENCES DIM_ROOM(RoomDimID),
    FOREIGN KEY (HotelDimID) REFERENCES DIM_HOTEL(HotelDimID),
    FOREIGN KEY (ResortDimID) REFERENCES DIM_RESORT(ResortDimID)
);