# Power of a number

def power(a, b):
    if b == 0:
        return 1
    result = a
    increment = a
    for i in range(b - 1):
        for j in range(a - 1):
            result += increment
        increment = result
    return result

a=int(input("Please enter base value (a): "))
b=int(input("Please enter exponent value (b): "))

result = power(a,b)

print("The value of a^b: ",result)