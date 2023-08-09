name = "devanshi"
color = 'red'
place = "Kanpur"
pet = ""
pet = "loooooooooooong cat"
print("Name: " + name + ", Favourite color: " + color)
print("------------------------------------------------------- 1")
print("eg" * 3)
print("------------------------------------------------------- 2")
print (len(pet))
print("------------------------------------------------------- 3")

name = "Jaylen"
print(name[1])
print("------------------------------------------------------- 4")
print(name[0])
print("------------------------------------------------------- 5")

text = "Random string with a lot of characters"
print(text[-1])
print("------------------------------------------------------- 6")
print(text[-2])
print("------------------------------------------------------- 7")

color = "Mangosteen"
print(color[1:4])
print("------------------------------------------------------- 8")
print(color[5:])
print("------------------------------------------------------- 9")
print(color[:5])
print("------------------------------------------------------- 10")
print(color[:5] + color[5:])
print("------------------------------------------------------- 11")

message = "A king string with a silly typo"
message = "A long string with a silly typo"
print(message)
print("------------------------------------------------------- 12")

pets = "Cats & Dogs"
print(pets.index("&"))
print("------------------------------------------------------- 13")
print("Dragons" in pets)
print("------------------------------------------------------- 14")
print("Cats" in pets)
print("------------------------------------------------------- 15")

print("Mountains".upper())
print("------------------------------------------------------- 16")
print(" yes ".strip())
print("------------------------------------------------------- 17")
print(" yes".lstrip())
print("------------------------------------------------------- 18")
print("My name is Devanshi".count("s"))
print("------------------------------------------------------- 19")
print("Forest".endswith("rest"))
print("------------------------------------------------------- 20")
print("12345".isnumeric())
print("------------------------------------------------------- 21")
print("....".join(["This", "is", "a", "phrase", "joined", "by", "dots"]))
print("------------------------------------------------------- 22")
print("This is another example".split())
print("------------------------------------------------------- 23")

name = "manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
print("------------------------------------------------------- 24")
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))
print("------------------------------------------------------- 25")

price = 7.5
with_tax = price *1.09
print(price, with_tax)
print("------------------------------------------------------- 26")

print("Base price: ${:.2f}. with tax: ${:.2f}".format(price, with_tax))
print("------------------------------------------------------- 27")

def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    input_string = input_string.replace(" ",'')
    input_string = input_string.lower()
    for letter in input_string:
        if letter in input_string:
            if letter != " ":
                new_string = new_string + letter
                reverse_string = letter + reverse_string
    if reverse_string == new_string:
        return True
        
    return False
    
print(is_palindrome("Never Odd or Even"))
print("------------------------------------------------------- 28")

print(is_palindrome("anc"))
print("------------------------------------------------------- 29")

print(is_palindrome("radar"))    
print("------------------------------------------------------- 30")

def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence 
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        i = len( sentence.split())
        new_sentence = sentence[:-len(old)] + new
        return new_sentence

    # Return the original sentence if there is no match 
    return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print("------------------------------------------------------- 31")

print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print("------------------------------------------------------- 32")

print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print("------------------------------------------------------- 33")

print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"      
print("------------------------------------------------------- 34")

sentence = input('Enter a Sentence: ').lower()
words = sentence.split()

for i, word in enumerate(words):
    
    '''
    if first letter is a vowel
    '''
    if word[0] in 'aeiou':
        words[i] = words[i]+ "ay"
    else:
        '''
        else get vowel position and postfix all the consonants 
        present before that vowel to the end of the word along with "ay"
        '''
        has_vowel = False
        
        for j, letter in enumerate(word):
            if letter in 'aeiou':
                words[i] = word[j:] + word[:j] + "ay"
                has_vowel = True
                break

        #if the word doesn't have any vowel then simply postfix "ay"
        if(has_vowel == False):
            words[i] = words[i]+ "ay"

pig_latin = ' '.join(words)
print("Pig Latin: ",pig_latin)  
print("------------------------------------------------------- 35")

def main():
    words = str(input("Input Sentence:")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
    print ()

main()
print("------------------------------------------------------- 36")

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print("------------------------------------------------------- 37")

a,b = input().split()
print(int(a)+int(b))
print("------------------------------------------------------- 38")
