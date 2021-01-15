import requests

api_key = "89236ab4-678f-4320-965a-efed356a900a"

url = 'https://api2.r6stats.com/public-api/stats/Kuri_NEON/pc/generics'
headers = "Authorization: Bearer " + api_key
jsonData = requests.get(url, headers=headers).json()
print(jsonData)