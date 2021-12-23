# Works with dates and times
# Importation of the datetime module
# Works with date
import datetime as dt
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
new_years_day = dt.date(2019,1,1)
memorial_day = dt.date(2019,5,27)
days_between = memorial_day - new_years_day
print(days_between)
print(type(days_between))
new_years_day = dt.date(2019,1,1)
duration = dt.timedelta(days=146)
print(new_years_day + duration)
memorial_day = dt.date(2019,5,27)
duration = dt.timedelta(days=146)
print(memorial_day - duration)

