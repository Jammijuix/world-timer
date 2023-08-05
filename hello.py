import pycountry
import pycountry_convert as Pc
import pytz
from datetime import datetime
print(datetime.now())

# important variables
try:
    name_of_users = input("please input your first name? ")
    name_of_country = input("please provide your country? ").capitalize().title()
    name_of_city = input("please provide your Present City?").title()
    #users_timezone = f'{name_of_country},{name_of_city}'

# code that helps choose country.
    y = pycountry.countries
except Exception as e:
    print("The error is:", e)
#name_of_country = input("please provide your country?").capitalize()
try:
    country_list = []
    for country in y:
        country_list.append(country.name)
    #print(country_list)
    #string in the list
    if name_of_country in country_list:
        print("Hello", name_of_users + "\n"+ "Your country official name is: ",name_of_country)
    else:
        print("its not a country name.")
    #function that helps identify users continent
    country_name = name_of_country
    def country_to_continent(country_name):
        country_alpha2 =Pc.country_name_to_country_alpha2(country_name)
        country_continent_code = Pc.country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = Pc.convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name
    print("Your Continent is: ",country_to_continent(country_name))
except Exception as e:
    print("the Error is:",e)
# function to displace your country time..
try:
    if country_to_continent(country_name) == 'North America' or 'Asia' or 'South America' or 'Europe' or 'Oceania':
        if country_name in country_list:
            x = country_name
            country_alpha2_code = pycountry.countries.get(name=x)
            Users_country_alpha2_code = country_alpha2_code.alpha_2
            print(country_alpha2_code.alpha_2)
            #time_zone = pytz.all_timezones #timezone("Africa/Lagos")
            tmZone = pytz.country_timezones[Users_country_alpha2_code]
            #print(tmZone)
            #code responsible for country actual time..
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

            '''if result:
                print("Match found:", result)
            else:
                print("No match found.")'''
        
            country_time_zone = pytz.timezone(result)
            country_time = datetime.now(country_time_zone)
            print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))
        else:
            print("Please provide a valid country.")
    #except Exception as e:
    #print("the error is:",e)
    if country_to_continent(country_name) == 'Africa':
        if country_name in country_list:
            x = country_name
            country_alpha2_code = pycountry.countries.get(name=x)
            Users_country_alpha2_code = country_alpha2_code.alpha_2
            print(country_alpha2_code.alpha_2)
            #time_zone = pytz.all_timezones #timezone("Africa/Lagos")
            tmZone = pytz.country_timezones[Users_country_alpha2_code]
            country_time_zone = pytz.timezone(tmZone)
            country_time = datetime.now(country_time_zone)
            print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))
        else:
            print("Please provide a valid country.")
except Exception as e:
    print("the error is:",e)
