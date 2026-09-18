from api import get_countries
from countries_info import *
countries = get_countries()
print(len(countries))

data = get_countries_info(countries)
# print(data[0])

# region = input("Enter the region you want to search: ")
# countries_by_region = filter_by_region(data, region)
# print(countries_by_region[0])

largest_country = get_largest_country(data)

print(largest_country)

most_population_country = get_most_populous_country(data)
print(most_population_country)


get_my_country = find_country(data,"China")
print(get_my_country)