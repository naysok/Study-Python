number2 = "4321"
print(number2)
print(type(number2))

"""
4321
<class 'str'>
"""


number2_cast_int = int(number2) # cast
print(number2_cast_int)
print(type(number2_cast_int))

"""
4321
<class 'int'>
"""

print("-----")

### python の int() のキャストは切り捨て

number_float1 = 1.4
number_float1_int = int(number_float1)

number_float2 = 7.9
number_float2_int = int(number_float2)

print("float :", number_float1, ", int :", number_float1_int)
print("float :", number_float2, ", int :", number_float2_int)

