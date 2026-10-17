import random
username = input("ENTER YOUR NAME  :-  ")
print(f"WELCOME {username}")
while True:
    levels = int(input(
        "PLEASE SELECT YOUR DIFFICULTY LEVEL\n"
        "1: EASY\n"
        "2: MEDIUM\n"
        "3: HARD\n"
        "Enter your choice: "))
    if levels == 1:
        bot = random.randint(1, 20)
        attempts = 10
    elif levels == 2:
        bot = random.randint(1, 50)
        attempts = 8
    elif levels == 3:
        bot = random.randint(1, 100)
        attempts = 5
    else:
        print("please select a level")
        exit()
    print(f"YOU HAVE {attempts}LIFELINES")
    while True:
        user = int(input("enter a number :- "))
        if bot == user :
            print("WOW !!! YOUR GUESS IS CORRECT ")
            break
        elif bot < user :
            attempts = attempts-1
            if attempts==0:
                print('gameover!')
                break
            print(f"TRY AGAIN.. YOU HAVE {attempts} LIFELINE LEFT  ")
            print("YOUR GUESS IS HIGH")
        elif bot > user:
            attempts = attempts-1
            if attempts==0:
                print("game over!")
                break
            print("you guess is low....")
            print(f"TRY AGAIN.. YOU HAVE {attempts}LIFELINE LEFT ")

        else:
            print("invalid input")
            break
    
    play_again = input("Do you want to play again? yes/no: ").lower()
    if play_again == "no":
        print("THANKS FOR PLAYING!")
        break
