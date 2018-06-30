import time

# Print Processing Time

time1 = time.time()


for i in range(1000):
    for j in range(1000):

        print("Hello World ",i*j )


        if i*j%3 == 0:
            print("Python")
        elif i*j%3 == 1:
            pass
        else:
            pass




time2 = time.time()


elapsed_time = time2 - time1

print(f"time : {elapsed_time} sec")