import pandas as pd

raw_path = "05_Data/Raw_Data/airport_passenger_journey_raw.csv"
cleaned_path = "05_Data/Cleaned_Data/airport_passenger_journey_cleaned.csv"

df = pd.read_csv(raw_path)

# Remove duplicates
df = df.drop_duplicates()

# Convert date/time columns
df["Arrival_Time"] = pd.to_datetime(df["Arrival_Time"])
df["Date"] = pd.to_datetime(df["Date"])

# Add useful analysis columns
df["Hour"] = df["Arrival_Time"].dt.hour
df["Month"] = df["Date"].dt.month
df["Day_Name"] = df["Date"].dt.day_name()

df["Peak_Period"] = df["Hour"].apply(
    lambda x: "Peak" if x in [6, 7, 8, 16, 17, 18, 19] else "Off-Peak"
)

df["Delay_Category"] = df["Total_Journey_Time"].apply(
    lambda x: "High Delay" if x > 90 else "Moderate Delay" if x > 60 else "Low Delay"
)

# Save cleaned dataset
df.to_csv(cleaned_path, index=False)

print("Cleaned dataset created successfully!")
print(df.head())
print(df.info())