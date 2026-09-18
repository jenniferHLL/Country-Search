def get_countries_info(countries):
    result = []
    for country in countries:
        language_names = []
        for language in country.get("languages", []):
            language_names.append(language.get("name"))
        result.append({
            "name": country.get("name"),
            "capital": country.get("capital"),
            "region": country.get("region"),
            "flag": country.get("flag"),
            "area": country.get("area"),
            "population": country.get("population"),
            "populationDensity": country.get("populationDensity"),
            "languages": language_names,
        })


    return result

def filter_by_region(countries,region):
    result = []
    for country in countries:
        if country.get("region") == region:
            result.append(country)

    return result

def get_largest_country(countries):
    result = {
        "name": countries[0].get("name"),
        "area": countries[0].get("area"),
    }
    for country in countries:
        if country.get("area") is None:
            continue

        if country.get("area") > result.get("area"):
           result = {
               "name": country.get("name"),
               "area": country.get("area"),
           }
        else:
            result = result

    return result

def get_most_populous_country(countries):
    result = {
        "name": countries[0].get("name"),
        "population": countries[0].get("population"),
        "populationDensity": countries[0].get("populationDensity"),
    }
    for country in countries:
        if country.get("population") is None:
            continue

        if country.get("population") > result.get("population"):
            result = {
                "name": country.get("name"),
                "population": country.get("population"),
                "populationDensity": country.get("populationDensity"),
            }
        else:
            result = result
    return result

def find_country(countries,country_input):
    result = {}
    for country in countries:
        if country_input == country.get("name"):
            result = country
            return result

    return {}