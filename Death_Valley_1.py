import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

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



import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,1)

ax[0].plot(dates, highs, c="red", alpha=0.5)
ax[0].plot(dates, lows, c="blue", alpha=0.5)

ax[0].title("Daily High and Low Temp (2018)\nDeath Valley", fontsize=16)
ax[0].xlabel("")
ax[0].ylabel("Temperature (F)", fontsize=16)
ax[0].tick_params(axis="both", labelsize = 16)

ax[0].fill_between(dates,highs,lows, facecolor='blue', alpha=0.1)

ax[0].autofmt_xdate()

plt.show()

'''
open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)



col_dict = {}

for index, column_header in enumerate(header_row):
    col_dict[column_header] = int(index)



highs = []
lows = []
dates = []

x = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(x)



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



import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

plt.title("Daily High and Low Temp (2018)\nSitka", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", labelsize = 16)

plt.fill_between(dates,highs,lows, facecolor='blue', alpha=0.1)

fig.autofmt_xdate()

plt.show()
'''