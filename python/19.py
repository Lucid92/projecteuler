import datetime

sunday_count = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        # .weekday() == 6 is a sunday
        if datetime.date(year, month, 1).weekday() == 6:
            sunday_count += 1

print(sunday_count)