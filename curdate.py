from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 

# dd/mm/YY H:M:S
def ctime():
    dt_string = now.strftime("%m-%d %H:%M:%S")
    return dt_string