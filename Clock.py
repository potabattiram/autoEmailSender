import schedule
import time 
from Functions import Mail_Sender
import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("potabattiram@gmail.com","Potabatti9012@")

def At_12():
    server.sendmail("potabattiram@gmail.com","potabattiram@gmail.com",'Testing Phase')
    print("Its Testing Phase Bro.")
 
def Test():
     print('Yes Bro, I am Okay & working;)')

schedule.every().seconds.do(Test)

schedule.every().day.at("16:35").do(At_12)
schedule.every().day.at("14:00").do(At_12)
schedule.every().day.at("15:00").do(At_12)
schedule.every().day.at("16:50").do(At_12)
schedule.every().day.at("17:00").do(At_12)
schedule.every().day.at("18:00").do(At_12)
schedule.every().day.at("12:00").do(At_12)

schedule.every().day.at("18:30").do(Mail_Sender)

while True:
    schedule.run_pending()
    time.sleep(59)

