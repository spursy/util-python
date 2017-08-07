#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from enum import Enum, unique
Month = Enum('Enum', (('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')))

for name, member in Month.__members__.items():
    print(name, ' => ', member, member.value )

@unique
class weekDay(Enum):
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Sun = 7

print(weekDay.Mon)
print(weekDay.Mon.value)