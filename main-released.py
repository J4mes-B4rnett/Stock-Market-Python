import requests
import time
import os
import json
import pytz
import datetime
from math import log10, floor

stock_type = str(input("Stock Type: "))
clearConsole = lambda: os.system('cls')

accounts = {"Changeme": 50000}
sharesCount = {"Changeme": 0}

api_url = 'https://api.coinmarketcap.com/v1/ticker/' + stock_type.lower() + '/'
response = requests.get(api_url)
response_json = response.json()
response_dict = {}
response_dict = response_json[0]

def updateAPI():
	api_url = 'https://api.coinmarketcap.com/v1/ticker/' + stock_type.lower() + '/'
	response = requests.get(api_url)
	response_json = response.json()
	response_dict = {}
	response_dict = response_json[0]
	price = round(float(response_dict['price_usd']), 3)

print(" ")
symb = str(response_dict['symbol'])
length = len(symb) + len(stock_type) + 4

print("#" * length)
print("{0}, ({1})".format(stock_type, symb))
print("#" * length)

print(" ")

price = round(float(response_dict['price_usd']), 3)
print("{1} Live Price (USD), ${0}".format(price, stock_type))
print(" ")

perch_h = round(float(response_dict['percent_change_1h']))
print("{1} Live Percent Change (1h), {0}%".format(perch_h, stock_type))

perch_d = round(float(response_dict['percent_change_24h']))
print("{1} Live Percent Change (24h), {0}%".format(perch_d, stock_type))

perch_w = round(float(response_dict['percent_change_7d']))
print("{1} Live Percent Change (1w), {0}%".format(perch_w, stock_type))

current_upkeep_h = round(float(response_dict['price_usd']), 2)
print(" ")

def command_line_input():
	command_line = str(input("Command ? for list: "))

	print(" ")
	print(" ")
	print("######################")
	if command_line.lower() == "?":
		print("List: ")
		print(" ")
		print("Buy Stock (BS)")
		print("Sell Stock (SS)")
		print("Review Portfolio (Rpo)")
		print("Update Stock Info (Usi)")
		print("#######################")
		print(" ")
		print(" ")

	elif command_line.lower() == "usi":
		updateAPI()

		print(" ")
		symb = str(response_dict['symbol'])
		length = len(symb) + len(stock_type) + 4

		print("#" * length)
		print("{0}, ({1})".format(stock_type, symb))
		print("#" * length)

		print(" ")

		price = round(float(response_dict['price_usd']), 3)
		print("{1} Live Price (USD), ${0}".format(price, stock_type))
		print(" ")

		perch_h = round(float(response_dict['percent_change_1h']))
		print("{1} Live Percent Change (1h), {0}%".format(perch_h, stock_type))

		perch_d = round(float(response_dict['percent_change_24h']))
		print("{1} Live Percent Change (24h), {0}%".format(perch_d, stock_type))

		perch_w = round(float(response_dict['percent_change_7d']))
		print("{1} Live Percent Change (1w), {0}%".format(perch_w, stock_type))

		current_upkeep_h = round(float(response_dict['price_usd']), 2)
		print(" ")

	elif command_line.lower() == "bs":
		shares = int(input("Share count: "))
		price_total = shares * price

		print("Price: ${}".format(price_total))
		double_check = str(input("Confirmation? (Y, N): "))

		if double_check == "Y":
			updateAPI()
			name = str(input("Full Name: "))

			if float(accounts[name]) >= price_total:
				print(" ")
				print("-" * 11)
				print("<<< Total ${}".format(accounts[name]))
				accounts[name] -= price_total
				sharesCount[name] += shares
				print(">>> Total ${}".format(accounts[name]))
				print(">>> Total Shares {}".format(sharesCount[name]))

				print("-" * 11)
				print(" ")
				time.sleep(1)
			elif float(accounts[name]) < price_total:
				print(" ")
				print("###################")
				print("Insufficient Funds.")
				print("###################")
				print(" ")
	elif command_line.lower() == "ss":
		shares = int(input("Share Count: "))
		price_total = shares * price
		double_check = str(input("Confirmation? (Y, N): "))

		if double_check == "Y":
			updateAPI()
			name = str(input("Full Name: "))

			print(" ")
			print("-" * 11)
			print("<<< Total ${}".format(accounts[name]))
			print("<<< Total Shares {}".format(sharesCount[name]))
			accounts[name] += price_total
			sharesCount[name] -= shares
			print("~" * 11)
			print(">>> Total ${}".format(accounts[name]))
			print(">>> Total Shares {}".format(sharesCount[name]))
			print("-" * 11)
			print(" ")
			time.sleep(1)

	elif command_line.lower() == "rpo":
		name = str(input("Full Name: "))
		print("Shares: {}".format(sharesCount[name]))
		print("#" * 16)

while True: 
	command_line_input()

accounts_json.close()
shares_json.close()
