# Import libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# Show current directory
print("Current working directory:", os.getcwd())

# Load dataset
file_path =(r"C:\Users\ambru\PycharmProjects\uber-raw-data-sep14.csv")

df = pd.read_csv(file_path)

# Preview data
print(df.head())

# Convert 'Date/Time' to datetime and extract components
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['Hour'] = df['Date/Time'].dt.hour
df['Day'] = df['Date/Time'].dt.day
df['Weekday'] = df['Date/Time'].dt.dayofweek
df['Month'] = df['Date/Time'].dt.month

# Visualization: Trips by Hour
plt.figure(figsize=(10,6))
sns.countplot(x='Hour', hue='Hour', data=df, palette='viridis', legend=False)
plt.title("Trips by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Number of Trips")
plt.grid(True)
plt.show()

# Visualization: Trips by Day of the Week
plt.figure(figsize=(10,6))
sns.countplot(x='Weekday', hue='Weekday', data=df, palette='coolwarm', legend=False)
plt.title("Trips by Day of Week")
plt.xlabel("Day of the Week (0=Monday)")
plt.ylabel("Number of Trips")
plt.grid(True)
plt.show()

# Visualization: Trips by Uber Base
plt.figure(figsize=(10,6))
sns.countplot(x='Base', hue='Base', data=df, palette='Set2', legend=False)
plt.title("Trips by Base")
plt.xlabel("Base")
plt.ylabel("Number of Trips")
plt.grid(True)
plt.show()

# Heatmap: Trips by Hour and Day
hour_day = df.groupby(['Day','Hour']).size().unstack()
plt.figure(figsize=(12,6))
sns.heatmap(hour_day, cmap='YlGnBu')
plt.title("Heatmap of Trips by Day and Hour")
plt.xlabel("Hour")
plt.ylabel("Day")
plt.show()

# Save to SQLite database
conn = sqlite3.connect("uber_data.db")
df.to_sql("uber_trips", conn, if_exists='replace', index=False)

# Optional: Load it back and preview
df_db = pd.read_sql("SELECT * FROM uber_trips", conn)
print(df_db.head())

# Close connection
conn.close()



