import pytz
import pycountry
import pycountry_convert as Pc
from datetime import datetime
from datetime import datetime
x = "Nigeria"
country  = pycountry.countries
country_alpha2_code = pycountry.countries.get(name=x)
w = country_alpha2_code.alpha_2
print(w)
#time_zone = pytz.all_timezones #timezone("Africa/Lagos")
#tmZone = pytz.country_timezones[w]
#print(tmZone)

#print(time_zone,"\n")
'''x = pytz.utc
print(x)

country_time_zone = pytz.timezone('America/New_York')
country_time = datetime.now(country_time_zone)
print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))'''
