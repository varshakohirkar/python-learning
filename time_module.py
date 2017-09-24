import time
def numbers(max):

    max=input("Enter the maximum value")
    time1=time.time()
    for i in range(0,max):
          print(i)
          time.sleep(1)
    time2=time.time()
    print(str(time2-time1))
          


numbers(max)
t=time.localtime()

year=t[0]
month=t[1]
day=t[2]

print(str(year)+"/"+str(month)+"/"+str(day))



