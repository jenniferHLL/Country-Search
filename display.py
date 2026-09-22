def display_countries_by_region(countries):
    for country in countries:
        if not countries:
            print("There are no countries in this region")
            return

    for country in countries:
        print(f"{country.get('flag')}{country.get('name')}")

def display_largest_country(country):
    print("The largest country is " + country.get("name"))
    print(f"{country.get('area')}km^2")

def display_most_populous_country(country):
    print("The most populous country is " + country.get("name"))
    print(f"{country.get('population')}")
    print(f"{country.get('populationDensity')}people/km^2")

def display_two_countries(country1,country2):
    print(f"{'':<20}{country1.get('name'):<20}{country2.get('name'):<20}")
    print(f"{'Area':<20}{country1.get('area'):<20}{country2.get('area'):<20}")
    print(f"{'Capital':<20}{country1.get('capital'):<20}{country2.get('capital'):<20}")
    print(f"{'Population':<20}{country1.get('population'):<20}{country2.get('population'):<20}")
    print(f"{'Languages':<20}{', '.join(country1.get('languages')):<20}{', '.join(country2.get('languages')):<20}")

