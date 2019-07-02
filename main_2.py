import locale
from datetime import datetime
import re
import lang

locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')  # the ru locale is installed
current_locale = locale.getlocale()[0][:2]

date_strings = ['Мар 9., 2019', 'Сен. 01, 2019', '2019-Апрель-26', '5 März 2020', ]

# date_formats = '%B %d, %Y', '%b %d, %Y', '%Y-%B-%d', '%B. %d, %Y'

dates = []

for date_str in date_strings:
    date = re.findall(r'\w+', date_str)
    # print(date)
    for i in date:
        try:
            if len(i) == 4 and int(i) >= 2019:
                year = i
                print(year)
            elif (len(i) == 1 or 2) and (int(i) <= 31):
                day = i
                print(i)
            elif i:
                # TODO extract MONTH!
                print(current_locale)
                for m in lang.DATE_TABLE[current_locale]:
                    if i[0:3].lower() in m:
                        month = m
                        print(month)
        except:
            pass




# for date_str in date_strings:
#     print(re.findall(r'\d{4}', date_str))


# print(re.findall(r"[\w]+", date_str))

#     for date_fmt in date_formats:
#         try:
#             dates.append(datetime.strptime(date_str, date_fmt).date())
#         except ValueError:
#             pass
#         else:
#             break
#     else:
#         print('failed to parse %r' % date_str)
#
# output_date_strings = list(map(str, dates))
# print(output_date_strings)
