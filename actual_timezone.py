import pycountry
import pycountry_convert as Pc
from pycountry_convert import country_alpha2_to_continent_code , country_alpha2_to_country_name
import pytz
import datetime
from datetime import datetime
name_of_users = input("please input your first name? ")
name_of_country = input("please provide your country? ").capitalize().title()
name_of_city = input("please provide your Present City?").title()
x = name_of_country
country  = pycountry.countries
country_alpha2_code = pycountry.countries.get(name=x)
w = country_alpha2_code.alpha_2
print(country_alpha2_code.alpha_2)
tmZone = pytz.country_timezones[w]
print(tmZone)
# Sample list
my_list = tmZone

# String to match
target_string = name_of_city
a = my_list

substring_to_find = name_of_city
result = None

for item in a:
    if substring_to_find in item:
        result = item
        break  # Exit the loop after finding the match

if result:
    print("Match found:", result)
else:
    print("No match found.")

