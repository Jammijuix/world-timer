import pycountry
import pycountry_convert as Pc
import pytz
from datetime import datetime

"""def number_of_country(country):
    list_ = []
    for country in pycountry.country.get(country_code=country):
        list_.append(country.name)
    return list_"""
#x = pycountry.countries.get(alpha_2='NG').name

'''for country in y:
    print(country.name)

print(country)'''
y = pycountry.countries
name_of_country = input("please provide your country?").capitalize()
country_list = []
for country in y:
    country_list.append(country.name)
#print(country_list)
#string in the list
if name_of_country in country_list:
    print("your country official name is:", name_of_country)
else:
    print("its not a country name.")
# functions that helps get a continent
country_name = name_of_country
def country_to_continent(country_name):
    country_alpha2 =Pc.country_name_to_country_alpha2(country_name)
    country_continent_code = Pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = Pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name
print("Your Continent is: ",country_to_continent(country_name))

# function that helps show timezone and time.
x = country_name
country_alpha2_code = pycountry.countries.get(name=x)
Users_country_alpha2_code = country_alpha2_code.alpha_2
print(country_alpha2_code.alpha_2)
#time_zone = pytz.all_timezones #timezone("Africa/Lagos")
tmZone = pytz.country_timezones[Users_country_alpha2_code]
print(tmZone)
