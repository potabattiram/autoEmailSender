import holidays
import datetime

curr_date = datetime.datetime.now().strftime("%Y %m %d")

for date,day in sorted(holidays.India(years=2021, state='MH').items()):
    if curr_date == '2021 08 12': 
        print(day)
        break




# # # def clock():
# # #     while True:
# # #         print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
# # #         time.sleep(1)

# # # clock()

# # while True:
    
# while True:
#     if curr_date == '20':
#         print('its 20')
#         break
        
