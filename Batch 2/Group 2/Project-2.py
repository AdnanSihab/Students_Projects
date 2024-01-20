def currency_converter():
    from_currency = input("Enter the source currency: ")
    to_currency = input("Enter the target currency: ")
    amount = float(input("Enter the amount: "))
    exchange_rate = float(input("Enter the exchange rate: "))

    original_amount = amount * exchange_rate
    converted_amount = int(original_amount)

    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
    
    reverse_exchange_rate = int(original_amount / amount)
    print(f"{converted_amount} {to_currency} = {reverse_exchange_rate} {from_currency}")

def health_assessment():
    name = input("Enter your name: ")
    gender = input("Enter your gender: ")
    age = int(input("Enter your age: "))
    weight = int(input("Enter your weight: "))
    height = int(input("Enter your height: "))

    if age <= 12:
        if weight <= 40 and height <= 5:
            print("You are normal.")
        elif weight > 40 and height <= 5:
            print("You are too fat.")
    elif age >= 13:
        if 30 <= weight <= 89 and height >= 5:
            print("You are fit.")
        elif weight >= 90 and height >= 5:
            print("You are too fat.")
        elif weight <= 45 and height <= 4:
            print("You are not fit.")

def main():
    print("Welcome to the Currency Converter and Health Assessment Program!")
    user_choice = input("Choose an option (1: Currency Converter, 2: Health Assessment): ")

    if user_choice == "1":
        currency_converter()
    elif user_choice == "2":
        health_assessment()
    else:
        print("Invalid choice. Please run again.")

main()