import pandas as pd

df = pd.read_csv("05_Data/Cleaned_Data/airport_passenger_journey_cleaned.csv")

print("\n===== AIRPORT JOURNEY ANALYTICS KPIs =====")

print("\nTotal Passengers:")
print(len(df))

print("\nAverage Total Journey Time:")
print(round(df["Total_Journey_Time"].mean(), 2), "minutes")

print("\nAverage Satisfaction Score:")
print(round(df["Satisfaction_Score"].mean(), 2))

print("\nPassenger Type Distribution:")
print(df["Passenger_Type"].value_counts())

print("\nPeak vs Off-Peak Traffic:")
print(df["Peak_Period"].value_counts())

print("\nDelay Category Distribution:")
print(df["Delay_Category"].value_counts())

print("\nTop Airlines:")
print(df["Airline"].value_counts())

print("\nTop Terminals:")
print(df["Terminal"].value_counts())

print("\nFlight Type Distribution:")
print(df["Flight_Type"].value_counts())
print("\nAverage Wait Times")

wait_columns = [
    "Check_In_Wait_Minutes",
    "Security_Wait_Minutes",
    "Immigration_Wait_Minutes",
    "Boarding_Wait_Minutes",
    "Baggage_Claim_Minutes"
]
print("\n===== AVERAGE WAIT TIMES =====")

wait_columns = [
    "Check_In_Wait_Minutes",
    "Security_Wait_Minutes",
    "Immigration_Wait_Minutes",
    "Boarding_Wait_Minutes",
    "Baggage_Claim_Minutes"
]

for column in wait_columns:
    print(f"{column}: {round(df[column].mean(), 2)} minutes")
