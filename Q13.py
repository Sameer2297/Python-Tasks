# Count the number of vowels and consonants in the given word

string = input("Please enter a word: ")

count_of_vowels = 0

count_of_consonants = 0

for letter in string:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        count_of_vowels += 1
    else:
        count_of_consonants += 1
    
print("The number of vowels in the given word are:",count_of_vowels)
print("The number of consonants in the given word are:",count_of_consonants)