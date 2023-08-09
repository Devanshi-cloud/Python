x = ["Now", "we", "are", "cooking!"]
print(type(x))
print("------------------------------------------------------- 1")

print(x)
print("------------------------------------------------------- 2")

print(len(x))
print("------------------------------------------------------- 3")

print("are" in x)
print("------------------------------------------------------- 4")

print("Today" in x)
print("------------------------------------------------------- 5")

print(x[0])
print("------------------------------------------------------- 6")

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing
print("------------------------------------------------------- 7")

fruits = ["pineapples", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)
print("------------------------------------------------------- 8")

fruits.insert(0, "Orange")
print(fruits)
print("------------------------------------------------------- 9")

fruits.insert(25, "Peach")
print(fruits)
print("------------------------------------------------------- 10")

fruits.remove("Melon")
print(fruits)
print("------------------------------------------------------- 11")

fruits.pop(3)
print(fruits)
print("------------------------------------------------------- 12")

fullname = ('Grace', 'M', 'Hopper')
print(fullname)
print("------------------------------------------------------- 13")

def file_size(file_info):
	name , type, size= file_info
	return("{:.2f}".format(size / 1024))
print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
print("------------------------------------------------------- 14")

animals = ["lion," "zebra", "dolphin", "monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
    
print("Total characters: {}, Average length {}".format(chars,chars/len(animals)))
print("------------------------------------------------------- 15")

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))
print("------------------------------------------------------- 16") 

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result
    
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
print("------------------------------------------------------- 17")

multiples = []
for x in range(1, 11):
    multiples.append(x*7)
print(multiples)    
print("------------------------------------------------------- 18")

multiples = [x * 7 for x in range(1,11)]
print(multiples)
print("------------------------------------------------------- 19")

languages = ["Python", "perl", "Ruby", "Go", "Java", "C++"]
lengths = [len(language) for language in languages]
print(lengths)
print("------------------------------------------------------- 20")

z = [x for x in range(0, 101) if x % 3 == 0]
print(z)
print("------------------------------------------------------- 21")

def odd_numbers(n):
    return [x for x in range(n + 1) if x % 2 == 1]

print(odd_numbers(5))  
# Should print [1, 3, 5]
print(odd_numbers(10)) 
# Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) 
# Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  
# Should print [1]
print(odd_numbers(-1)) 
# Should print []
print("------------------------------------------------------- 22")

### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines 
# of code into one line:
print([x*2 for x in range(1,11)]) 



### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,11):
    my_list.append(x*2)
print(my_list)
print("------------------------------------------------------- 23")

### List Comprehension with Conditional Statement
print("List comprehension result:")

# The following list comprehension compacts multiple lines 
# of code into one line:
print([ x for x in range(1,101) if x % 10 == 0 ])

### Long form for loop with nested if-statement
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1,101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)
print("------------------------------------------------------- 24")

# The "years" list is given with existing elements. 
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]


# The variable "updated_years" is initialized as a list data type 
# using empty square brackets []. This list will hold the new list
# with the updated years. 
updated_years = []

# The for loop checks each "year" element in the list "years".
for year in years:

    # The if-statement checks if the "year" element ends with the 
    # substring "2023". 
    if year.endswith("2023"):

        # If True, then a temporary variable "new" will hold the 
        # modified "year" element where the "2023" substring is 
        # replaced with the substring "2024".
        new = year.replace("2023","2024")

        # Then, the list "updated_years" is appended with the changed
        # element held in the temporary variable "new".
        updated_years.append(new)
        
    # If False, the original "year" element will be appended to the 
    # the "updated_years" list unchanged.
    else:
        updated_years.append(year)


print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]
print("------------------------------------------------------- 23")

# accepts two integer variables through the function’s parameters.
def squares(start, end):
    
# The list comprehension calculates the square of a variable integer 
# "n", where "n" ranges from the "start" to "end" variables inclusively.
# To be inclusive in a range(), add +1 to the end of range variable.
    return [n*n for n in range(start,end+1)] 


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("------------------------------------------------------- 24")

# The "years" list is given with existing elements.
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The list comprehension below creates a new list "updated_years" to
# hold the command to replace the "2023" substring of the "year"
# element with the substring "2024". This action will be executed if
# the last 4 indices of the "year" string is equal to the substring
# "2023". If false (else), the "year" element will be included in the
# new list "updated_years" unchanged.
updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]


print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]
print("------------------------------------------------------- 25")

def change_string(given_string):

# Initialize "new_string" as a string data type by using empty quotes.
    new_string = ""
    # Split the "given_string" into a "new_list", with each "element"
    # holding an individual word from the string.
    new_list = given_string.split()

    # The for loop iterates over each "element" in the "new_list".
    for element in new_list:

        # Convert the list into a "new_string" by using the assignment
        # operator += to concatenate the following items: 
        # + Each list "element" (starting at index position [1:]), 
        # + a dash "-", 
        # + append the first character of the "element" (using the index 
        # [0]) to the end of the "element", and finally,
        # + a space " " to separate each "element" in the "new_string".
        new_string += element[1:] + "-"  + element[0] + " "

    # Return the list that has been converted back into a string.
    return new_string


print(change_string("1one 2two 3three 4four 5five")) 
# Should print "one-1 two-2 three-3 four-4 five-5"  
print("------------------------------------------------------- 26")

def list_elements(list_name, elements):

    # This task can be completed in a single line of code. The 
    # concatenation of strings, "list_name", and the list "elements" can
    # occur on the return line. In this case, the string "The " is added 
    # to the "list_name", plus the string " list includes: ", then the
    # "elements" are joined using a comma to separate each element of the 
    # list.
    return "The " + list_name + " list includes: " + ", ".join(elements)


