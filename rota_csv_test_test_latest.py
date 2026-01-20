import csv
from datetime import datetime,date, timedelta
import pytz
import requests



url='https://fn-gc-dv-we-01.azurewebsites.net/api/schedule'
filename='rota.csv'
third_shift_name = "Haris Pirzada"
third_shift_tel = "0887219388"
new_list=[]

def dt_convert(row_num):
    req_date = row_num
    text = req_date.split()
    temp_dt=f"{text[1]} {text[2]}"
    final_date=datetime.strptime(temp_dt, '%d-%b-%Y %H:%M')
    tz = pytz.timezone("America/New_York")
    #Check the time
    if final_date.hour==10:
        temp_d=str(final_date.date())+" 03:00"
        temp_dd=datetime.strptime(temp_d, '%Y-%m-%d %H:%M')
        am_time = tz.localize(datetime(temp_dd.year, temp_dd.month, temp_dd.day, 3, 00), is_dst=None)
        utc_date = am_time.astimezone(pytz.timezone('UTC'))
    if final_date.hour==18:
        temp_d=str(final_date.date())+" 11:00"
        temp_dd=datetime.strptime(temp_d, '%Y-%m-%d %H:%M')
        am_time = tz.localize(datetime(temp_dd.year, temp_dd.month, temp_dd.day, 11, 00), is_dst=None)
        utc_date = am_time.astimezone(pytz.timezone('UTC'))
    if final_date.hour==2:
        temp_d=str(final_date.date()-timedelta(days=1))+" 19:00"
        temp_dd=datetime.strptime(temp_d, '%Y-%m-%d %H:%M')
        am_time = tz.localize(datetime(temp_dd.year, temp_dd.month, temp_dd.day, 19, 00), is_dst=None)
        utc_date = am_time.astimezone(pytz.timezone('UTC'))

    #utc_date = final_date.astimezone(pytz.timezone('UTC'))
    new_text=str(utc_date).split()
    new_time=new_text[1]
    dd=new_text[0]
    tt=new_time[:8]
    final_dt = f"{dd}T{tt}"
    return final_dt

def insert_third_shift():
    third_shift_dict = {}
    third_shift_dict["startDate"] = temp_end_time

    temp_date01 = datetime.strptime(temp_end_time, '%Y-%m-%dT%H:%M:%S')
    temp_date02 = temp_date01 + timedelta(hours=8)
    temp_date03 = str(temp_date02)
    temp_date04 = temp_date03.split()
    new_time = f"{temp_date04[0]}T{temp_date04[1]}"

    third_shift_dict["endDate"] = new_time
    third_shift_dict["name"] = third_shift_name
    third_shift_dict["phone"] = third_shift_tel
    new_list.append(third_shift_dict)

with open(filename, 'r') as f:
    add_third_shift=bool
    temp_end_time=str()
    text01=csv.reader(f)
    for row in text01:
        if (row[0]=='Date' and row[1]=='Shift' and row[2]=='Start' and row[3]=='End' and row[4]=='Engineer' and row[5]=='Contact'):
            continue
        if (row[0]=='' and row[1]=='' and row[2]=='' and row[3]=='' and row[4]=='' and row[5]==''):
            continue
        if add_third_shift==True:
            insert_third_shift()

        my_dict={}
        my_dict["startDate"]=dt_convert(row[2])
        my_dict["endDate"]=dt_convert(row[3])
        my_dict["name"]=row[4]
        my_dict["phone"]=row[5]
        new_list.append(my_dict)
        if "00:00:00" in my_dict["endDate"]:
            add_third_shift=True
            temp_end_time=my_dict["endDate"]
        else:
            add_third_shift=False
    if add_third_shift==True:
        insert_third_shift()



''''Test print the lines'''
for item in new_list:
   print(item)

'''Test POST a single line'''
#resp_req=requests.post(url, json=new_list[14] )
#print(resp_req.text)
#print(f"Line updated:\n{new_list[14]}")

'''POST all lines and print the result for each line'''
# for item in new_list:
#     res_req=requests.post(url, json=item)
#     print(f"Line updated:{item}\n Status:{res_req.text}")



