import time

# Print Processing Time

time1 = time.time()


for i in range(1000000):

    if i%3 == 0:
        pass
    elif i%3 == 1:
        pass
    else:
        pass


time2 = time.time()

#

elapsed_time = time2 - time1

print(f"time : {elapsed_time} sec")