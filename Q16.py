# Reducing the number to single digit by adding every corresponding digit in the number

num = int(input())

while len(str(num)) > 1 :
    res = 0
    for i in str(num):
        res += int(i)
    
    num = res

print(num)