# Find the frequency of a number in an array

seq = list(map(int,input("Please enter a sequence of number seperated by space to find count of each number in the sequence: ").split()))

counts_dict = {}

for i in range(len(seq)):
    count = 0
    for j in range(len(seq)):
        if seq[i] == seq[j]:
            count += 1
    counts_dict[seq[i]] = count

items = []

for pair in counts_dict:
    val = counts_dict[pair]
    items.append((pair,val))

print(items)