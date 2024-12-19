import datetime
x = datetime.datetime.now()
print("Current date and time:", x)

print("Current year:", x.year)

print(x.strftime("Month of the year:%B"))

print(x.strftime("Week number of the year:%U"))

print(x.strftime("Weekday of the week:%A"))

print(x.strftime("Day of year:%j"))

print(x.strftime("Day of the month:%d"))

print(x.strftime("Day of week:%w"))
