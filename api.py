import requests

def get_countries():
 url = "https://countries.dev/countries"
 try:
  response = requests.get(url)
  response.raise_for_status()
  countries = response.json()
  return countries
 except requests.exceptions.RequestException as e:
     print(e)
     return []



