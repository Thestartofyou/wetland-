import requests

# Replace with the actual API endpoint URL
api_url = "https://api.mapsonline.net/wetlands"

# Replace with any required API authentication headers or parameters
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

# Replace with the name of the town or location you want to query
town_name = "YourTownName"

# Make the API request
response = requests.get(api_url, headers=headers, params={"town": town_name})

# Check if the request was successful
if response.status_code == 200:
    wetlands_data = response.json()
    # Process and display the wetlands data as needed
    print(wetlands_data)
else:
    print(f"Failed to retrieve wetlands data. Status code: {response.status_code}")
