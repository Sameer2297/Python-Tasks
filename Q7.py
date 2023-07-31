# Prime Number

def check_prime(num):
    res = True

    for i in range(2,num):
        if num%i == 0:
            res = False
            break
    
    return res

num = int(input("Please enter a number to check whether it is prime or not: "))

res = check_prime(num)

if res:
    print("Given number {} is a Prime number.".format(num))
else:
    print("Given number {} is not a Prime number.".format(num))