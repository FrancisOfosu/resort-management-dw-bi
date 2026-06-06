USE resort_dw;

INSERT INTO FACT_PAYMENT
(SourcePaymentID, DateID, CustomerDimID, ResortDimID, Amount, PaymentCount)
SELECT
    p.PaymentID,
    dd.DateID,
    dc.CustomerDimID,
    dr.ResortDimID,
    p.Amount,
    1
FROM resort_operational_db.PAYMENT p
JOIN DIM_DATE dd
    ON p.`Date` = dd.FullDate
JOIN DIM_CUSTOMER dc
    ON p.CF = dc.CF
JOIN DIM_RESORT dr
    ON p.ResortID = dr.SourceResortID;

INSERT INTO FACT_ROOM_RENTAL
(SourceRoomRentalID, DateID, CustomerDimID, RoomDimID, HotelDimID, ResortDimID,
 Period, RentalDays, RoomPrice, RentalRevenue, RentalCount)
SELECT
    rr.RoomRentalID,
    dd.DateID,
    dc.CustomerDimID,
    drom.RoomDimID,
    dh.HotelDimID,
    dr.ResortDimID,
    rr.Period,

    CASE
        WHEN rr.Period LIKE '%week%' THEN CAST(SUBSTRING_INDEX(rr.Period, ' ', 1) AS UNSIGNED) * 7
        WHEN rr.Period LIKE '%day%' THEN CAST(SUBSTRING_INDEX(rr.Period, ' ', 1) AS UNSIGNED)
        ELSE 1
    END AS RentalDays,

    drom.RoomPrice,

    drom.RoomPrice *
    CASE
        WHEN rr.Period LIKE '%week%' THEN CAST(SUBSTRING_INDEX(rr.Period, ' ', 1) AS UNSIGNED) * 7
        WHEN rr.Period LIKE '%day%' THEN CAST(SUBSTRING_INDEX(rr.Period, ' ', 1) AS UNSIGNED)
        ELSE 1
    END AS RentalRevenue,

    1
FROM resort_operational_db.ROOM_RENTAL rr
JOIN DIM_DATE dd
    ON rr.`Date` = dd.FullDate
JOIN DIM_CUSTOMER dc
    ON rr.CF = dc.CF
JOIN DIM_ROOM drom
    ON rr.RoomID = drom.SourceRoomID
JOIN DIM_HOTEL dh
    ON drom.HotelDimID = dh.HotelDimID
JOIN DIM_RESORT dr
    ON dh.ResortDimID = dr.ResortDimID;