print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"])) 
# Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"
print("------------------------------------------------------- 27")

def guest_list(guests):

    for guest in guests:
        name, age, job = guest
    print("{} is {} years old and works as {}.".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
print("------------------------------------------------------- 28")

print("dictionary")
file_count = {"jpg":10,"txt":14, "csv":2, "py":23}
print(file_count)
print("------------------------------------------------------- 29")

print(file_count["txt"])
print("------------------------------------------------------- 29")

print("jpg" in file_count)
print("------------------------------------------------------- 30")

print("html" in file_count)
print("------------------------------------------------------- 31")

file_count["cfg"] = 8
print(file_count)
print("------------------------------------------------------- 32")

file_count["csv"] = 17
print(file_count)
print("------------------------------------------------------- 33")

del file_count["cfg"]
print(file_count)
print("------------------------------------------------------- 34")

file_count = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_count:
    print(extension)
print("------------------------------------------------------- 35")

cool_beasts = {"octopus":"tentacles", "dolphins":"fins", "rhino":"horns"}
for animal, parts in cool_beasts.items():
    print("{} have {}".format(animal, parts))
print("------------------------------------------------------- 36") 

for ext, amount in file_count.items():
    print("There are {} files with the .{} extension".format(amount, ext))
print("------------------------------------------------------- 37")

file_count.keys()
dict_keys= (['jpg', 'csv', 'py'])
for keys in file_count.keys():
    print(keys)
print("------------------------------------------------------- 38") 

file_count.values()
dict_values= ([10, 14, 2, 23])
for value in file_count.values():
    print(value)
print("------------------------------------------------------- 39") 

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result  
print(count_letters("aaaa"))
print(count_letters("tenants"))
print(count_letters("a long string with a lot of letters"))
print("------------------------------------------------------- 40")

pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"], "cats": ["Persian", "Scottish Fold", "Siberian"], "rabbits": ["Angora", "Holland Lop", "Harlequin"]}  
print(pet_dictionary.get("dogs", 0))
# Should print ['Yorkie', 'Collie', 'Bulldog']
print("------------------------------------------------------- 41")

pet_list  = ["Yorkie", "Collie", "Bulldog", "Persian", "Scottish Fold", "Siberian", "Angora", "Holland Lop", "Harlequin"]
print(pet_list[0:3])
# Should print ['Yorkie', 'Collie', 'Bulldog']
print("------------------------------------------------------- 42")

# This function returns the total time, with minutes represented as 
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day. 
def sum_server_use_time(Server):
    
    # Initialize the variable as a float data type, which will be used
    # to hold the sum of the total hours and minutes of server usage by
    # end users in a day.
    total_use_time = 0.0

    # Iterate through the "Server" dictionary’s key and value items 
    # using a for loop.
    for key,value in Server.items():

        # For each end user key, add the associated time value to the
        # total sum of all end user use time.
        total_use_time += Server[key]
        
    # Round the return value and limit to 2 decimal places.
    return round(total_use_time, 2)  

FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

print(sum_server_use_time(FileServer)) # Should print 20.1
print("------------------------------------------------------- 43")

# This function receives a dictionary, which contains common employee 
# last names as keys, and a list of employee first names as values. 
# The function generates a new list that contains each employees’ full
# name (First_name Last_Name). For example, the key "Garcia" with the 
# values ["Maria", "Hugo", "Lucia"] should be converted to a list 
# that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].


def list_full_names(employee_dictionary):
    # Initialize the "full_names" variable as a list data type using
    # empty [] square brackets.  
    full_names = []

    # The outer for loop iterates through each "last_name" key and 
    # associated "first_name" values, in the "employee_dictionary" items.
    for last_name, first_names in employee_dictionary.items():

        # The inner for loop iterates over each "first_name" value in 
        # the list of "first_names" for one "last_name" key at a time.
        for first_name in first_names:

            # Append the new "full_names" list with the "first_name" value
            # concatenated with a space " ", and the key "last_name". 
            full_names.append(first_name+" "+last_name)
            
    # Return the new "full_names" list once the outer for loop has 
    # completed all iterations. 
    return(full_names)


print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']
print("------------------------------------------------------- 44")

# This function receives a dictionary, which contains resource 
# categories (keys) with a list of available resources (values) for a 
# company’s IT Department. The resources belong to multiple categories.
# The function should reverse the keys and values to show which 
# categories (values) each resource (key) belongs to. 


def invert_resource_dict(resource_dictionary):
    # Initialize a "new_dictionary" variable as a dict data type using
    # empty {} curly brackets. 
    new_dictionary = {}
    # The outer for loop iterates through each "resource_group" and 
    # associated "resources" in the "resource_dictionary" items.
    for resource_group, resources in resource_dictionary.items():
        # The inner for loop iterates over each "resource" value in 
        # the list of "resources" for one "resource_group" key at a time.
        for resource in resources:
            # The if-statement checks if the current "resource" value has 
            # been appended as a key to the "new_dictionary" yet.
            if resource in new_dictionary:
                # If True, then append the "resource_group" as a value to the
                # "resource", which is now the key.
                new_dictionary[resource].append(resource_group)
            # If False (else), then add the "resource" as a new key with the 
            # "resource_group" as a value for that key.
            else:
                new_dictionary[resource] = [resource_group]
    # Return the new dictionary once the outer for loop has completed  
    # all iterations.
    return(new_dictionary)


print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}
print("------------------------------------------------------- 45")
