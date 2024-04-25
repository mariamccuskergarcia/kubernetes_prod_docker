import requests

# Request all companies
r = requests.get(r'http://localhost:8101/companies')

print("--------------------------")
print("Requesting all companies of my api, response is:")
print(r.text)
print("--------------------------")
