# Use with Google Colab for best experience imo
import json

# Create empty JSON files if they don’t exist
with open("users.json", "w") as f:
    json.dump({'Adjoa':'1234',
    'Romel': '2345',
    'Newlove': '1998',
    'Joseph': '1192',
    'Alex': '2234',
    'Brian': '3345',
    'Catherine': '9876',
    'Diana': '2200',
    'Edward': '2020',
    'Fiona': '4990',
    'George': '1777',
    'Hannah': '1357',
    'Isaac': '1002',
    'Julia': '9087',
    'Kevin': '9999',
    'Laura': '1122',
    'Michael': '4664',
    'Nina': '6756',
    'Oscar': '0098',
    'Patricia': '0987',
    'Quentin': '9983'}, f)

with open("balances.json", "w") as f:
    json.dump({'Adjoa':10000,
    'Romel': 1000,
    'Newlove': 20000,
    'Joseph': 150000,
    'Alex': 43820,
    'Brian': 157230,
    'Catherine': 93210,
    'Diana': 84190,
    'Edward': 124500,
    'Fiona': 21450,
    'George': 182000,
    'Hannah': 120340,
    'Isaac': 94500,
    'Julia': 38600,
    'Kevin': 159300,
    'Laura': 75100,
    'Michael': 120000,
    'Nina': 64750,
    'Oscar': 112900,
    'Patricia': 58040,
    'Quentin': 152100}, f)

from PIL import Image, ImageDraw, ImageFont
from IPython.display import display, Image as IPImage
from google.colab import files
import datetime

def create_receipt_image(customer_name, transaction_type, amount, new_balance, file_name="receipt.png"):
    width, height = 250, 300
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", size=16)
    except:
        font = ImageFont.load_default()

    y = 20
    draw.text((75, y), "EAGLE BANK RECEIPT", fill="black", font=font)
    y += 30
    draw.text((0, y), "==========================================", fill="black", font=font)
    y += 30
    draw.text((10, y), f"Customer:    {customer_name}", fill="black", font=font)
    y += 30
    draw.text((10, y), f"Transaction:     {transaction_type}", fill="black", font=font)
    y += 30
    draw.text((10, y), f"Amount:     GHC {amount:.2f}", fill="black", font=font)
    y += 30
    draw.text((10, y), f"New Balance:        GHC {new_balance:.2f}", fill="black", font=font)
    y += 30
    draw.text((10, y), f"Date:    {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", fill="black", font=font)
    y += 30
    draw.text((70, y), "Thank you for banking with us!", fill="black", font=font)
    y += 30
    draw.text((0, y), "==========================================", fill="black", font=font)


    img.save(file_name)
    display(IPImage(file_name))
    files.download(file_name)
import json
import time
  


import requests
# Your Fixer API key
api_key = '721c82d10f51341f485f19d10782ffc5'

# List of desired currency symbols
symbols = ['USD', 'GBP', 'CHF', 'AUD', 'CAD', 'DKK', 'JPY', 'NZD', 'NOK', 'SEK', 'ZAR', 'EUR', 'CNY']

# Construct the symbols parameter as a comma-separated string
symbols_param = ','.join(symbols + ['GHS'])  # Include GHS to get its rate

# API endpoint
url = 'http://data.fixer.io/api/latest'

# Parameters for the API request
params = {
    'access_key': api_key,
    'symbols': symbols_param
}
# Make the GET request to the Fixer API
response = requests.get(url, params=params)

# Parse the JSON response
data = response.json()

balances = {}
users = {}

# Load the user credentials
with open("users.json", "r") as f:
    users = json.load(f)

# Load the banking balances
with open("balances.json", "r") as f:
    balances = json.load(f)
print(balances)
print(users)
while True:
    V = int(input('''Hi there! What do you want to do?
              1. Login
              2. Create new account '''))
    if V == 1:
        print('Redirecting to Login page...')
        time.sleep(2)
        break
    elif V == 2:
        A = int(input('''Do you want to create an account?
        1. Yes
        2. No
        '''))
        if A == 1:
            B = input('New Username: ')
            time.sleep(1.2)
            C = input('New Password: ')
            users[B] = C
            balances[B] = 0
            time.sleep(2)
            print('Account created')
        else:
            print('Goodbye')
while True:
    Login = input('Type in your username: ')
    Password = input('Type in your password: ')

    if Login in users and Password == users[Login]:
        time.sleep(3)
        print('Welcome to Eagle Bank')
       
    while True:
        X = int(input('''What do you wish to do?
                  1. Check balance
                  2. Deposit money
                  3. Withdraw money
                  4. Check current exchange rate
                  5. Log out
                  '''))
        time.sleep(2)

        if X == 1:
            print(f"{Login}'s balance is GHC {balances[Login]}")
            continue
        elif X == 2:
            D = float(input('How much are you depositing? '))
            balances[Login] += D
            create_receipt_image(Login, "Deposit", D, balances[Login])
            continue
        elif X == 3:
            E = float(input('How much are you withdrawing? '))
            if E > balances[Login]:
                print('Insufficent balance')
                continue
            balances[Login] -= E
            time.sleep(3)
            create_receipt_image(Login, "Withdrawal", E, balances[Login])
            continue
        elif X == 4:
            if data.get('success'):
                rates = data['rates']
                ghs_rate = rates.get('GHS')

            if ghs_rate:
                 print("Exchange Rates Relative to GHS:")
            for currency in symbols:
                currency_rate = rates.get(currency)
                if currency_rate:
                    rate_to_ghs = ghs_rate / currency_rate
                    print(f"1 {currency} = {rate_to_ghs:.4f} GHS")
                    time.sleep(1.5)
                    continue
        elif X == 5:
            print('''
            Do you want to log out?
            1. Yes
            2. No
              ''')
        y = int(input())
        if y == 1:
            break
        elif y == 2:
            continue
    else:
     print('Username not found.')