
from datetime import datetime
from errno import ESTALE

import pytz
from pytz import timezone

format = "%Y-%m-%dT%H:%M:%S"

# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
#print(now_utc.strftime(format))

# Convert to Asia/Kolkata time zone
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
#print(now_asia.strftime(format))

#print(now_utc.hour)
# if now_utc.hour==8:
#     print("The sky is blue")
#     print(now_utc.date())
#     print(now_utc)


# test01="2025-03-27 18:00"
# temp_dd=datetime.strptime(test01, '%Y-%m-%d %H:%M')
# utc_date = temp_dd.astimezone(pytz.timezone('UTC'))
# utc_date02=temp_dd.replace(tzinfo=pytz.timezone('EST'))
# print(utc_date02)


# format='%Y-%m-%d %H:%M'
# final_date=datetime.strptime(test01, format)
# final_date=final_date.replace(tzinfo=pytz.timezone('America/New_York'))
#
#
# #utc_date = final_date.astimezone(pytz.timezone('UTC'))
#
# print(final_date)

# format = '%d-%b-%Y %H:%M'
# final_date = datetime.strptime(temp_dt, format)
# utc_date = final_date.astimezone(pytz.timezone('UTC'))
new_time=now_utc.astimezone(pytz.timezone('EST'))

test01=str(new_time.date())
test01+=" 18:00"
temp_dd=datetime.strptime(test01, '%Y-%m-%d %H:%M')


tz=pytz.timezone("America/New_York")
am_time = tz.localize(datetime(temp_dd.year, temp_dd.month, temp_dd.day, 11, 00), is_dst=None)
utc_date = am_time.astimezone(pytz.timezone('UTC'))
print(utc_date)

