name = "DIVA"
color = 'red'
print ("name: " + name + " favorite color: " + color)
print("------------------------------------------------------- 1")

print ("example" * 3)
print("------------------------------------------------------- 2")

print(len(name))
print("------------------------------------------------------- 3")

print(name[3])
print("------------------------------------------------------- 4")

print(name[-1])
print("------------------------------------------------------- 5")

print(name[0:3])
print("------------------------------------------------------- 6")

print(name[3:])
print("------------------------------------------------------- 7")

print(name[:3])
print("------------------------------------------------------- 8")

#explain (name[::-1])?
print(name[::-1])
print("------------------------------------------------------- 9")

#explain (name[::-2])?
print(name[::-2])
print("------------------------------------------------------- 10")

#explain (name[::-3])?
print(name[::2])
print("------------------------------------------------------- 11")

#explain (name[::-4])?
print(name[::-3])
print("------------------------------------------------------- 12")

#explain new_message = message[0:2] + "l" + message[3:]?
message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)
print("------------------------------------------------------- 13")

pets= "Cats and Dogs n dogs & cats"
print(pets.index("and"))
print("------------------------------------------------------- 14")

print(pets.count("Dogs"))
print("------------------------------------------------------- 15")

print(pets.split())
print("------------------------------------------------------- 16")

print(pets.split("s"))
print("------------------------------------------------------- 17")

print(pets.split("s")[1])
print("------------------------------------------------------- 18")

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return(new_email)
    return email

print(replace_domain('devanshijaiswal@gmail.com', 'gmail.com','shs.com'))
print("------------------------------------------------------- 19")

print(" yes no ".strip())
print("------------------------------------------------------- 20")

print(" no yes ".lstrip())
print("------------------------------------------------------- 21")

print(" no ".rstrip())
print("------------------------------------------------------- 22")

print(" ".join(['Cats', 'and', 'Dogs', 'n', 'dogs', '&', 'cats']))
print("------------------------------------------------------- 23")

print("Hello {0}, your lucky color is {1} & lucky no. is {2}".format(name, color, len(name)*3))
print("------------------------------------------------------- 24")

#what is the final price by 9% tax on $10?
price = 10
with_tax = price * 1.09
print("Base price: ${:.2f}. With 9% Tax: ${:.2f}".format(price, with_tax))
print("------------------------------------------------------- 25")

def to_celsius(x):
    return (x - 32) * 5/9

#explain {:>6.2f}?
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
print("------------------------------------------------------- 26")

def to_fahrenheit(x):
    return (x * 9/5) + 32

for x in range(0,101,10):
    print("{:>3} C | {:>6.2f} F".format(x, to_fahrenheit(x)))
print("------------------------------------------------------- 27")

def mirrored_string(my_string):
    forward = ""
    backward = ""
    for character in my_string:
        if character.isalpha():
            forward += character
            backward = character + backward
    if forward.lower() == backward.lower():
        return True
    else:
        return False
    
print(mirrored_string("12 Noon"))
print(mirrored_string("Was it a car or a cat"))
print(mirrored_string("eve, madam Eve"))
print(mirrored_string("divid"))
print("------------------------------------------------------- 28")

def replace_date(schedule, old_date, new_date):
    if schedule.endswith(old_date):
        p = len(old_date)
        #explain new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)?
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
        return new_schedule
    return schedule
print(replace_date("Last year's annual report will be released in March 2023", "2023", "2024")) 
print(replace_date("In April, the CEO will hold a conference", "April", "May")) 
print(replace_date("The convention is scheduled for October", "October", "June")) 
print("------------------------------------------------------- 29")

schedule = "Monday, Tuesday, Wednesday, Thursday, Friday, Friday"
old_date = "Friday"
new_date = "Saturday"

new_schedule = schedule[:-len(old_date)] + schedule[-len(old_date):].replace(old_date, new_date)

print(new_schedule)
print("------------------------------------------------------- 30")

def car_listing(car_prices):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.
    for car, price in car_prices.items():
        result += "A {} costs {} dollars\n".format(car, price) # Use a string method to format the required string. 
    return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
print("------------------------------------------------------- 31")

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])
print("------------------------------------------------------- 32")

music_genres = ["rock", "pop", "country"]
print(music_genres.append("blues"))
print(music_genres)
print("------------------------------------------------------- 33")

teacher_names = {"Math": "Aniyah Cook", "Science": "Ines Bisset", "Engineering": "Wayne Branon"}
print(teacher_names.values())
print("------------------------------------------------------- 34")

