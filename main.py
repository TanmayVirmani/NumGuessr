import time
#Welcome
print("="*100)
print("👾: Welcome to NumGuessr, a program that helps me, a computer guess your number!")
print("👾: You will now be requested to set the upper limit.")
print("👾: The number you want me to guess must be lower than the upper limit you set.")
while True:
    upper_limit=input("👾: Enter upper limit (MAX 1,000,000,000): ")
    if upper_limit.replace(",","").isdigit() and int(upper_limit.replace(",",""))<=1000000000:
        set_upper=int(upper_limit.replace(",",""))
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
print("👾: If the number you have chosen is lower than myguess, type 'l'.")
print("👾: If I correctly guesses your number, type 'c'.")

#Guessing Mechanism
attempts=0
while True:
    if set_upper-set_lower==2:
        attempts+=1
        celeb="time"
        ans=(set_upper+set_lower)//2
        break
    else:
        guess=(set_upper+set_lower)//2
        inq=input(f"👾: Is your number {guess}? (h/l/c): ").lower()
        if inq !="h" and inq != "l" and inq != "c":
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
            celeb="gotans"
            ans=guess
            break
    
if celeb=="gotans":
    print("="*100)
    print(f"👾: I have successfully guessed your number as {ans}!")
    print(f"👾: It took me {attempts} attempts!")
    print("👾: Thank you for playing!")
    print("="*100)
elif celeb=="time":
    print("="*100)
    print("👾: Revealing my final guess in...")
    for i in range (5,0,-1):
        time.sleep(1)
        print(i)
    print(f"👾: I have successfully figured that your number was {ans}!")
    print(f"👾: I took {attempts} attempts!")
    print("👾: Thank you for playing!")
    print("="*100)