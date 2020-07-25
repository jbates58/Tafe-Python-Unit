


#  importing the required libraries and packages
import independentreserve as ir
import json
import requests
import configparser
import time



#  Below imports the required values from the config.ini file and then saves them to the respective variables
config = configparser.ConfigParser()
config.read('config.ini')

runAgain = "y"
apiKey = config.get('Default', 'api_key')
apiSecret = config.get('Default', 'api_secret')
withdrawFrequency = int(config.get('Default', 'withdraw_frequency'))
buyPercent = int(config.get('Default', 'buy_percentage'))
walletAddress = config.get('Default', 'wallet_address')
audBal = 0
usdtBal = 0
buyAmount = 0
withdrawInterger = 0
withdrawReset= 0



api = ir.PrivateMethods(apiKey, apiSecret)


#  run the API call to get the AUD balance and store it in the correct variables
def walletBalance():
    global audBal
    global usdtBal
    global buyAmount
    accountListDload = api.get_accounts()
    for account in accountListDload:
        #print(account["CurrencyCode"], ":", account["AvailableBalance"])
        audBal = account["CurrencyCode",'Aud']["AvailableBalance"]
        usdtBal = account["CurrencyCode",'Aud']["AvailableBalance"]
        break
    buyAmount = format((audBal/100)*buyPercent, ".2f")
    print("Your Current Account Balance in AUD is: $", audBal)
    print("based upon the inputted buy percentage, i will place a market buy order for: ", buyPercent, "% of your current account balance")
    print(buyPercent, "% of $", audBal, "is equal to: $", buyAmount)


#  Place market order for buyAmount of AUD into USDT
def buyOrder():
    print("Placing market order for: $", buyAmount, "USDT")
    # print("Placing market order for: $", buyAmount, "AUD worth of USDT")    <---- This line is what i need to fix. it purchases buyAmount of primart currency, not AUD worth of primary
    #buyOrder = api.place_market_order(volume=buyAmount, primary_currency_code="Usdt", secondary_currency_code="Aud", order_type="MarketBid")
    print("Market buy order completed.")



#  Automaticvally withdraw 100% of the USDT Balance to the specified Wallet address
def withdrawal():
    global withdrawInterger
    global withdrawReset
    if withdrawReset == withdrawFrequency:
        print("Processing withdrawal #", withdrawInterger, "For a total amount of $", usdtBal, "To the specified wallet ", walletAddress)
        #withdraw = api.withdraw_digital_currency(primaryCurrencyCode="Usdt", amount=int(usdtBal), withdrawal_address=walletAddress, comment="Python Test")
        print("Withdrawal complete")
        withdrawReset = 0
    else:
        print(withdrawFrequency, " Days has not yet elapsed, so withdrawal is not processed")
        withdrawInterger = withdrawInterger + 1
        withdrawReset = withdrawReset + 1




while runAgain == "y":
    #  Run the functions and Print out the relevent information for the user to see
    print("The entered API key is: ", apiKey)
    print("The percentage of your account to buy daily is: ", buyPercent, "%")
    print("The period between withdrawals is: ", withdrawFrequency, "Days")
    print("The Entered withdrawal wallet address is: ", walletAddress, "\n\n\n")
    print("Withdrawal Interger: ", withdrawInterger)
    print("Withdrawal Reset: ", withdrawReset)

    walletBalance()
    time.sleep(1)
    buyOrder()
    time.sleep(1)
    withdrawal()
    runAgain = input("\n\nDo you want to run the script again?")
