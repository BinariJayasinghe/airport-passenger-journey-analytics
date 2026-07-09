-- 1. Passenger count by airline
SELECT Airline,
       COUNT(*) AS Passenger_Count
FROM airport_passenger_journey
GROUP BY Airline
ORDER BY Passenger_Count DESC;

-- 2. Average journey time by airline
SELECT Airline,
       ROUND(AVG(Total_Journey_Time),2) AS Avg_Journey_Time
FROM airport_passenger_journey
GROUP BY Airline
ORDER BY Avg_Journey_Time DESC;

-- 3. Average satisfaction by passenger type
SELECT Passenger_Type,
       ROUND(AVG(Satisfaction_Score),2) AS Avg_Satisfaction
FROM airport_passenger_journey
GROUP BY Passenger_Type;

-- 4. Delay category distribution
SELECT Delay_Category,
       COUNT(*) AS Passenger_Count
FROM airport_passenger_journey
GROUP BY Delay_Category
ORDER BY Passenger_Count DESC;

-- 5. Average wait times across airport processes
SELECT
    ROUND(AVG(Check_In_Wait_Minutes),2) AS Avg_CheckIn,
    ROUND(AVG(Security_Wait_Minutes),2) AS Avg_Security,
    ROUND(AVG(Immigration_Wait_Minutes),2) AS Avg_Immigration,
    ROUND(AVG(Boarding_Wait_Minutes),2) AS Avg_Boarding,
    ROUND(AVG(Baggage_Claim_Minutes),2) AS Avg_Baggage_Claim
FROM airport_passenger_journey;