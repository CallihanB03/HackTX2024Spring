# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json
import datetime
import time

apiKey = '2562b2e98f7a38a09dbaa132bece8b56'
UserID = '65ff2dc99683f20dd51898da'
AccountID = '65ff2e1b9683f20dd51898db'


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
    url = 'http://api.nessieisreal.com/customers/{}/accounts?key={}'.format(CustomerID,apiKey)
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
        print('account created: ' + response.json()['objectCreated']['_id'])
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

def get_balance(AccountNumber):
    # Get balance of account
    url = 'http://api.nessieisreal.com/accounts/{}?key={}'.format(AccountNumber,apiKey)
    response = requests.get( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 200:
        print('balance retrieved')
        return response.json()['balance']
    return None

def delete_account(AccountNumber):
    # Delete account
    url = 'http://api.nessieisreal.com/accounts/{}?key={}'.format(AccountNumber,apiKey)
    response = requests.delete( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 204:
        print('account deleted')
        return True
    return False

def delete_all_accounts():
    # Delete all accounts
    url = 'http://api.nessieisreal.com/accounts?key={}'.format(apiKey)
    response = requests.get( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 200:
        accounts = response.json()
        for account in accounts:
            delete_account(account['_id'])
        return True
    return False

def get_all_deposits(AccountNumber):
    # Get all deposits of account
    url = 'http://api.nessieisreal.com/accounts/{}/deposits?key={}'.format(AccountNumber,apiKey)
    response = requests.get( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 200:
        print('deposits retrieved')
        return response.json()
    return None

def get_deposit(DepositID):
    # Get deposit
    url = 'http://api.nessieisreal.com/deposits/{}?key={}'.format(DepositID,apiKey)
    response = requests.get( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 200:
        print('deposit retrieved')
        return response.json()
    return None

def get_deposit_date(DepositID):
    # Get deposit date
    url = 'http://api.nessieisreal.com/deposits/{}?key={}'.format(DepositID,apiKey)
    response = requests.get( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 200:
        print('deposit date retrieved')
        return response.json()['transaction_date']
    return None

def get_deposit_amount(DepositID):
    # Get deposit amount
    url = 'http://api.nessieisreal.com/deposits/{}?key={}'.format(DepositID,apiKey)
    response = requests.get( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 200:
        print('deposit amount retrieved')
        return response.json()['amount']
    return None

def get_deposit_status(DepositID):
    # Get deposit status
    url = 'http://api.nessieisreal.com/deposits/{}?key={}'.format(DepositID,apiKey)
    response = requests.get( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 200:
        print('deposit status retrieved')
        return response.json()['status']
    return None

def get_all_withdrawals(AccountNumber):
    # Get all withdrawals of account
    url = 'http://api.nessieisreal.com/accounts/{}/withdrawals?key={}'.format(AccountNumber,apiKey)
    response = requests.get( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 200:
        print('withdrawals retrieved')
        return response.json()
    return None

def get_withdrawal(WithdrawalID):
    # Get withdrawal
    url = 'http://api.nessieisreal.com/withdrawals/{}?key={}'.format(WithdrawalID,apiKey)
    response = requests.get( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 200:
        print('withdrawal retrieved')
        return response.json()
    return None

def get_withdrawal_date(WithdrawalID):
    # Get withdrawal date
    url = 'http://api.nessieisreal.com/withdrawals/{}?key={}'.format(WithdrawalID,apiKey)
    response = requests.get( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 200:
        print('withdrawal date retrieved')
        return response.json()['transaction_date']
    return None

def get_withdrawal_amount(WithdrawalID):
    # Get withdrawal amount
    url = 'http://api.nessieisreal.com/withdrawals/{}?key={}'.format(WithdrawalID,apiKey)
    response = requests.get( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 200:
        print('withdrawal amount retrieved')
        return response.json()['amount']
    return None

def get_withdrawal_status(WithdrawalID):
    # Get withdrawal status
    url = 'http://api.nessieisreal.com/withdrawals/{}?key={}'.format(WithdrawalID,apiKey)
    response = requests.get( 
        url,
        headers={'content-type':'application/json'},
        )
    if response.status_code == 200:
        print('withdrawal status retrieved')
        return response.json()['status']
    return None



#deposit(AccountID,100)
while True:
    print(get_balance(AccountID))
    time.sleep(3)