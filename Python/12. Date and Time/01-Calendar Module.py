# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true


# Language: Python

# ========================
#         Solution
# ========================

import calendar

MONTH, DAY, YEAR = map(int, input().split())

print(calendar.day_name[calendar.weekday(YEAR, MONTH, DAY)].upper())
