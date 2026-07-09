# Airport Passenger Journey Dataset Design

## Dataset Purpose

The dataset is designed to capture passenger movement across major airport touchpoints to support operational analysis, bottleneck identification, and KPI monitoring.

---

## Granularity

One record represents one passenger journey through the airport.

---

## Proposed Columns

| Column Name | Description |
|------------|-------------|
| Passenger_ID | Unique passenger identifier |
| Flight_ID | Flight number |
| Airline | Airline name |
| Flight_Type | Domestic or International |
| Terminal | Airport terminal |
| Arrival_Time | Passenger arrival time |
| Check_In_Wait_Minutes | Check-in waiting time |
| Security_Wait_Minutes | Security waiting time |
| Immigration_Wait_Minutes | Immigration processing time |
| Boarding_Wait_Minutes | Boarding waiting time |
| Baggage_Claim_Minutes | Baggage claim time |
| Total_Journey_Time | Total airport journey duration |
| Satisfaction_Score | Passenger satisfaction rating |
| Missed_Flight | Yes or No |
| Travel_Class | Economy, Business, First |
| Passenger_Type | Solo, Family, Business Traveler |
| Date | Journey date |