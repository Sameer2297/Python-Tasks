# Find minimum and maximum number from the sequence

def minimum(seq):
    min_num = seq[0]
    for i in seq:
        if i < min_num:
            min_num = i
    return min_num

def maximum(seq):
    max_num = seq[0]
    for i in seq:
        if i > max_num:
            max_num = i
    return max_num

num_seq = list(map(int,input("Please enter numbers seperated by a space: ").split()))

print("The minimum number in the given sequence is:",minimum(num_seq))

print("The maximum number in the given sequence is:",maximum(num_seq))