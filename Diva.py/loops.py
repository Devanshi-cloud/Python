x = 0 
while x < 5:
    print("Not there yet, x= " + str(x))
    x = x + 1
print("x=" + str(x))
print("------------------------------------------------------- 1")

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
        
attempts(5)        
print("------------------------------------------------------- 2")

x = 1
sum = 0
while x < 10:
    sum += x
    x += 1
    
product = 1
while x < 10:
    product = product * x
    x += 1
    
print(sum, product)
print("------------------------------------------------------- 3")


def count_down(current):
    while current > 0:
        print(current)
        current -= 1
    print("zero!")
    
count_down(3)   
print("------------------------------------------------------- 4")

x = 8
if x != 0:
    while x % 2 == 0:
        x = x / 2     
        print (x) 
 
x = 10
print("------------------------------------------------------- 5")

while x % 2 == 0 or x != 0:   
    x = x / 2       
    print (x) 
    break
print("------------------------------------------------------- 6")
        
def print_range(start, end): 
    n = start
    while n <= end:
        print (n)
        n += 1

print_range(1, 3) 
print("------------------------------------------------------- 7")

multiplier = 1
result = multiplier*5
while result <= 50:
  print(result)
  multiplier += 1
  result = multiplier*5       
print("------------------------------------------------------- 8")

def count_factors(given_number):
  factor = 1
  count = 1
  if given_number == 0:
    return 0
  while factor < given_number:
    if given_number % factor == 0:
      count += 1
    factor += 1
  return count
 
print(count_factors(0)) # Count value will be 0
print(count_factors(3)) # Should count 2 factors (1x3)
print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8,
# and 4x6). 
print("------------------------------------------------------- 9")


for x in range(5):
    print(x)
print("------------------------------------------------------- 10")
    
friends = ['Tayllor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("hi " + friend)
print("------------------------------------------------------- 11")
    
    
values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1 
    
print("Total sum: " + str(sum) + " - Average: " + str(sum/length))
print("------------------------------------------------------- 12")

product = 1
for n in range(1,10):
    product = product * n
    
print(product)  
print("------------------------------------------------------- 13")

def to_celsius(x):
    return (x-32)*5/9

for x in range(0, 40, 10):
    print(x, to_celsius(x))
print("------------------------------------------------------- 14")
    
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
print("------------------------------------------------------- 15")
 
teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team) 
print("------------------------------------------------------- 16")
            
            
long_list = ("a", "b", "c", "d", "e")
for element1 in long_list:
    for element2 in long_list:
        print(element1, element2)    
print("------------------------------------------------------- 17")
        
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)
greet_friends("Barry")
greet_friends(['ace', 'kacy', 'chaos'])             
print("------------------------------------------------------- 18")
               
for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop") 
print("------------------------------------------------------- 19")

for n in range(12, 36, 6):
    print(n*2)
print("------------------------------------------------------- 20")

for n in range(6, 18+1, 3):
    print(n*2)    
print("------------------------------------------------------- 21")

for n in range(6, 18, 3):
    print(n*2)
print("------------------------------------------------------- 22")
    
for n in range(18+1):
    print(n**2)
print("------------------------------------------------------- 23")
    
for n in range(0, 18+1, 2):
    print(n*2)   
print("------------------------------------------------------- 24")
    
for n in range(19):
    if n % 2 == 0:
       print(n)   
print("------------------------------------------------------- 25")
    
for n in range(10):
    print(n+n)   
print("------------------------------------------------------- 26")

def count_by_10(end):
    count = ""
    for number in range(0, end+1, 10):
        count += str(number) + " "
    return count.strip() 
print(count_by_10(100))   
print("------------------------------------------------------- 27")


def matrix(initial_number, end_of_first_row):
    n1 = initial_number
    n2 = end_of_first_row+1
    for column in range(n1,n2):
        for row in range(n1, n2):
            print(column*row, end=" ")
        print()
matrix(1, 4)
print("------------------------------------------------------- 28")
        
number = 2
while number <= 13:
    print(number, end=" ")    
    number = number + 2   
print("------------------------------------------------------- 29")

def sequence(low, high):
    for x in range(2):
        for y in range(high, low-1, -1):
            if y == low:
                print(str(y))
            else:
                print(str(y), end=", ")
sequence(1, 3)
print("------------------------------------------------------- 30")

for sum in range(5):
    sum += sum
    print(sum)     
print("------------------------------------------------------- 31")

for outer_loop in range(2, 6+1):
    print("This is the outer loop iteration number " + str(outer_loop))
    for inner_loop in range(outer_loop):
        if inner_loop % 2 == 0:
           print(inner_loop)
print("------------------------------------------------------- 32")
           