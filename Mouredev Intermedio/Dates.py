### FECHAS  ###


from datetime import time
from datetime import datetime


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


now = datetime.now()
print_date(now)

year_2023 = datetime(year=2023, month=1, day=1)
print_date(year_2023)

current_time = time()
print_date(current_time)