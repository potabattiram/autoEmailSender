from datetime import date
import time
import server
import datetime
import personsData
import json

file = json.loads(personsData.Person)

curr_month = datetime.datetime.now().strftime("%B")
curr_date = datetime.datetime.now().strftime("%d")


def main_Func():
    for i in file:
        if  curr_month in i["bdate"]:
            if curr_date in i["bdate"]:
                server.server.sendmail("potabattiram@gmail.com",i["emailId"],"Hello, "+i["name"]," Wish you a happy birthday bro")
                print("Check your Email Once!")


starttime = time.time()
interval = 3600
while True:
    main_Func()
    time.sleep(interval - ((time.time() - starttime) % interval))
    

