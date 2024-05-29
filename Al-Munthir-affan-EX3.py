print("===========================")
print("Welcome to $$ EXCHANGE STORE $$")
print("===========================")

Currency_From = input("Exchange From (USD, EUR, SAR): ").upper()
user_money = float(input("How much? "))
Currency_To= input("Exchange To (USD, EUR, SAR): ").upper()

usd_sar = 3.75
usd_eur = 0.99

if (Currency_From == Currency_To):
    print(f"You will keep your amount {user_money}")
    exit()

elif (Currency_From == "USD" and Currency_To == "SAR"):
    amount = user_money * usd_sar

elif (Currency_From == "USD" and Currency_To == "EUR"):
    amount = user_money * usd_eur

elif (Currency_From == "EUR" and Currency_To == "USD"):
    amount = user_money / usd_eur

elif (Currency_From == "SAR" and Currency_To == "USD"):
    amount = user_money / usd_sar

elif (Currency_From == "EUR" and Currency_To == "SAR"):
    amount = (user_money / usd_eur) * usd_sar

elif (Currency_From == "SAR" and Currency_To == "EUR"):
    amount = (user_money / usd_sar) * usd_eur

else:
    print("PLease Choose From (USD, EUR, SAR)")
    exit()

print(f"You will give {user_money} {Currency_From}, and you will take {amount:.1f} {Currency_To}")

# ===========================    
# Welcome to $$ EXCHANGE STORE $$
# ===========================    
# Exchange From (USD, EUR, SAR): sar
# How much? 11400
# Exchange To (USD, EUR, SAR): usd
# You will give 11400.0 SAR, and you will take 3040.00 USD
