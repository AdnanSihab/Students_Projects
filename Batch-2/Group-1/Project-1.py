print("Welcome To Our Advanced Converter And Calculator.")
print("This project is on behalf of boys in the Python course from Batch 2.")
print("Fully Made By Niamul Kabir Afif.")

def calculate_bmi(weight, height):
    bmi_value = weight / (height * height)
    print(f"Your BMI: {bmi_value:.2f}")
    
    if bmi_value < 18.5:
        print('Underweight')
    elif 18.5 <= bmi_value < 25:
        print("Normal")
    elif 25 <= bmi_value < 30:
        print('Overweight')
    else:
        print('Obesity')


def currency_converter(from_currency, to_currency, amount):
    exchange_rates = {'bdt': 0.0091, 'usd': 109.25}
    
    if from_currency in exchange_rates and to_currency in exchange_rates:
        converted_amount = amount * exchange_rates[from_currency] / exchange_rates[to_currency]
        print(f"{amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}")
    else:
        print("Invalid currency. Please run again.")


def temperature_converter(from_unit, to_unit, amount):
    if from_unit.lower() == "celsius" and to_unit.lower() == "fahrenheit":
        converted_temp = (amount * 1.8) + 32
        print(f"{amount} °C = {converted_temp:.2f} °F")
    elif from_unit.lower() == "fahrenheit" and to_unit.lower() == "celsius":
        converted_temp = (amount - 32) * 5 / 9
        print(f"{amount} °F = {converted_temp:.2f} °C")
    else:
        print("Invalid temperature units. Please run again.")


def height_converter(from_unit, to_unit, amount):
    if from_unit.lower() == "feet" and to_unit.lower() == "meter":
        converted_height = amount * 0.305
        print(f"{amount} Feet = {converted_height:.2f} Meter")
    elif from_unit.lower() == "meter" and to_unit.lower() == "feet":
        converted_height = amount * 3.28
        print(f"{amount} Meter = {converted_height:.2f} Feet")
    else:
        print("Invalid height units. Please run again.")


def kg_to_pound_converter(from_unit, to_unit, amount):
    kg_to_pound = 2.205
    pound_to_kg = 0.454
    
    if from_unit.lower() == "kg" and to_unit.lower() == "pound":
        converted_amount = amount * kg_to_pound
        print(f"{amount} KG = {converted_amount:.2f} Pound")
    elif from_unit.lower() == "pound" and to_unit.lower() == "kg":
        converted_amount = amount * pound_to_kg
        print(f"{amount} Pound = {converted_amount:.2f} KG")
    else:
        print("Invalid weight units. Please run again.")

user_input = input("Available Methods: 1) Calculate BMI, 2) Currency Converter, 3) Temperature Converter, 4) Height Converter, 5) Weight Converter (KG to Pound)\nWhat Are You Doing Today?\nAnswer: ")

if user_input == "1" or user_input.lower() == "calculate bmi":
    weight = float(input("Enter your weight in KG: "))
    height = float(input("Enter your height in Meter: "))
    calculate_bmi(weight, height)

elif user_input == "2" or user_input.lower() == "currency converter":
    from_currency = input("Enter your source currency (e.g., BDT): ").lower()
    to_currency = input("Enter your target currency (e.g., USD): ").lower()
    amount = float(input("Enter the amount: "))
    currency_converter(from_currency, to_currency, amount)

elif user_input == "3" or user_input.lower() == "temperature converter":
    from_unit = input("Enter your source temperature unit (e.g., Celsius): ")
    to_unit = input("Enter your target temperature unit (e.g., Fahrenheit): ")
    amount = float(input("Enter the temperature: "))
    temperature_converter(from_unit, to_unit, amount)

elif user_input == "4" or user_input.lower() == "height converter":
    from_unit = input("Enter your source height unit (e.g., Feet): ")
    to_unit = input("Enter your target height unit (e.g., Meter): ")
    amount = float(input("Enter the height: "))
    height_converter(from_unit, to_unit, amount)

elif user_input == "5" or user_input.lower() == "weight converter":
    from_unit = input("Enter your source weight unit (e.g., KG): ")
    to_unit = input("Enter your target weight unit (e.g., Pound): ")
    amount = float(input("Enter the weight: "))
    kg_to_pound_converter(from_unit, to_unit, amount)
