import requests

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

with open("data/raw/nav_data.json", "w") as f:
    f.write(response.text)

print("NAV Data Saved")