#project9_datetime_challenges.py
#📄 Description:
#Uses Python's datetime module to compute birthdays, double day, and how much older one person is than another.
print("name : Siddarth TR \n usn : 1AY24AI106 \n section : O ")
from datetime import datetime, timedelta

# 1. Current day
print("Today is:", datetime.today().strftime("%A"))

# 2. Time till next birthday
def next_birthday(birth_date):
    now = datetime.now()
    birthday = birth_date.replace(year=now.year)
    if birthday < now:
        birthday = birthday.replace(year=now.year + 1)
    diff = birthday - now
    print("Time until next birthday:", diff)

next_birthday(datetime(2000, 12, 25))

# 3. Double Day
def double_day(birth1, birth2):
    older, younger = sorted([birth1, birth2])
    diff = younger - older
    return younger + diff

print("Double Day:", double_day(datetime(2000, 1, 1), datetime(2004, 1, 1)))

# 4. More general version
def n_times_older_day(birth1, birth2, n):
    older, younger = sorted([birth1, birth2])
    days_apart = (younger - older).days
    double_day = younger + timedelta(days=days_apart // (n - 1))
    return double_day

print("Triple Day:", n_times_older_day(datetime(2000, 1, 1), datetime(2004, 1, 1), 3))
