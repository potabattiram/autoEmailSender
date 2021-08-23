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
schedule.every().day.at("20:00").do(Mail_Sender)
schedule.every().day.at("21:00").do(Mail_Sender)
schedule.every().day.at("22:00").do(Mail_Sender)
schedule.every().day.at("19:52").do(Mail_Sender)

while True:
    schedule.run_pending()
    time.sleep(6)

