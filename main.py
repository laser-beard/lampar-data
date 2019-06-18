import pandas
import locale
import sys
import lang

if sys.version_info[0] < 3:
        raise RuntimeError('Must be run using python 3.x')


locale.setlocale(locale.LC_ALL, "de_DE.utf8")

current_locale = locale.getlocale()[0][:2]

print(current_locale)

date = '7 mär, 2019'

a = date.split(' ')
day = a[0]
month = a[1][:3].lower()
year = a[2]
print(day, month, year)

# dates = ['05.12.1989', '8 jan 2019']
#
# parserd_dates = [pandas.to_datetime(d) for d in dates]
#
# print(parserd_dates)


print(lang.DATE_TABLE[current_locale])

for i in lang.DATE_TABLE[current_locale]:
    if month in i:
        print(i)
