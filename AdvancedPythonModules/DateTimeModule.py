import datetime

print('**************TIME INFO**************************')

mytime = datetime.time(13,20,1,15)
print(type(mytime))         #<class 'datetime.time'>
print(mytime)               #13:20:01.000015
print(mytime.hour)          #13
print(mytime.minute)        #20
print(mytime.second)        #1
print(mytime.microsecond)   #5

print('**************DATE INFO**************************')

today = datetime.date.today()
print(today)            #2020-09-13
print(today.year)       #2020
print(today.month)      #9
print(today.day)        #13
print(today.ctime())    #Sun Sep 13 00:00:00 2020

print('**************DATE TIME INFO**************************')

from datetime import datetime

mydatetime = datetime(2021,11,8,14,20,1)
print(mydatetime)                           #2021-11-08 14:20:01
mydatetime = mydatetime.replace(year=2020)
print(mydatetime)                           #2020-11-08 14:20:01

print('****************************************')

#Arithmetic on DATE info

from datetime import date
date1 = date(2020,11,8)
date2 = date(2020,8,8)
result = date1-date2
print(type(result))
print(result)
print(result.days)
print(result.seconds)

print('****************************************')

#Arithmetic on DATETIME info

datetime1 = datetime(2020,11,8,22,0)
datetime2 = datetime(2020,8,8,13,30)
result = datetime1-datetime2
print(type(result))
print(result)
print(result.days)
print(result.seconds)