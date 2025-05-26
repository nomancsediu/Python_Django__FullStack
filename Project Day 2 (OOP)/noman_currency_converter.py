class CurrencyConverter:


    exchange_rates = {
        "USD": 1.0,     # Base currency
        "BDT": 121.75,  
        "EUR": 0.88,   
        "GBP": 0.75     
    }

    # Constructor to initialize
    def __init__(self, amount, from_currency, to_currency):
        self.amount = amount
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()

    # Main method to convert currency using exchange rates
    def convert(self):

        if self.from_currency not in CurrencyConverter.exchange_rates or \
           self.to_currency not in CurrencyConverter.exchange_rates:
            return "Invalid currency not in our system"

        # Convert amount to base currency (USD)
        base_amount = self.amount / CurrencyConverter.exchange_rates[self.from_currency]
        converted_amount = base_amount * CurrencyConverter.exchange_rates[self.to_currency]

        return round(converted_amount, 2)  # Round to 2 decimal places

    # Class method to update or add a currency exchange rate
    @classmethod
    def update_rate(cls, currency, new_rate):
        cls.exchange_rates[currency.upper()] = new_rate

    # Static method to check if a currency code is valid
    @staticmethod
    def is_valid_currency(code):
        return code.upper() in CurrencyConverter.exchange_rates


class Logger:
    def Log(self, user, converter):
        result = converter.convert()
        print(f"record: {user} converted {converter.amount} {converter.from_currency} -> {result} {converter.to_currency}")


# Main execution block
if __name__ == "__main__":

    # Taking user input
    amount = float(input("Enter amount: "))
    from_curr = input("Enter Your Currency: ")
    to_curr = input("Enter Your Desired Currency In Which You Want To Convert: ")
    user = input("Enter Your Name: ")


    converter = CurrencyConverter(amount, from_curr, to_curr)

    
    if not CurrencyConverter.is_valid_currency(from_curr) or not CurrencyConverter.is_valid_currency(to_curr):
        print("Invalid Currency — we don't have that currency.")
    else:
        # Creating Logger instance and logging the conversion
        Logger_object = Logger()
        Logger_object.Log(user, converter)
