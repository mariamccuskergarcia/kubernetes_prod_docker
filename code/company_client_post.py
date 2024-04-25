import requests

# Posts a new company
company_details = {
    "ticker": "PYPL",
    "name": "PayPal",
    "website": "www.paypal.com"
}

r = requests.post(r'http://localhost:8101/companies/', json=company_details)

print("--------------------------")
print("Posting a company to my api, response is:")
print(r.text)
print("--------------------------")
