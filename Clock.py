import schedule
import time 
from Functions import Mail_Sender
import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("potabattiram@gmail.com","Potabatti9012@")

def At_12():
    server.sendmail("potabattiram@gmail.com","potabattiram@gmail.com",'Its 10')
    print("12:00 Testing")
 
def Test():
     print('Test')

schedule.every().seconds.do(Test)
schedule.every().day.at("00:00").do(At_12)
schedule.every().day.at("23:45").do(Mail_Sender)

while True:
    schedule.run_pending()
    time.sleep(2)

