

from datetime import datetime
import pytz

def find_times():
    tz_portland= pytz.timezone('America/Los_Angeles')
    tz_nyc= pytz.timezone('America/New_York')
    tz_london= pytz.timezone('Europe/London')

    datetime_port=datetime.now(tz_portland)
    datetime_nyc=datetime.now(tz_nyc)
    datetime_lon=datetime.now(tz_london)

    open_time= datetime_port.replace(hour=9, minute=0)
    close_time=datetime_port.replace(hour=17, minute=0)

    open_time_nyc= datetime_nyc.replace(hour=9, minute=0)
    close_time_nyc=datetime_nyc.replace(hour=17, minute=0)

    open_time_lon= datetime_lon.replace(hour=9, minute=0)
    close_time_lon=datetime_lon.replace(hour=17, minute=0)

    if open_time <= datetime_port <= close_time:
        print("The Portland office is open!")
    else:
        print("The Portland office is closed!")

    if open_time_nyc <= datetime_nyc <= close_time_nyc:
        print("The NYC office is open!")
    else:
        print("The NYC office is closed!")

    if open_time_lon <= datetime_lon <= close_time_lon:
        print("The London office is open!")
    else:
        print("The London office is closed!")


if __name__=="__main__":
    find_times()

    

#print("The time in Portland is: ", datetime_port.strftime('%H:%M %p %Z'))

#print("The time in NYCis: ", datetime_nyc.strftime('%I:%M %p %Z'))

#print("The time in London is: ", datetime_lon.strftime('%I:%M %p %Z'))


