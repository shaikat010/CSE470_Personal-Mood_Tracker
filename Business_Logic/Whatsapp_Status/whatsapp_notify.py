import time

import pywhatkit

from datetime import datetime

naive_dt = datetime.now()

naive_utc_dt = datetime.utcnow()

print(naive_utc_dt)
print(naive_dt) # "this gives the current data""
x = str(naive_dt)
print(x)
y = x.split(" ")
print(y)
z = y[1].split(":")
print(z)



hour = int(z[0])
minute = int(z[1])
print(minute)
print(type(minute))
final_min = minute + 2

def send_notification(x):
     notification = pywhatkit.sendwhatmsg("+8801827595264", "Your mood status is "+ x ,hour, final_min)
     return notification

send_notification("Hello There")


