def welcome_message():
    print("""
        Welcome to the Geography Quiz!
        Test your knowledge about different countries and landmarks.

        Let's get started!
    """)

def get_play_choice():
    while True:
        answer = input("Do you want to play? (y/n) ans=")
        answer = answer.lower()
        if answer in ["y", "n"]:
            if answer == "y":
                print("Let's start!")
                break
            else:
                print("Maybe next time. Goodbye!")
                exit()
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

def ask_question(question, option1, option2, option3, correct_option):
    print(question)
    print("a) " + option1)
    print("b) " + option2)
    print("c) " + option3)
    answer = input("ans=")
    
    if answer.lower() in ["a", "b", "c"]:
        return answer.lower() == correct_option
    else:
        print("Invalid choice. Skipping question.")
        return False

def run_quiz():
    welcome_message()
    get_play_choice()
    score = 0

    if ask_question("1. What is the capital of France?", "Paris", "Madrid", "Berlin", "a"):
        score += 1

    if ask_question("2. Which river is the longest in the world?", "Nile", "Amazon", "Yangtze", "b"):
        score += 1

    if ask_question("3. In which continent is Egypt located?", "Africa", "Asia", "Europe", "a"):
        score += 1

    if ask_question("4. What is the highest mountain in the world?", "Mount Kilimanjaro", "Mount Everest", "K2", "b"):
        score += 1

    if ask_question("5. Which desert is the largest in the world?", "Sahara Desert", "Arabian Desert", "Gobi Desert", "a"):
        score += 1

    print(f"You got {score}/5 marks")
    print(f"Your score is {(score/5)*100}%")

if __name__ == "__main__":
    run_quiz()
