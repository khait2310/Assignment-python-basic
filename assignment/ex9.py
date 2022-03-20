import datetime
from datetime import date

cur_date = date.today()
cur_date_time = datetime.datetime.now()
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")


print("Current date time: ", cur_date_time)
print("Current year:", cur_date.year)
print("Current month:", cur_date.month)
print("Current week of year: ", cur_date.isocalendar()[1])
print("Current weekday: ", weekDays[cur_date.weekday()])
print("Current day of year: ", cur_date.timetuple().tm_yday)
print("Current day of month:", cur_date.day)
print("Current day of week: ", cur_date.isocalendar()[2])
