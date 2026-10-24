import requests


# requires to run this in your terminal : python -m pip install requests befor running the program

url = "https://www.google.com"

try:
    response = requests.get(url)
    print("URL:", url)
    print("Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
