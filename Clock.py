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
     print('Working Well!')

schedule.every().seconds.do(Test)
schedule.every().day.at("15:00").do(Mail_Sender)
schedule.every().day.at("16:00").do(Mail_Sender)
schedule.every().day.at("17:00").do(Mail_Sender)
schedule.every().day.at("18:52").do(Mail_Sender)

while True:
    schedule.run_pending()
    time.sleep(6)

