#Fibonacci Sequence

def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)

fib_seq = []

a=int(input('Please enter a number to generate Fibonacci series: '))

for i in range(a):
    fib_seq.append(fib(i))

print(*fib_seq)

# Using for loop

for i in range(a):
    if len(fib_seq)<2:
        fib_seq.append(i)
    else:
        fib_seq.append(fib_seq[-1]+fib_seq[-2])

print(*fib_seq)