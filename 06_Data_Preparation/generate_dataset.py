import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

airlines = ["SriLankan Airlines", "Emirates", "Qatar Airways", "Singapore Airlines", "AirAsia"]
flight_types = ["Domestic", "International"]
terminals = ["T1", "T2", "T3"]
travel_classes = ["Economy", "Business", "First"]
passenger_types = ["Solo Traveler", "Family Traveler", "Business Traveler"]

records = []

start_date = datetime(2026, 1, 1)

for i in range(1, 5001):
    passenger_id = 100000 + i
    flight_id = random.choice(["UL225", "EK651", "QR665", "SQ469", "AK045"])
    airline = random.choice(airlines)
    flight_type = random.choice(flight_types)
    terminal = random.choice(terminals)
    travel_class = random.choice(travel_classes)
    passenger_type = random.choice(passenger_types)

    date = start_date + timedelta(days=random.randint(0, 180))
    arrival_time = date + timedelta(hours=random.randint(4, 23), minutes=random.randint(0, 59))

    check_in = random.randint(5, 35)
    security = random.randint(4, 30)
    immigration = random.randint(3, 25) if flight_type == "International" else 0
    boarding = random.randint(5, 25)
    baggage = random.randint(8, 35)

    total_time = check_in + security + immigration + boarding + baggage

    satisfaction = round(max(1, min(5, 5 - (total_time / 100) + random.uniform(-0.5, 0.5))), 1)
    missed_flight = "Yes" if total_time > 100 else "No"

    records.append([
        passenger_id, flight_id, airline, flight_type, terminal, arrival_time,
        check_in, security, immigration, boarding, baggage, total_time,
        satisfaction, missed_flight, travel_class, passenger_type, date.date()
    ])

columns = [
    "Passenger_ID", "Flight_ID", "Airline", "Flight_Type", "Terminal",
    "Arrival_Time", "Check_In_Wait_Minutes", "Security_Wait_Minutes",
    "Immigration_Wait_Minutes", "Boarding_Wait_Minutes",
    "Baggage_Claim_Minutes", "Total_Journey_Time",
    "Satisfaction_Score", "Missed_Flight", "Travel_Class",
    "Passenger_Type", "Date"
]

df = pd.DataFrame(records, columns=columns)

df.to_csv("05_Data/Raw_Data/airport_passenger_journey_raw.csv", index=False)

print("Dataset created successfully!")
print(df.head())