def greetings(name, department):
    print("My name is "+ name)
    print("You are a part of "+ department)
greetings("Devanshi", "IT")    
print("------------------------------------------------------- 1")

def triangle(base, height):
    return base*height/2
area_1= triangle(24, 4)
area_2= triangle(30, 6)
sum = area_1 + area_2
print("The sum of both areas is: "+str(sum))
print("------------------------------------------------------- 2")

#how to convert hours and minutes to seconds?
def convert_to_seconds(hours, minutes, sec):
    return hours*3600 + minutes*60 + sec
second = convert_to_seconds(3, 40, 43)
print(second)
print("------------------------------------------------------- 3")

#how to convert seconds to hours, minutes and remaining seconds?
def convert_to_hours_and_minutes(seconds):
    hours = seconds//3600
    minutes = (seconds - hours*3600)//60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
result = convert_to_hours_and_minutes(5000)
print(result)
print("------------------------------------------------------- 4")

#how to convert years, month and days to total days?
def convert_to_days(years, months, days):
    return years*365 + months*30 + days
total_days = convert_to_days(2, 3, 4)
print(total_days)
print("------------------------------------------------------- 5")

#how to convert days to years, months, day?
def convert_to_years_months_days(days):
    years = days//365
    months = (days - years*365)//30
    days = days - years * 365 - months * 30
    return years, months, days
result_2 = convert_to_years_months_days(35)
print(result_2)
print("------------------------------------------------------- 6")

import datetime

# Create a datetime.date object from the number of days.
days = 35
date = datetime.date.fromordinal(days)

# Get the year, month, and day.
year = date.year
month = date.month
day = date.day

print(day, month, year)
print("------------------------------------------------------- 7")

# how to get remainder of a number?
def get_remainder(num, div):
    if num == 0 or div ==0 or num == div:
        remainder = 0
    else:
        remainder = (num % div) / div
    return remainder

print("{:.2f}".format(get_remainder(10,3)))
print("------------------------------------------------------- 8")

print("hello")
print("world")
print("------------------------------------------------------- 9")


