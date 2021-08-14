import datetime
import datetime
import personsData
import json
import smtplib

file = json.loads(personsData.Person)
curr_whole = datetime.datetime.now().strftime("%Y %m %d")
curr_month = datetime.datetime.now().strftime("%B")
curr_date = datetime.datetime.now().strftime("%d")
curr_Hour = datetime.datetime.now().strftime("%H")

curr_mint = datetime.datetime.now().strftime("%M")

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("potabattiram@gmail.com","Potabatti9012@")

def Mail_Sender():
    for i in file:
        if curr_month in i["b_month"]:
            if curr_date in i["b_date"]-1:
                subject = 'Birthday Wishes!'
                body = '\nHello, ' + i["name"]+"!"+ '\nHow are you? ' + 'Its been a long while we have met\nHere I remember you on your special occassion of Birthday\nBirthdays are inevitable, beautiful and very particular moments in our lives! \nMoments that brings precious memories back, celebrates the present times and gives a strong hope for the future.'+ '\n\n'+i["name"].split()[0] +', Wish you a Happy and Prosperous Birthday\nThank You!'
                message = f'Subject: {subject}\n\n{body}'

                server.sendmail("potabattiram@gmail.com",i["emailId"],message)
                print("Email Sent for Bday!")


# def Festival_Emails():
#     for date,day in sorted(holidays.India(years=2021, state='MH').items()):
#         # if curr_whole == date: 
#             for i in file:
#                 subject = day
#                 body = '\nHello, ' + i["name"]+"!"+ ',\nHere, I wish you a very {day} with loads of happiness'
#                 message = f'Subject: {subject}\n\n{body}'

#                 server.sendmail("potabattiram@gmail.com",i["emailId"],message)
#                 print("Email Sent to "+ i["name"] +"for Festivals!")

