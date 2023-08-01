# Generate a Fibonacci sequence

a=int(input('Please enter a number to generate Fibonacci series: '))

fib_seq = []

for i in range(a):
    if len(fib_seq)<2:
        fib_seq.append(i)
    else:
        fib_seq.append(fib_seq[-1]+fib_seq[-2])

print(*fib_seq)