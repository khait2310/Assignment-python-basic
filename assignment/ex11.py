import datetime
from datetime import date, timedelta

temp_date = date.today()
for i in range(7):
    temp_date -= timedelta(days=1)
    if temp_date.isocalendar()[2] == 5: break
print('Last Friday: ', temp_date)

