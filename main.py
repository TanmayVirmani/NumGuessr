#Defining functions

def welcome():
    border_design()
    print("👾: Welcome to NumGuessr, a program that helps me, a computer guess your number!")
    print("👾: You will now be requested to set the upper limit.")
    print("👾: The number you want me to guess must be lower than the upper limit you set.")

def border_design():
    print("="*100)

def get_upper_limit():
    while True:
            inp_limit=input("👾: Enter upper limit (MAX 1,000,000,000): ")
            clean_inp=(inp_limit.replace(",",""))
            if clean_inp.isdigit() and int(clean_inp)<=1000000000:
                set_upper=int(clean_inp)
                border_design()
                print(f"👾: Great! {set_upper} has been set as the upper limit!")
                return(set_upper)
            else:
                print("👾: Please enter a valid upper limit")

def instructions():
    input("👾: Press Enter when ready! ")
    border_design()
    print("👾: If the number you have chosen is higher than my guess, type 'h'.")
    print("👾: If the number you have chosen is lower than my guess, type 'l'.")
    print("👾: If I correctly guesses your number, type 'c'.")

def get_response(guess):
    while True:
        inquire=input(f"👾: Is your number {guess}? (h/l/c): ").lower().strip()
        if inquire not in ("h","l","c"):
            print("👾: That's not a valid response!")
        else:
            return inquire


def play_round(set_upper, set_lower):
    attempts=0
    while True:
        if set_upper-set_lower<=1:
            return "liar", None, None                  
            
        else:
            guess=(set_upper+set_lower)//2
            inq=get_response(guess)
            if inq=="h":
                print("👾: Hmmm...")
                attempts+=1
                set_lower=guess
            elif inq=="l":
                print("👾: Hmmm...")
                attempts+=1
                set_upper=guess
            else:
                attempts+=1
                ans=guess
                return "gotans", ans, attempts

def re_play():
    while True:
            play_again=input("Play Again? (y/n): ").lower().strip()
            if play_again in ("y","n"):
                return play_again
            else:
                print("That's not a valid response! Enter 'y' to play again or 'n' to stop playing.")

def game_over(times_played):
    border_design()
    print(f"👾: You played a total of {times_played} times!!")
    print("👾: Thank you for playing!")
    border_design()

def main(times_played):
    while True:
        set_upper=get_upper_limit()
        set_lower=-1
        print(f"👾: You are now requested to think of a number between 0 and {set_upper} (both inclusive).")
        set_upper+=1
        instructions()
        #Guessing Mechanism
        round_result, ans, attempts=play_round(set_upper, set_lower)

        if round_result=="gotans":
            border_design()
            print(f"👾: I have successfully guessed your number as {ans}!")
            print(f"👾: It took me {attempts} attempts!")
            times_played+=1
            border_design()
        else:
            border_design()
            print("Caught Red-Handed! 🚨")
            print("Nice try! The math doesn't lie, even if you do. According to your previous responses, your secret number has been logically eliminated.")
            print("Integrity is about doing the right thing when no one is watching, and a game is only fun when everyone plays by the rules. As the saying goes, 'No legacy is so rich as honesty.' Let's start a fresh game!")
            times_played+=1
            border_design()

        play_again=re_play()
        if play_again=="n":
            return times_played

#------------------------------------------------------------------
welcome()
times_played=0
times_played=main(times_played)
game_over(times_played)