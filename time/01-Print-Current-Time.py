import time

# Print Current Time


print(time.time())
'''
1530359435.175801
'''


print(time.gmtime())
'''
time.struct_time(tm_year=2018, tm_mon=6, tm_mday=30, tm_hour=11, tm_min=50, tm_sec=35, tm_wday=5, tm_yday=181, tm_isdst=0)
'''


now = time.ctime()
cnvtime = time.strptime(now)
print (time.strftime("%Y/%m/%d %H:%M", cnvtime))
'''
2018/06/30 20:50
'''