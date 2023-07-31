# Check whether the string contains only digits or not

string = input("Please enter a word or number: ")

res = False

for letter in string:
    if letter == '1' or letter == '2' or letter == '3' or letter == '4' or letter == '5' or letter == '6' or letter == '7' or letter == '8' or letter == '9':
        res = True
    else:
        res = False
        break

print(res)