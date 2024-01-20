def welcome_message():
    print("""
        'Banglar rup ami dekhiachi, tai pritibir rup kujite jai na ar'
        Independent Bangladesh was born on December 16, 1971 after breaking the chains of subjugation.
        Beloved Bangladesh has become known as a wonder to the whole world by carrying the cultural abundance 
        along with the history of liberation war along with the natural beauty.

        How much we know about our motherland?

        Let's check!
    """)

def get_play_choice():
    while True:
        answer = input("Do you want to play? (i/ii/iii) ans=")
        answer = answer.lower()
        if answer in ["i", "ii", "iii"]:
            print("Let's start!")
            break
        else:
            print("Invalid choice. Please enter 'i', 'ii', or 'iii'.")


def ask_question(question, option1, option2, option3):
    print(question)
    print("i) " + option1)
    print("ii) " + option2)
    print("iii) " + option3)
    answer = input("ans=")
    return answer.lower()

def evaluate_answer(q_number, user_answer, correct_answer, score):
    user_answer = user_answer.lower()
    correct_answer = correct_answer.lower()

    options = ["i", "ii", "iii"]
    
    if user_answer in options and user_answer == correct_answer:
        print(f"{q_number}. Correct")
        return score + 1
    else:
        print(f"{q_number}. Incorrect")
        return score




def run_quiz():
    welcome_message()
    score = 0

    score = evaluate_answer(1, ask_question("1. What is the full name of 'Bangladesh'?", "Bangladesh", 
                                              "People's Republic of Bangladesh", "Republic Bangladesh"), "ii", score)
    score = evaluate_answer(2, ask_question("2. When was the Mujibnagar government formed?", 
                                              "10 April, 1971", "10 January, 1971", "23 March, 1910"), "i", score)
    score = evaluate_answer(3, ask_question("3. Who is the main director of 'Concert for Bangladesh'?", 
                                              "pondit robishonkor", "Arijit Sing", "George Harrison"), "iii", score)
    score = evaluate_answer(4, ask_question("4. In which sector was Cox's Bazar included during the Liberation War?", 
                                              "2 no sector", "1 no sector", "11 no sector"), "ii", score)
    score = evaluate_answer(5, ask_question("5. Where is Sompur Mahavihar located?", "Nouga", "Dhaka", "Chottogram"), "i", score)
    score = evaluate_answer(6, ask_question("6. What is the duration of Bangabandhu Satellite 1?", "50 years", "15 years", "30 years"), "ii", score)
    score = evaluate_answer(7, ask_question("7. What is the economic sea limit of Bangladesh in nautical miles?", "200", "3000", "40"), "i", score)
    score = evaluate_answer(8, ask_question("8. What is the position of Bangladesh in the world in terms of freelancing?", "33", "10", "3"), "iii", score)
    score = evaluate_answer(9, ask_question("9. When did the historical student movement of Bangladesh begin?", "1971", "1972", "1962"), "iii", score)
    score = evaluate_answer(10, ask_question("10. Where was the first independent Bengali radio station established?", "Syllet", "Chottogram", "Dhaka"), "ii", score)

    print(f"You got {score}/10 marks")
    print(f"Your score is {(score/10)*100}%")

run_quiz()