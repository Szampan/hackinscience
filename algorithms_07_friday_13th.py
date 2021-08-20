import datetime

today = datetime.date.today()
delta = datetime.timedelta(days=1)

day = today

while True:
    if day.weekday() == 4 and day.day == 13:
        print(day)
        break
    day += delta