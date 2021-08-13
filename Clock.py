import schedule
import time 
from mainDef import Mail_Sender
import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("potabattiram@gmail.com","Potabatti9012@")
def At_12():
    server.sendmail("potabattiram@gmail.com","potabattiram@gmail.com",'Its 12:00')
    print("12:00 Testing")
    


schedule.every(3600).seconds.do(Mail_Sender)
schedule.every().day.at("00:00").do(At_12)

while True:
    schedule.run_pending()
    time.sleep(3600)

