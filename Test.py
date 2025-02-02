import requests

GameCode = input("Введіть код ігри: ")

print("-------------")
response = requests.get(
    f"https://store.steampowered.com/api/appdetails?appids={GameCode}")

data = response.json()

print(data[GameCode]['data']['type'])
print(data[GameCode]['data']['name'])
print(data[GameCode]['data']['is_free'])
print(data[GameCode]['data']['price_overview']['final_formatted'])
print("-------------")