# Swap two numbers without using a third variable

a=int(input("Please enter first number: "))
b=int(input("Please enter second number: "))

a,b = b,a

print("The value of first variable is:",a)
print("The value of second variable is:",b)