import datetime
import time
now = datetime.datetime.now()
formatted = now.strftime("%Y-%M-%D-%H-%M")
# yesterday = datetime.datetime(2017-04,15,10,15,0)
# difference = now - yesterday
print(formatted)

lst = []
for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(1) #creates a time delay

print(lst)
