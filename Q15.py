# Check Palindrome or not

string = input("Please enter a word: ")

res = ''

for letter in string:
    res = letter+res

if res==string:
    print("The given string {} is a Palindrome".format(string))
else:
    print("The given string {} is not a Palindrome".format(string))