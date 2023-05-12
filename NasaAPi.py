import requests
API_KEY = 'GBVv7U3iHPy3bdgYgi6mZhhFI5s2c2I5QiCoOYdG'
BASE_URL = 'https://api.nasa.gov/neo/rest/v1/feed'
start_date = input("Enter the start date: ")
end_date = input("Enter the end date: ")
ACTUAL_URL = f"{BASE_URL}?start_date={start_date}$end_date={end_date}&api_key={API_KEY}"
response = requests.get(ACTUAL_URL)
data = response.json() 


if response.status_code == 404:
    print("Error")
else:
    print(f"The total number of asteriods during this date are :{data['element_count']}")
    print(f"Date range: {data['near_earth_objects'][start_date][0]['close_approach_data'][0]['close_approach_date_full']} - {data['near_earth_objects'][end_date][0]['close_approach_data'][0]['close_approach_date_full']}")

