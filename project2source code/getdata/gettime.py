import datetime
import time
def ctime(f,data):
    startime =  time.clock()
    a,b =f(data)
    endtime = time.clock()
    return endtime - startime
