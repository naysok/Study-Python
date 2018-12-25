def Remap(src, old_min, old_max, new_min, new_max):
    return( (src - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min


value_1 = Remap(50, 0, 100.0, -1.0, 1.0)
print(value_1)

value_2 = Remap(50, 0, 100.0, 0, 1.0)
print(value_2)

value_3 = Remap(50, 0, 100.0, 0, 2.0)
print(value_3)