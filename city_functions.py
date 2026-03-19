def get_city_country(city, country,  population=''):
    if population:
        return f"{city.title()}, {country.title()}– población {population}"
    else:
        return f"{city.title()}, {country.title()}"