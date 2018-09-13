import random

### 0 to 1.0
r0 = random.random()
print(r0)
### out
### 0.24723391432174502
### out
### 0.49865911083118075


print("---")


r_uniform = random.uniform(0, 10)
print(r_uniform)
### out
### 7.193823411688488
### out
### 2.5840504417492016


print("---")


r1 = random.randrange(0, 10.0)
print("r1 = ", r1)
### out
### r1 =  8

### out
### r1 =  8


print("---")


random.seed(3)
r_s1 = random.randrange(0, 10.0)
print(r_s1)


print("---")


for i in range(10):
    r = random.randrange(0, 10.0)
    print("r",str(i),"=", str(r))

### out
"""
r 0 = 1
r 1 = 8
r 2 = 4
r 3 = 3
r 4 = 2
r 5 = 8
r 6 = 7
r 7 = 9
r 8 = 9
r 9 = 9
"""


### out
"""
r 0 = 7
r 1 = 4
r 2 = 9
r 3 = 2
r 4 = 9
r 5 = 8
r 6 = 3
r 7 = 1
r 8 = 2
r 9 = 1
"""