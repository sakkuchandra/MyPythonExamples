# import only datetime class
from datetime import datetime

# current datetime
now = datetime.now()

current_date = now.date()
print('Date:', current_date)
print(type(current_date))

current_time = now.time()
print('Time', current_time)
print(type(current_time))


Note:  time() allows us to get currently executing time from the system which we are working.

Note:  date() allows us to get currently executing date from the system which we are working.
