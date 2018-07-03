str1 = input('please enter str1 : ')
print('str1 is "', str1, '"')

int1 = input('please enter integer1 : ') #ここで
int2 = input('please enter integer2 : ')

"""
print(int1)
print(type(int1))
# これに <class 'str'> とかえってくる
"""

sum_int = int(float(int1)) + int(float(int2))
# cast
# str -> int : X
# str -> float -> int : O

print(sum_int)


"""
please enter str1 : apple
str1 is " apple "

please enter integer1 : 1.234
please enter integer2 : 9.99
10 # 切り捨てで (1 + 9)
"""