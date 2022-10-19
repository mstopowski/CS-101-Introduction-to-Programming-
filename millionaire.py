import host
import gamer
import questions
import prizes
import sys
import random

def main():
    host1 = host.Host()
    # host1.welcome()
    # gamer_name, gamer_city = host1.introduce_gamer()
    # gamer1 = gamer.Gamer(gamer_name, gamer_city)
    # _play = host1.do_we_start_the_game(gamer1.name)
    gamer1 = gamer.Gamer("maurycy", "gdansk")
    _play = "yes"
    if _play == "yes":
        list_of_questions = [i+1 for i in range(len(questions.questions_dict))] #[1, 2, 3, 4, 5]
        while gamer1.can_play == True and len(list_of_questions) > 0:
            question_index = random.randint(0, len(list_of_questions) - 1) #range(0,4)
            selected_question = questions.questions_dict[list_of_questions[question_index]] #question from dictionary
            host1.ask_question(selected_question, gamer1.questions_answered + 1)
            selected_answer = input("(SELECT AN ANSWER BY TYPING NUMBER) ").strip()
            valid_answer = host1.check_answer(selected_question, int(selected_answer), questions.answers_dict[list_of_questions[question_index]])
            if valid_answer == True:
                gamer1.questions_answered += 1
                gamer1.prize += prizes.prizes_dict[gamer1.questions_answered]
                list_of_questions.pop(question_index)
                host1.prize_info(prizes.prizes_dict[gamer1.questions_answered], gamer1.prize)
            else:
                print("Bye, bye")
                print("Your total winings: " + str(gamer1.prize))
                gamer1.can_play = False
        print("Congrats!")
        print("Your total winings: " + str(gamer1.prize))
        return
    

if __name__ == "__main__":
    main()
    sys.exit()