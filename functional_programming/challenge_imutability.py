"""
CHALLENGE:
Using a calendar library, get all months with 31 days
"""

from calendar import mdays, month_name
from functools import reduce

months_31 = filter(lambda month: mdays[month] == 31, range(1, 13))
months_name = map(lambda month: month_name[month], months_31)
months = reduce(lambda all, name_month: f'{all}\n- {name_month}', months_name, 'Months with 31 days:')
print(months)
