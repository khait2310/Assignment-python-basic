import datetime
from datetime import date, timedelta

temp_date = (date(date.today().year, 1, 1))
for i in range(7):
    temp_date += timedelta(days=1)
    if temp_date.isocalendar()[2] == 1: break
week = 0
while temp_date.year == 2022:
    week += 1
    print(temp_date, week)
    temp_date += timedelta(days=7)

