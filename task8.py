from random import randint
choice_map = {1: "Rock", 2: "Paper", 3: "Scissors"}
def user_choice():
    while True:
        try:
            u_choice = int(input("Choose 1 for Rock,2 for Paper,3 for Scissor: "))
            p_choice = randint(1,3)
            u_choice_name = choice_map[u_choice]
            p_choice_name = choice_map[p_choice]
            if (u_choice == 1 and p_choice == 3) or (u_choice == 2 and p_choice == 1) or (u_choice == 3 and p_choice == 2):
                print(f"You win! You chose {u_choice_name} and PC chose {p_choice_name}")
                return 1
            elif u_choice == p_choice:
                print(f"It's a draw! You chose {u_choice_name} and PC chose {p_choice_name}")
                return 0
            else:
                print(f"You lose! You chose {u_choice_name} and PC chose {p_choice_name}")
                return -1
        except:
            print(f"{u_choice} is not a option! Try again")
            return user_choice()

def game():
    user_score = 0
    pc_score = 0
    while user_score < 3 and pc_score < 3:
        result = user_choice()
        if result == 1:
            user_score += 1
        elif result == -1:
            pc_score += 1
        print(f"Score: You {user_score} - {pc_score} PC")

    if user_score == 3:
        print("Hey! You win!")
    else:
        print("Sorry! You lose")


game()