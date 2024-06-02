import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200 or data['result'] != 'success':
        print("Error fetching exchange rate")
        return None
    
    return data['conversion_rate']

def convert_currency(amount, rate):
    return amount * rate

def main():
    api_key = 'ada4d268e4de486054292e95'
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))
    
    rate = get_exchange_rate(api_key, base_currency, target_currency)
    if rate is not None:
        converted_amount = convert_currency(amount, rate)
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    else:
        print("Failed to retrieve exchange rate.")

if __name__ == "__main__":
    main()
