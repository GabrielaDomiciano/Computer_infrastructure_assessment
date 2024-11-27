#! /usr/bin/env python

import pandas as pd
import datetime as dt 

## read the Data
df = pd.read_json('/workspaces/Computer_infrastructure_assessment/data/weather/20241119_170405_athenry.json')
## Show
df.head()

##Get teh current date and time
#filename = dt.datetime.now()
# Create a string from the current date and time.
#filename = filename.strftime("%Y%m%d_%H%M%S")
#filename = 'data/' + filename + ".csv"

# Save the data to a CSV file.
#df.to_csv(filename)

