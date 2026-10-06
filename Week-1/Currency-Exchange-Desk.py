print("==============================")
print("      CURRENCY EXCHANGE")
print("==============================")

exchange_rate = float(input("Enter Exchange Rate: "))

usd_amount = float(input("USD Amount: "))

etb_amount = usd_amount * exchange_rate

print(f"\nExchange Rate: 1 USD = {exchange_rate:g} ETB")
print(f"\nETB Amount: {etb_amount:,.0f} ETB")

print("==============================")