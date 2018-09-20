import sys

args = sys.argv

# print(len(args))
# print(args[0])

result = 0

for i in range(len(args)-1):
    result += int(args[i+1])

print("Result is",result)


# $python3 Add.py 1 2 3 4
# Result is 10

# $ python3 Add.py 1 2 3 4 5 6 7 8 9
# Result is 45