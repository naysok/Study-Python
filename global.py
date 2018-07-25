# グローバル変数


var_A = 4

def calc_add_A(x):
    print(var_A+x)

calc_add_A(3)
# out
# 7 (4 + 3)


### -------------------------------------------------


var_B = 2

def calc_add_B(x):
    var_B = 200 # update
    print(var_B + x)


calc_add_B(10)
# out
# 210 (200 + 10)

print(var_B)
# 2


### -------------------------------------------------


var_C = 99

def calc_add_C(x):
    global var_C
    var_C = 20
    print(var_C + x)

calc_add_C(1)
# out
# 21 (20 + 1)

print(var_C)
# 20