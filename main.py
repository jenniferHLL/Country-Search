from api import *
from countries_info import *
from display import *

data = get_countries()
countries = get_countries_info(data)
while True:
    display_menu()
    try:
        choice = int(input("Enter choice(from 1 to 5): "))
    except ValueError:
        print("Invalid choice,Please try again")
        continue
    if choice == 1:
        region = input("Enter region name: ")
        countries_by_region = filter_by_region(countries,region)
        display_countries_by_region(countries_by_region)
    elif choice == 2:
        largest_country = get_largest_country(countries)
        display_largest_country(largest_country)
    elif choice == 3:
        most_populous_country = get_most_populous_country(countries)
        display_most_populous_country(most_populous_country)
    elif choice == 4:
        countryA = input("Enter country 1: ")
        countryB = input("Enter country 2: ")
        country1 = find_country(countries,countryA)
        country2 = find_country(countries,countryB)
        if not country1 or not country2:
            print("Country not found. Please try again.")
            continue
        display_two_countries(country1, country2)
    elif choice == 5:
        print("See you next time!")
        break
    else:
        print("Enter a valid choice,Please try again")






