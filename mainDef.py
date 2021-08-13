import datetime
import time
import datetime
import personsData
import holidays
import json
import sys 
from threading import Timer
import smtplib
import os
from flask import Flask
app = Flask(__name__)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

file = json.loads(personsData.Person)
curr_whole = datetime.datetime.now().strftime("%Y %m %d")
curr_month = datetime.datetime.now().strftime("%B")
curr_date = datetime.datetime.now().strftime("%d")
curr_Hour = datetime.datetime.now().strftime("%H")

curr_mint = datetime.datetime.now().strftime("%M")

def main_Func():
    for i in file:
        if curr_month in i["b_month"]:
            if curr_date in i["b_date"]:
                subject = 'Birthday Wishes!'
                body = '\nHello, ' + i["name"]+"!"+ '\nHow are you? ' + 'Its been a long while we have met\nHere I remember you on your special occassion of Birthday\nBirthdays are inevitable, beautiful and very particular moments in our lives! \nMoments that brings precious memories back, celebrates the present times and gives a strong hope for the future.'+ '\n\n'+i["name"].split()[0] +', Wish you a Happy and Prosperous Birthday\nThank You!'
                message = f'Subject: {subject}\n\n{body}'

                server = smtplib.SMTP_SSL("smtp.gmail.com",465)
                server.login("potabattiram@gmail.com","Potabatti9012@")
                server.sendmail("potabattiram@gmail.com",i["emailId"],message)
                print("Email Sent for Bday!")


def Festival_Emails():
    for date,day in sorted(holidays.India(years=2021, state='MH').items()):
        # if curr_whole == date: 
            for i in file:
                subject = day
                body = '\nHello, ' + i["name"]+"!"+ ',\nHere, I wish you a very {day} with loads of happiness'
                message = f'Subject: {subject}\n\n{body}'

                Mainserver.server.sendmail("potabattiram@gmail.com",i["emailId"],message)
                print("Email Sent to "+ i["name"] +"for Festivals!")

interval = 10


@app.route("/")   
def MainFunction():     
    for i in range(sys.maxsize):
            t = Timer(3.0, main_Func)
            t.start()
            time.sleep(interval)

MainFunction()