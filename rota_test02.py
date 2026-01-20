import csv
from datetime import datetime, date, timedelta
import pytz
import requests


url='https://fn-gc-dv-we-01.azurewebsites.net/api/schedule'
filename='rota.csv'
new_list=[]

def dt_convert(row_n):
    req_date = row_n
    text = req_date.split()
    temp_dt=f"{text[1]} {text[2]}"
    format='%d-%b-%Y %H:%M'
    final_date=datetime.strptime(temp_dt, format)
    utc_date = final_date.astimezone(pytz.timezone('UTC'))
    if final_date.hour==10:
        temp_d=str(final_date.date())+" 03:00"
        temp_dd=datetime.strptime(temp_d, '%Y-%m-%d %H:%M')
        tz = pytz.timezone("America/New_York")
        am_time = tz.localize(datetime(temp_dd.year, temp_dd.month, temp_dd.day, 3, 00), is_dst=None)
        utc_date = am_time.astimezone(pytz.timezone('UTC'))
    if final_date.hour==18:
        temp_d=str(final_date.date())+" 11:00"
        temp_dd=datetime.strptime(temp_d, '%Y-%m-%d %H:%M')
        tz = pytz.timezone("America/New_York")
        am_time = tz.localize(datetime(temp_dd.year, temp_dd.month, temp_dd.day, 11, 00), is_dst=None)
        utc_date = am_time.astimezone(pytz.timezone('UTC'))
    if final_date.hour==2:
        temp_d=str(final_date.date()-timedelta(days=1))+" 19:00"
        temp_dd=datetime.strptime(temp_d, '%Y-%m-%d %H:%M')
        tz = pytz.timezone("America/New_York")
        am_time = tz.localize(datetime(temp_dd.year, temp_dd.month, temp_dd.day, 19, 00), is_dst=None)
        utc_date = am_time.astimezone(pytz.timezone('UTC'))

    new_text=str(utc_date).split()
    new_time=new_text[1]
    dd=new_text[0]
    tt=new_time[:8]
    final_dt = f"{dd}T{tt}"
    return final_dt

with open(filename, 'r') as f:
    text01=csv.reader(f)
    for row in text01:
        if (row[0]=='Date' and row[1]=='Shift' and row[2]=='Start' and row[3]=='End' and row[4]=='Engineer' and row[5]=='Contact'):
            continue
        if (row[0]=='' and row[1]=='' and row[2]=='' and row[3]=='' and row[4]=='' and row[5]==''):
            continue
        my_dict={}
        my_dict["startDate"]=dt_convert(row[2])
        my_dict["endDate"]=dt_convert(row[3])
        my_dict["name"]=row[4]
        my_dict["phone"]=row[5]
        new_list.append(my_dict)

for item in new_list:
    print(item)
