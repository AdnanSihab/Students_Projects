def calculator():
    print("Welcome to Calculator")
    num_a = int(input("a = "))
    num_b = int(input("b = "))
    print("What would you like to do")
    print("Instructions: \n1. Press 1 for addition\n2. Press 2 for subtraction\n3. Press 3 for multiplication\n4. Press 4 for division\n5. Press 5 for exponent\n6. Press 6 for square root")
    operation = int(input("Enter your choice: "))
    
    if operation == 1:
        print(num_a + num_b)
    elif operation == 2:
        print(num_a - num_b)
    elif operation == 3:
        print(num_a * num_b)
    elif operation == 4:
        print(num_a / num_b)
    elif operation == 5:
        print(num_a ** num_b)
    elif operation == 6:
        print(num_a ** 0.5)
    else:
        print("Invalid choice")

def guessing_game():
    print("Welcome to Guessing Game")
    print("The game is available for 4 to 6 years old")
    age = int(input("Your age: "))
    numbers_to_guess = [2, 3, 4]
    guessed_numbers = ["Two", "Three", "Four"]
    score = 0
    
    if 4 <= age <= 6:
        i = 0
        while i < 3:
            number_to_guess = numbers_to_guess[i]
            print("Here is the number:", number_to_guess)
            print("Please guess the number")
            guessed_number = input("Guessed number: ")
            
            if guessed_number == guessed_numbers[i]:
                print("You guessed the right number")
                print("Thanks for playing")
                score += 1
            else:
                print("You did not guess the right number")
                print("Try it again")
            
            i += 1
            print("Your score is:", score)
    else:
        print("You do not play the game")

def algebra():
    print("Welcome to Algebra")
    memorize_laws = int(input("1. Memorize laws: "))
    take_exam = int(input("2. Exam: "))
    
    if memorize_laws == 1:
        print("Memorize these laws: ...")  # Display the algebraic laws
    elif take_exam == 2:
        print("Exam is starting")
        questions = ["(2a+3b)^2", "(2x+3y)^3", "(If m+1/m =a, m^3+1/m^3 =?)"]
        answers = ["4a^2+12ab+9b^2", "8x^3+36x^2y+54xy^2+27y^3", "a^3-3a"]
        score = 0
        
        for i in range(3):
            question = questions[i]
            print("Question:", question)
            user_answer = input("Answer: ")
            
            if user_answer == answers[i]:
                print("Your answer is correct")
                score += 1
            else:
                print("Your answer is incorrect")
        
        print("Your score is:", score)
    else:
        print("You pressed the wrong number")

def temperature_indicator():
    print("Welcome to Temperature Indicator")
    convert_celsius = int(input("1. Celsius to Fahrenheit and Kelvin\n2. Fahrenheit to Celsius and Kelvin\n3. Kelvin to Fahrenheit and Celsius\nEnter your choice: "))
    
    if convert_celsius == 1:
        temp_celsius = float(input("Temperature in Celsius = "))
        print("Fahrenheit =", ((temp_celsius * 9) / 5) + 32)
        print("Kelvin =", (temp_celsius + 274.15))
    elif convert_celsius == 2:
        temp_fahrenheit = float(input("Temperature in Fahrenheit = "))
        print("Celsius =", ((temp_fahrenheit - 32) * 5) / 9)
        print("Kelvin =", (temp_fahrenheit + 274.15))
    elif convert_celsius == 3:
        temp_kelvin = float(input("Temperature in Kelvin = "))
        print("Fahrenheit =", ((temp_kelvin * 9) / 5) + 32)
        print("Celsius =", ((temp_kelvin - 32) * 5) / 9)
    else:
        print("You pressed the wrong number")

def multiplication_table():
    print("Welcome to Multiplication Table")
    number_to_multiply = int(input("Enter a number: "))
    
    for i in range(1, 11):
        print(f"{number_to_multiply} X {i} = {number_to_multiply * i}")

def main():
    print("Welcome to ALLROUNDER")
    print("To select a specific functionality, enter the corresponding number.")
    print("Instructions:")
    print("1. Press 1 to start Calculator\n2. Press 2 to start Guessing Game\n3. Press 3 to start Algebra\n4. Press 4 to start Temperature Indicator\n5. Press 5 to start Multiplication Table")
    
    user_choice = int(input("Enter your choice: "))
    
    if user_choice == 1:
        calculator()
    elif user_choice == 2:
        guessing_game()
    elif user_choice == 3:
        algebra()
    elif user_choice == 4:
        temperature_indicator()
    elif user_choice == 5:
        multiplication_table()
    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()