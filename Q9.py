# Check whether the two words are anagrams to each other or not

str1 = input("Please enter a word: ")
str2 = input("Please enter a word: ")

str1_count = {}
str2_count = {}

for i in str1:
    count = 0
    for j in str1:
        if i==j:
            count += 1
    str1_count[i] = count

for i in str2:
    count = 0
    for j in str2:
        if i==j:
            count += 1
    str2_count[i] = count

# print(str1_count)
# print(str2_count)

res = True

for pair in str1_count:
    if str1_count[pair] != str2_count[pair]:
        res = False
        break

if res:
    print("Both the given words are Anagrams to each other!")
else:
    print("Both the given words are not Anagrams")