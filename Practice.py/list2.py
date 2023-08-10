x = ['Cats', 'and', 'Dogs', 'n', 'dogs', '&', 'cats']
print(len(x))
print("------------------------------------------------------- 1")

print(x[4])
print("------------------------------------------------------- 2")

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)
print("------------------------------------------------------- 3")

fruits.remove("Apple")
print(fruits)
print("------------------------------------------------------- 4")

# explain print(fruits.pop())?
print(fruits.pop())
print("------------------------------------------------------- 5")

fruits.insert(0, "Orange")
print(fruits)
print("------------------------------------------------------- 6")

fruits.reverse()
print(fruits)
print("------------------------------------------------------- 7")

fruits.sort()
print(fruits)
print("------------------------------------------------------- 8")

fruits.insert(25, "Peach")
print(fruits)
print("------------------------------------------------------- 9")

print(fruits.pop(3))
print(fruits)
print("------------------------------------------------------- 10")

fruits[2] = "Strawberry"
print(fruits)
print("------------------------------------------------------- 11")

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
    
print("Total Characters: {}, Average length: {}".format(chars, chars/len(animals)))
print("------------------------------------------------------- 12")

winners = ["Diva", "Dylan", "Ava"] #give example of enumerate?
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))
print("------------------------------------------------------- 13")

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email)) #explain result.append("{} <{}>".format(name, email))?
    return result
print(full_emails([("devanshi@gmail.com", "devanshi jaiswal"), ("diva@gmail.com", "diva jazz")]))
print("------------------------------------------------------- 14")

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Iterate over the list using `enumerate()`
for index, number in enumerate(numbers):
    # Print the index and the number
    print(index, number)
print("------------------------------------------------------- 15")

multiples = []
for x in range(1, 11):
    multiples.append(x*7)
print(multiples)
print("------------------------------------------------------- 16")

languages = ["Python", "Perl", "Ruby", "go", "Java", "C++"]
lengths = [len(language) for language in languages]
print(lengths)
print("------------------------------------------------------- 17")

z = [x for x in range(0, 101) if x % 8 == 0]
print(z)
print("------------------------------------------------------- 18")


#print(squares(0, 10)) Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100] how?
def squares(start, end):
    squares = []
    for x in range(start, end + 1):
        square = x * x
        squares.append(square)
    return squares


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("------------------------------------------------------- 19")

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years = []
for year in years:
    if year.endswith("2023"):
        new = year.replace("2023","2024")
        updated_years.append(new)
    else:
        updated_years.append(year)
print(updated_years) 
print("------------------------------------------------------- 21")

def squares(start, end):
    return [n*n for n in range(start,end+1)] 
print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("------------------------------------------------------- 22")

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]
print(updated_years) 
print("------------------------------------------------------- 23")

def change_string(given_string):
    new_string = ""
    new_list = given_string.split()
    for element in new_list:
        new_string += element[1:] + "-"  + element[0] + " "
    return new_string
print(change_string("1one 2two 3three 4four 5five")) 
print("------------------------------------------------------- 24")

def list_elements(list_name, elements):
    return "The " + list_name + " list includes: " + ", ".join(elements)
print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"])) 
print("------------------------------------------------------- 25")