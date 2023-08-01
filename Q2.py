#Armstrong Number

def power(a,b):
    if b == 0:
        return 1
    result = a
    increment = a
    for i in range(b-1):
        for j in range(a-1):
            result += increment
        increment = result
    return result

num = input('Please enter a number: ')

pow = len(num)

res = 0

for i in num:
    res += power(int(i),pow)

if res == int(num):
    print("Given number '{}' is an Armstrong Number".format(num))
else:
    print("Given number '{}' is not an Armstrong Number".format(num))