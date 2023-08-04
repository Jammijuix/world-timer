import pycountry
import pycountry_convert as Pc
from pycountry_convert import country_alpha2_to_continent_code , country_alpha2_to_country_name
import pytz
import datetime
from datetime import datetime
name_of_users = input("please input your first name? ")
name_of_country = input("please provide your country? ").capitalize().title()
name_of_city = input("please provide your Present City?").title()
def country_to_continent(country_name):
    country_alpha2 =Pc.country_name_to_country_alpha2(country_name)
    country_continent_code = Pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = Pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name
x = "Nigeria"
country  = pycountry.countries
country_alpha2_code = pycountry.countries.get(name=x)
w = country_alpha2_code.alpha_2
print(country_alpha2_code.alpha_2)
#time_zone = pytz.all_timezones #timezone("Africa/Lagos")
tmZone = pytz.country_timezones[w]
print(tmZone)
users_timezone = f"'{country_to_continent(name_of_country)}/{name_of_city}'"
print(users_timezone)
'''country_time_zone = pytz.timezone(tmZone)
country_time = datetime.now(country_time_zone)
print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))'''
