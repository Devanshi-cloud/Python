def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)
greeting("Blake", "IT Support") 
print("------------------------------------------------------- 1")

def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum)) 
print("------------------------------------------------------- 2")

def convert_seconds(seconds):
    hours = seconds // 3600 #floor division
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result= convert_seconds(5000)
print(result)
print(type(result))
print("------------------------------------------------------- 3")

name = "Kay"
number = len(name) * 9

print("Hello " + name + ", Your lucky number is " + str(number))

name = "Cameron"
number = len(name) * 9

print("Hello " + name + ", Your lucky number is " + str(number))
print("------------------------------------------------------- 4")

def find_total_days (years, months, days):
    my_days = (years * 365) + (months*30) + days
    return my_days
print(find_total_days(2,5,23))
print("------------------------------------------------------- 5")

def convert_volume(fluid_ounce):
    ml = fluid_ounce* 29.5
    return ml
print("the volume in millimeters is " + str(convert_volume(2)))
print("The volume in millimeters is " + str(convert_volume(2)*2))
print("------------------------------------------------------- 6")

def get_remainder(x, y):
    
    if x == 0 or y == 0 or x == y:
        remainder = 0
    else:
        remainder = (x % y) / y
    return remainder

print("{:.2f}".format(get_remainder(10, 3)))
print("------------------------------------------------------- 7")

m = "big" > "small"
print(m)

number = 4
if number * 4 < 15:
    print(number / 4)
elif number < 5:
    print(number + 3)
else:
    print(number * 2 % 5)       
print("------------------------------------------------------- 8")
    
def difference(x, y):
    z = x - y
    return z
print(difference(5,3))    
print("------------------------------------------------------- 9")

q = ((10 >= 5*2) and (10 <= 5*2))
print(q)    
print("------------------------------------------------------- 10")

def hint_username(username):
    if len(username) < 3:
        print("invalid username. must be atleast 3 characters only")
    else:
        print("Valid statement")    
print(hint_username("So"))  
print("------------------------------------------------------- 11")

def is_even(number):
    if number % 2 == 0:
        return True
    return False  
print(is_even(5))   
print("------------------------------------------------------- 12")

print((3**2)==5)
print("------------------------------------------------------- 13")

def max_product(nums) :
    n = len(nums)
    res = nums[0]
    for i in range (n) :
        prod = nums[i]
        
        for j in range (i + 1, n):
            res = max(res, prod)
            prod = prod * nums[j]
            
        res = max(res, prod)
        
    return res
nums = [6, -3, -10, 0, 2]
print(max_product(nums))
print("------------------------------------------------------- 14")