import time
from datetime import datetime as dt
hosts_path =r"/etc/hosts"
hosts_temp = r"hosts"
redirect = "127.0.0.1"
weblist = ["www.facebook.com","facebook.com"]

currentYear = dt.now().year
currentMonth = dt.now().month
currentDay = dt.now().day
currentHour = dt.now().hour

while True:
    if dt(currentYear,currentMonth,currentDay, 8) < dt.now() < dt(currentYear,currentMonth,currentDay, 9):
        print("Working" )
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in weblist:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in weblist):
                    file.write(line)
            file.truncate()
        print("fun fun fun")
    time.sleep(5)
