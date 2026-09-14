#Welcome
print("="*100)
print("👾: Welcome to NumGuessr, a program that helps me, a computer guess your number!")
print("👾: You will now be requested to set the upper limit.")
print("👾: The number you want me to guess must be lower than the upper limit you set.")
times_played=0
while True:
    while True:
        inp_limit=input("👾: Enter upper limit (MAX 1,000,000,000): ")
        if inp_limit.replace(",","").isdigit() and int(inp_limit.replace(",",""))<=1000000000:
            set_upper=int(inp_limit.replace(",",""))
            break
        else:
            print("👾: Please enter a valid upper limit")

    #Successful setting of starting upper and lower limts
    set_lower=-1
    print("="*100)
    print(f"👾: Great! {set_upper} has been set as the upper limit!")

    print(f"👾: You are now requested to think of a number between 0 and {set_upper} (both inclusive).")
    set_upper+=1
    input("👾: Press Enter when ready! ")
    print("="*100)
    print("👾: If the number you have chosen is higher than my guess, type 'h'.")
    print("👾: If the number you have chosen is lower than my guess, type 'l'.")
    print("👾: If I correctly guesses your number, type 'c'.")

    #Guessing Mechanism
    attempts=0
    while True:
        if set_upper-set_lower<=1:
            times_played+=1
            ending="liar"
            break
            
        else:
            guess=(set_upper+set_lower)//2
            inq=input(f"👾: Is your number {guess}? (h/l/c): ").lower().strip()
            if inq not in ("h","l","c"):
                print("👾: That's not a valid response!")
            elif inq=="h":
                print("👾: Hmmm...")
                attempts+=1
                set_lower=guess
            elif inq=="l":
                print("👾: Hmmm...")
                attempts+=1
                set_upper=guess
            else:
                attempts+=1
                ending="gotans"
                ans=guess
                times_played+=1
                break
        
    if ending=="gotans":
        print("="*100)
        print(f"👾: I have successfully guessed your number as {ans}!")
        print(f"👾: It took me {attempts} attempts!")
        print("="*100)
    else:
        print("="*100)
        print("Caught Red-Handed! 🚨")
        print("Nice try! The math doesn't lie, even if you do. According to your previous responses, your secret number has been logically eliminated.")
        print("Integrity is about doing the right thing when no one is watching, and a game is only fun when everyone plays by the rules. As the saying goes, 'No legacy is so rich as honesty.' Let's start a fresh game!")
        print("="*100)

    while True:
        play_again=input("Play Again? (y/n): ").lower().strip()
        if play_again in ("y","n"):
            break
        else:
            print("That's not a valid response! Enter 'y' to play again or 'n' to stop playing.")
    if play_again=="n":
        break
print("="*100)
print(f"👾: You played a total of {times_played} times!!")
print("👾: Thank you for playing!")
print("="*100)