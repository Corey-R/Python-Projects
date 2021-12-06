
# importing datetime module and pytz module
import datetime
from datetime import datetime
import pytz
from pytz import timezone

# timezones
# New York -- America/New_York OR US/Eastern
# Portland -- US/Pacific
# London -- Europe/London

class Open_Hours():
    UTC = pytz.utc 
    tz_portland = pytz.timezone('US/Pacific')
    tz_london = pytz.timezone('Europe/London')
    tz_newYork = pytz.timezone('America/New_York')

    # gets the current date and time of specified timezones
    # NOTE: since the 'datetime' class has already been imported,
    # we don't have to call it below (i.e., datetime.datetime.now())
    dt_portland = datetime.now(tz_portland).strftime('%H')
    dt_london = datetime.now(tz_london).strftime('%H')
    dt_newYork = datetime.now(tz_newYork).strftime('%H')

    

    # defining a method that will determine whether each location is open or closed
    def times(self):
        if int(self.dt_portland) >= 9 and int(self.dt_portland) < 17:
            open_por = "Open "
        else:
            open_por = "Closed "

        if int(self.dt_london) >= 9 and int(self.dt_london) < 17:
            open_lon = "Open "
        else:
            open_lon = "Closed "

        if int(self.dt_newYork) >= 9 and int(self.dt_newYork) < 17:
            open_new = "Open "
        else:
            open_new = "Closed "

        print("Portland HQ: {} \nLondon: {} \nNew York: {}".format(open_por, open_lon, open_new))
            
        
        
        


if __name__ == "__main__":
    Open_Hours().times()
   



