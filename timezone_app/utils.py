import pycountry
import pycountry_convert as Pc
import pytz
from datetime import datetime

def get_info(name, country_name, city_name):
    try:
        # Try exact match first
        country_obj = pycountry.countries.get(name=country_name.title())
        if not country_obj:
            # Try fuzzy search if exact match fails
            try:
                results = pycountry.countries.search_fuzzy(country_name)
                if results:
                    country_obj = results[0]
            except LookupError:
                pass

        if not country_obj:
            return {"error": "Country not found."}

        country_code = country_obj.alpha_2

        try:
            continent_code = Pc.country_alpha2_to_continent_code(country_code)
            continent_name = Pc.convert_continent_code_to_continent_name(continent_code)
        except Exception:
            continent_name = "Unknown"

        timezones = pytz.country_timezones.get(country_code, [])

        selected_tz = None
        for tz in timezones:
            if city_name.title() in tz:
                selected_tz = tz
                break

        if not selected_tz and timezones:
            selected_tz = timezones[0]

        if selected_tz:
            tz_obj = pytz.timezone(selected_tz)
            current_time = datetime.now(tz_obj).strftime("%Y-%m-%d %H:%M:%S")
        else:
            current_time = "Unknown"

        return {
            "name": name,
            "country": country_obj.name,
            "continent": continent_name,
            "timezone": selected_tz,
            "time": current_time
        }
    except Exception as e:
        return {"error": str(e)}
