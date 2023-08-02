import pycountry
import pycountry_convert as Pc
from pycountry_convert import country_alpha2_to_continent_code , country_alpha2_to_country_name
import pytz
import datetime
from datetime import datetime
x = "Nigeria"
country  = pycountry.countries
country_alpha2_code = pycountry.countries.get(name=x)
w = country_alpha2_code.alpha_2
print(country_alpha2_code.alpha_2)
#time_zone = pytz.all_timezones #timezone("Africa/Lagos")
tmZone = pytz.country_timezones[w]
print(tmZone)
'''country_time_zone = pytz.timezone(tmZone)
country_time = datetime.now(country_time_zone)
print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))'''
