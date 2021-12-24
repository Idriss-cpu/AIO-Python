# Works with dates and times
# Importation of the datetime module
# Works with date
# import dateutil tz
import datetime as dt
from dateutil.tz import gettz
print(dt.date.today())
# Store some other date in a variable
LAST_OF_TEENS = dt.date(2019, 12, 31)
print(LAST_OF_TEENS)
print(LAST_OF_TEENS.day)
print(LAST_OF_TEENS.month)
print(LAST_OF_TEENS.year)
print(f"{LAST_OF_TEENS:%A, %B %d, %Y}")
today = dt.date.today()
print(f"{today:%d/%m/%Y}")
print(f"{today:%d, %m, %Y}")
print(f"{today:%x}")
# Works with time
MIDNIGHT = dt.time()
print(MIDNIGHT)
print(type(MIDNIGHT))
almost_midnight = dt.time(23, 59, 59, 999999)
print(almost_midnight)
right_now = dt.datetime.now()
print(right_now)
new_years_day = dt.date(2019, 1, 1)
memorial_day = dt.date(2019, 5, 27)
days_between = memorial_day - new_years_day
print(days_between)
print(type(days_between))
new_years_day = dt.date(2019, 1, 1)
duration = dt.timedelta(days=146)
print(new_years_day + duration)
memorial_day = dt.date(2019, 5, 27)
duration = dt.timedelta(days=146)
print(memorial_day - duration)
# Working with time zones
here_now = dt.datetime.now()
utc_now = dt.datetime.utcnow()
time_difference = utc_now - here_now
print(f"My time    : {here_now:%I:%M:%p}")
print(f"UTC time   : {utc_now:%I:%M:%p} ")
print(f"Differnrce : {time_difference}")
event = dt.datetime(2020, 7, 4, 19, 0, 0)
# UTC time right now.
utc = dt.datetime.now(gettz('Etc/UTC'))
print(f"{utc:%A %D %I:%M %p %Z}")
# USA Estern time.
est = dt.datetime.now(gettz('America/New_York'))
print(f"{est:%A %D %I:%M %p %Z}")
# USA Central time.
cst = dt.datetime.now(gettz('America/Chicago'))
print(f"{cst:%A %D %I:%M %p %Z}")
# USA Mountain time.
mst = dt.datetime.now(gettz('America/Boise'))
print(f"{mst:%A %D %I:%M %p %Z}")
pst = dt.datetime.now(gettz('America/Los_Angeles'))
print(f"{pst:%A %D %I:%M %p %Z}")
