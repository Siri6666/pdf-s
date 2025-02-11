#CURRENCY CONVERTER PROJECT
import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][target_currency]
        return rate
    else:
        print("Failed to fetch exchange rate data.")
        return None

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is not None:
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

def main():
    print("Welcome to the Currency Converter Program!")
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency you're converting from (3-letter code, e.g., USD): ").upper()
    to_currency = input("Enter the currency you're converting to (3-letter code, e.g., EUR): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Failed to convert currency. Please try again.")

if __name__ == "__main__":
    main()
