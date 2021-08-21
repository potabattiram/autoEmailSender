import schedule
import time 
from Functions import Mail_Sender
import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("potabattiram@gmail.com","CalculusmadeE@sy")

def At_12():
    server.sendmail("potabattiram@gmail.com","potabattiram@gmail.com",'Testing Phase')
    print("Its Testing Phase Bro.")
 
def Test():
     print('Yes Bro, I am Okay & working;)')

schedule.every().seconds.do(Test)

schedule.every().day.at("04:00").do(At_12)
schedule.every().day.at("05:00").do(At_12)
schedule.every().day.at("06:00").do(At_12)
schedule.every().day.at("07:00").do(At_12)
schedule.every().day.at("08:00").do(At_12)
schedule.every().day.at("10:10").do(At_12)

schedule.every().day.at("18:30").do(Mail_Sender)

while True:
    schedule.run_pending()
    time.sleep(60)

