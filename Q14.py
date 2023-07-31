# Find the occurence of a given character in the string

string = input("Please enter a word: ")
char = input("Please enter a character: ")

count = 0

for letter in string:
    if letter == char:
        count += 1
    
print("Count of given character in the word is:",count)