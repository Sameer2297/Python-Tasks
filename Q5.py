# Remove duplicates from the sequence

seq = input("Please enter the sequence of characters seperated by space to remove duplicates:").split()

counts_dict = {}

for i in range(len(seq)):
    count = 0
    for j in range(len(seq)):
        if seq[i]==seq[j]:
            count += 1
    if count == 1:
        counts_dict[seq[i]] = count

unique_values = []

for pair in counts_dict:
    unique_values.append(pair)

print(unique_values)