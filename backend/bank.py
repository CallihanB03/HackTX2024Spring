# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json
import datetime

apiKey = '2562b2e98f7a38a09dbaa132bece8b56'

# Create a customer
def create_customer(firstName, lastName, streetNumber, streetName, city, state, zipCode):
    url = 'http://api.nessieisreal.com/customers?key={}'.format(apiKey)
    payload = {
      "first_name": firstName,
      "last_name": lastName,
      "address": {
        "street_number": streetNumber,
        "street_name": streetName,
        "city": city,
        "state": state,
        "zip": zipCode
      }
    }
    response = requests.post( 
        url, 
        data=json.dumps(payload),
        headers={'content-type':'application/json'},
        )
    if response.status_code == 201:
        print('customer created')
        return response.json()['objectCreated']['_id']
    return None

def create_savings_account(CustomerID, nickname):
    # Create a Savings Account
    url = 'http://api.nessieisreal.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
    payload = {
      "type": "Savings",
      "nickname": "test",
      "rewards": 0,
      "balance": 0,	
    }
    response = requests.post( 
        url, 
        data=json.dumps(payload),
        headers={'content-type':'application/json'},
        )
    if response.status_code == 201:
        print('account created')
        return response.json()['objectCreated']['_id']
    return None

def deposit(AccountNumber, DollarAmount):
    # Deposit money into account
    url = 'http://api.nessieisreal.com/accounts/{}/deposits?key={}'.format(AccountNumber,apiKey)
    payload = {
      "medium": "balance",
      "transaction_date": datetime.datetime.now().isoformat(),
      "status": "pending",
      "amount": DollarAmount,
      "description": "Deposit $" + str(DollarAmount)
    }
    response = requests.post( 
        url, 
        data=json.dumps(payload),
        headers={'content-type':'application/json'},
        )
    if response.status_code == 201:
        print('deposit created')
        return response.json()['objectCreated']['_id']
    return None

def withdraw(AccountNumber, DollarAmount):
    # Withdraw money from account
    url = 'http://api.nessieisreal.com/accounts/{}/withdrawals?key={}'.format(AccountNumber,apiKey)
    payload = {
      "medium": "balance",
      "transaction_date": datetime.datetime.now().isoformat(),
      "status": "pending",
      "amount": DollarAmount,
      "description": "Withdraw $" + str(DollarAmount)
    }
    response = requests.post( 
        url, 
        data=json.dumps(payload),
        headers={'content-type':'application/json'},
        )
    if response.status_code == 201:
        print('withdrawal created')
        return response.json()['objectCreated']['_id']
    return None