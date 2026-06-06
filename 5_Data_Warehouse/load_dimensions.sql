USE resort_dw;

INSERT INTO DIM_DATE
(FullDate, DayOfWeek, MonthNumber, MonthName, QuarterNumber, YearNumber, BusinessSeason)
SELECT DISTINCT
    d.FullDate,
    DAYNAME(d.FullDate),
    MONTH(d.FullDate),
    MONTHNAME(d.FullDate),
    QUARTER(d.FullDate),
    YEAR(d.FullDate),
    CASE
        WHEN MONTH(d.FullDate) IN (6,7,8) THEN 'Summer'
        WHEN MONTH(d.FullDate) IN (12,1,2) THEN 'Winter'
        WHEN MONTH(d.FullDate) IN (3,4,5) THEN 'Spring'
        ELSE 'Autumn'
    END AS BusinessSeason
FROM (
    SELECT `Date` AS FullDate FROM resort_operational_db.PAYMENT
    UNION
    SELECT `Date` AS FullDate FROM resort_operational_db.ROOM_RENTAL
) d
WHERE d.FullDate IS NOT NULL;

INSERT INTO DIM_CUSTOMER
(CF, Name, Gender, Age, AgeGroup, City, Country)
SELECT
    CF,
    Name,
    Gender,
    Age,
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 55 THEN '46-55'
        WHEN Age BETWEEN 56 AND 65 THEN '56-65'
        ELSE '65+'
    END AS AgeGroup,
    TRIM(SUBSTRING_INDEX(Address, ',', 1)) AS City,
    TRIM(SUBSTRING_INDEX(Address, ',', -1)) AS Country
FROM resort_operational_db.PERSON;

INSERT INTO DIM_RESORT
(SourceResortID, ResortName, ResortAddress, ResortCity, ResortCountry)
SELECT
    ResortID,
    Name,
    Address,
    TRIM(SUBSTRING_INDEX(Address, ',', 1)) AS ResortCity,
    TRIM(SUBSTRING_INDEX(Address, ',', -1)) AS ResortCountry
FROM resort_operational_db.RESORT;

INSERT INTO DIM_HOTEL
(SourceHotelID, HotelName, HotelAddress, HotelCity, HotelCountry, ResortDimID)
SELECT
    h.HotelID,
    h.Name,
    h.Address,
    TRIM(SUBSTRING_INDEX(h.Address, ',', 1)) AS HotelCity,
    TRIM(SUBSTRING_INDEX(h.Address, ',', -1)) AS HotelCountry,
    dr.ResortDimID
FROM resort_operational_db.HOTEL h
JOIN DIM_RESORT dr
    ON h.ResortID = dr.SourceResortID;

INSERT INTO DIM_ROOM
(SourceRoomID, RoomSize, RoomType, RoomPrice, HotelDimID)
SELECT
    r.RoomID,
    r.Size,
    r.Type,
    r.Price,
    dh.HotelDimID
FROM resort_operational_db.ROOM r
JOIN DIM_HOTEL dh
    ON r.HotelID = dh.SourceHotelID;