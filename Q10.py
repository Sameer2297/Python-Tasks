# Print duplicates in the string

string = input("Please enter a word: ")

dups = {}

for i in range(len(string)):
    count = 0
    for j in range(len(string)):
        if string[i]==string[j]:
            count += 1
    if count > 1:
        dups[string[i]] = count

res = ''

for pair in dups:
    res += pair[0]+","

print(res)