#! /usr/bin/env python

import pandas as pd
import datetime as dt
import os
import requests

## read the Data
#df = pd.read_json('data/weather/20241119_170405_athenry.json')
## Show
#df.head()

##Get teh current date and time
#filename = dt.datetime.now()
# Create a string from the current date and time.
#filename = filename.strftime("%Y%m%d_%H%M%S")
#filename = 'data/' + filename + ".csv"

# Save the data to a CSV file.
#df.to_csv(filename)


# Define the URL for the weather data
url = "https://prodapi.metweb.ie/observations/athenry/today"

# Generate filenames based on the current timestamp
timestamp = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
json_filename = f"data/weather/{timestamp}_athenry.json"
csv_filename = f"data/{timestamp}.csv"

# Download the JSON data and save it to a file
response = requests.get(url)
with open(json_filename, "w") as file:
    file.write(response.text)

# Read the JSON file into a pandas DataFrame and save as CSV
df = pd.read_json(json_filename)
df.to_csv(csv_filename, index=False)

print(f"Weather data saved: JSON -> {json_filename}, CSV -> {csv_filename}")
