"""date time in python"""
import datetime
import pytz

# Naive
d = datetime.date(2005, 6, 7)
tday = datetime.date.today()

print("weekday (monday=0,sunday=6)",tday.weekday())

print("weekday (monday=1,sunday=7)",tday.isoweekday())


datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
tdelta = datetime.timedelta(hours=100)

print("printing 100hrs after today's date ", tday + tdelta)

bday = datetime.date(2024, 5, 5)

till_bday = bday - tday

print("number of days till my birthday ",till_bday.days)

t = datetime.time(9, 30, 45, 100000)

dt = datetime.datetime.today()
dtnow = datetime.datetime.now()
#print(dt)
#print(dtnow)

dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)

dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

dt_calc = datetime.datetime.now()
calc_tz = pytz.timezone('GMT')
dt_calc = calc_tz.localize(dt_calc)
print(dt_calc.strftime('%B %d, %Y'))

DT = 'July 24, 2023'
dt = datetime.datetime.strptime(DT, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime
