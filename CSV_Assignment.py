import csv
import matplotlib.pyplot as plt
from datetime import datetime



#this is the death valley section
open_file2 = open("death_valley_2018_simple.csv", "r")

csv_file2 = csv.reader(open_file2, delimiter=",")

header_row2 = next(csv_file2)



col_dict2 = {}

for index, column_header2 in enumerate(header_row2):
    col_dict2[column_header2] = int(index)



highs2 = []
lows2 = []
dates2 = []


for row2 in csv_file2:
    try:
        high2 = int(row2[col_dict2.get("TMAX")])
        low2 = int(row2[col_dict2.get("TMIN")])
        current_date2 = datetime.strptime(row2[col_dict2.get("DATE")],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date2}")
    else:
        highs2.append(row2[col_dict2.get("TMAX")])
        lows2.append(row2[col_dict2.get("TMIN")])
        dates2.append(current_date2)



#create the figure
fig, ax = plt.subplots(2)

ax[0].plot(dates2, highs2, c="red", alpha=0.5)
ax[0].plot(dates2, lows2, c="blue", alpha=0.5)
ax[0].set_title("Daily High and Low Temp (2018)\nDeath Valley")




#this is the sitka weather section
open_file = open("sitka_weather_2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter=",")
header_row = next(csv_file)



col_dict = {}

for index, column_header in enumerate(header_row):
    col_dict[column_header] = int(index)



highs = []
lows = []
dates = []


for row in csv_file:
    try:
        high = int(row[col_dict.get("TMAX")])
        low = int(row[col_dict.get("TMIN")])
        current_date = datetime.strptime(row[col_dict.get("DATE")],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs.append(row[col_dict.get("TMAX")])
        lows.append(row[col_dict.get("TMIN")])
        dates.append(current_date)


ax[1].plot(dates, highs, c="red", alpha=0.5)
ax[1].plot(dates, lows, c="blue", alpha=0.5)
ax[1].set_title("Daily High and Low Temp (2018)\nSitka")



plt.show()