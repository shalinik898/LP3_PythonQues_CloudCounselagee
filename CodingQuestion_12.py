"""
CODING QUESTIONS:11
Write a Python program to get a week number.
Sample Date :
2015, 6, 16
Expected Output :
25
"""

import datetime

date_entry = input('Enter a date in YYYY-MM-DD format\n')
year, month, day = map(int, date_entry.split(','))
print(datetime.date(year,month,day).isocalendar()[1])
