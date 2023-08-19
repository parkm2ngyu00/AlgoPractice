import datetime
import sys

x, y = map(int, sys.stdin.readline().split())

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

result = days[datetime.date(2007, x, y).weekday()]

print(result)
