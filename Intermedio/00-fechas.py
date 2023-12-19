print("\n***Modulo Dates (datetime)***\n")

from datetime import datetime

#imprimir fecha y hora actual.
now = datetime.now()
print(now)#2023-12-19 16:41:14.884022

print("\n")
#imprimir datos separados
print(now.year)#2023
print(now.month)#12
print(now.day)#19
print(now.hour)#16
print(now.minute)#44
print(now.second)#33

print("\n")

#representacion unica de un tiempo
timestamp = now.timestamp()
print(timestamp)#1703000819.574182

print("\n")

#personalizar fecha
year_2023 = datetime(2023,1,1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(year_2023)

print("\n")

#modulo time
from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print("\n")

#Modulo date
from datetime import date

#creando una fecha con el sistema
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)


#creando una fecha manualmente
current_date = date(2023,11,19)

print(current_date)

print("\n")

#modificar fecha
current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

print("\n")

year_2023 = datetime(2024,1,1)

#calcular diferencia entre una fecha y otra
diff =year_2023 - now
print(diff)

print("\n")

#Modulo timedelta
from datetime import timedelta

#se trabaja con franjas de tiempo
start_timedelta = timedelta(200, 100, 100 , weeks = 10)
end_timedelta = timedelta(300, 100, 100 , weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

print("\n")