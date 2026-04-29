# Mini accounting app solution
This mini web app allows to make simple records about accounting processes in business.

## Description

This app has 6 navigation tabs for simple accounting process.

### Create Transaction

Allows user to create send/receive transaction to specified partner.

### Receive Payment

Allows user to receive cash from specified customer.

### Pay vendor

Allows user to send money to specified vendor

### Transactions

Shows all transactions made by user and postings (logic part of app)

### Partner Ledger

Shows users' partner balances:
positive value - partner owes
negative value - user owes

### Statistics

Shows Profit and Loss stats for business:

__1. Revenue__

How much user earned

__2. Expenses__

How much user spent

__3. Waiting to receive__

Transactions, that user has not received yet

__4. Waiting to pay__

Transactions, that user has not paid yet

__5. Profit__

Revenue and expenses correlation

__6. Cash__

Currently held money by user

## Getting Started

If you want to test out this app, here is what you need.

### Requirements

Python version: 3.9+

### Installation

* Open command line
* Clone this repo
```
git clone https://github.com/Denial-First/mini-accounting-app.git
```
* Open repo folder
```
cd mini-accounting-app
```
* Install dependencies
```
pip install -r requirements.txt
```
* Run the app
```
streamlit run app.py
```
* Open following link in browser and test the app
```
http://localhost:8501
```

## Author

Denys Symotiuk

