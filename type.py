hello = "Hello World!!"
print(hello)
print(type(hello))

"""
Hello World!!
<class 'str'>
"""

###

number1 = 1234
print("int -", number1)
print(type(number1))

"""
int - 1234
<class 'int'>
"""

###

number2 = "5678"
print("str -", number2)
print(type(number2))

"""
str - 5678
<class 'str'>
"""


number2_cast_int = int(number2) # cast
print("int -", number2_cast_int)
print(type(number2_cast_int))

"""
int - 5678
<class 'int'>
"""


number2_cast_float = float(number2) # cast
print("float -", number2_cast_float)
print(type(number2_cast_float))

"""
float - 5678.0
<class 'float'>
"""
