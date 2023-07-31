#Armstrong Number

num = input('Please enter a number: ')

pow = len(num)

res = 0

for i in num:
    res += int(i)**pow

if res == int(num):
    print("Given number '{}' is an Armstrong Number".format(num))
else:
    print("Given number '{}' is not an Armstrong Number".format(num))