import requests

# Get the data from the API
def call_api(endpoint):
    response = requests.get(f"https://api.usaspending.gov/{endpoint}")
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data.")

