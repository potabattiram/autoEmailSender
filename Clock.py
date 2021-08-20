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

schedule.every().day.at("16:35").do(At_12)
schedule.every().day.at("16:46").do(At_12)
schedule.every().day.at("17:45").do(At_12)
schedule.every().day.at("18:20").do(At_12)
schedule.every().day.at("18:50").do(At_12)
schedule.every().day.at("19:00").do(At_12)
schedule.every().day.at("20:00").do(At_12)

schedule.every().day.at("18:30").do(Mail_Sender)

while True:
    schedule.run_pending()
    time.sleep(60)

