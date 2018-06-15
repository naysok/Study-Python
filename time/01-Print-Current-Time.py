import time

# Print Current Time

print(time.time())
print(time.gmtime())

now = time.ctime()
cnvtime = time.strptime(now)
print (time.strftime("%Y/%m/%d %H:%M", cnvtime))