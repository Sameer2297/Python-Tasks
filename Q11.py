# Find the first non repeated character in the string

string = input("Please enter a word: ")

for i in range(len(string)):
    count = 0
    for j in range(len(string)):
        if string[i]==string[j]:
            count += 1
    if count == 1:
        print(string[i])
        break