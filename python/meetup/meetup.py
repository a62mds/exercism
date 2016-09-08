#!/usr/bin/env python
from calendar import day_name
from calendar import monthcalendar
from datetime import date

####
# Strategy:
# int(year) int(month) str(day) str(occurrence)
#                         |
#                         V
#                      int(dow) str(occurrence)     day of week
#                      \___________ __________/
#                                  V
#                                  |
#                                  V
# int(year) int(month) int(dow) int(woo)            week of occurrence
#                      \_______ _______/
#                              V
#                             /
#                            V
# int(year) int(month)  int(dom)                    day of month
# \_____________ ______________/
#               V
#               |
#               V
#     date(year, month, dom)

num_in_week = {day_name[n] : n for n in range(len(day_name))}

def get_week(monthcal, day, pred):
    for week in monthcal:
        if pred(week, day):
            return monthcal.index(week)

is_in_month = lambda date_of, day: date_of[num_in_week[day]] != 0
def week_of_first_occurrence(monthcal, day):
    return get_week(monthcal, day, is_in_month)

def week_of_occurrence(num):
    return lambda monthcal, day: week_of_first_occurrence(monthcal, day) + num

def week_of_last_occurrence(monthcal, day):
    return len(monthcal)-1 - get_week(list(reversed(monthcal)), day, is_in_month)

is_in_teens = lambda date_of, day: date_of[num_in_week[day]] in range(13, 20)
def teenth_week(monthcal, day):
    return get_week(monthcal, day, is_in_teens)    

week_of = {'1st' : week_of_first_occurrence,
           '2nd' : week_of_occurrence(1),
           '3rd' : week_of_occurrence(2),
           '4th' : week_of_occurrence(3),
           '5th' : week_of_occurrence(4),
           'last' : week_of_last_occurrence,
           'teenth' : teenth_week}

def meetup_day(year, month, day, occurrence):
    monthcal = monthcalendar(year, month)
    week_num = week_of[occurrence](monthcal, day)
    day_num  = num_in_week[day]
    return date(year, month, monthcal[week_num][day_num])
