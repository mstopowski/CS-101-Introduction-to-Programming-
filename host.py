class Host:
    def __init__(self):
        pass

    def welcome(self):
        print("""
        Goodafternoon and welcome to the show
        /-----------------------------------/
        
            WHO WANTS TO BE A MILLIONAIRE?
        
        /-----------------------------------/
        """)

    def introduce_gamer(self):
        print("""
        On tonight's show we have with us a new contestant.
        Please, be so kind and intriduce yourself.
        What is your name?
        """)    
        gamer_name = input("ENTER YOUR NAME: ")
        print("Hi " + gamer_name + "! Tell us where are your from?")
        gamer_city = input("ENTER THE NAME OF YOUR CITY: ")
        print("So you are from " + gamer_city + " " + gamer_name + ".")
        return gamer_name, gamer_city
    
    def do_we_start_the_game(self, gamer_name):
        print(gamer_name + ",are you ready to become a milionaire?")
        _play = input("TYPE YES OR NO: ").lower()
        return _play

    def ask_question(self, q_and_a, q_numb):
        print("Here is the question number " + str(q_numb) + " for you.")
        print("/-----------------------------------/")
        print(q_and_a[0])
        print("")
        print("Here are available answers:")
        print("1: " + q_and_a[1])
        print("2: " + q_and_a[2])
        print("3: " + q_and_a[3])
        print("4: " + q_and_a[4])
        print(" ")

    def check_answer(self, q_and_a, sel_answer, answer):
        if q_and_a[sel_answer] == answer:
            print("It's a correct answer!")
            return True
        else:
            print("I'm sorry, but that's wrong.")
            return False
    
    def prize_info(self, money, gamer_money):
        print("Your win: " + str(money))
        print("Your current winnings: " + str(gamer_money))
        print(" ")
