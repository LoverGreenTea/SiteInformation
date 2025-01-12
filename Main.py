import requests

valcode = input("Введіть валюту:")
rate = input("Введіть дату:")
print("-------------")
response = requests.get(
    f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={rate}&json")

data = response.json()

print(data[0]['txt'])
print(data[0]['cc'])
print(data[0]['rate'])
print(data[0]['exchangedate'])
print("-------------")
