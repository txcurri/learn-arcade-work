MILES_TRAVELED=0
THIRST=0
CAMEL_TIREDNESS=0
DISTANCE_NATIVES_TRAVELED=-20
DRINKS_LEFT_IN_CANTEEN=3
NIGHTS_CAMPED=0
done = False
def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the")
    print("great Mobi desert.")
    print("The natives want their camel back and are chasing you")
    print("down! Survive your desert trek and out run the natives.")

main()
import random
def status():
    print(MILES_TRAVELED, "total miles traveled")
    print(DRINKS_LEFT_IN_CANTEEN, "Drinks Left")
    print(CAMEL_TIREDNESS, "Camel Tiredness")
    print(DISTANCE_NATIVES_TRAVELED,"Miles natives traveled")
    print(NIGHTS_CAMPED,"Nights Camped")
    print(THIRST, "thirst")

while not done:
    print(" A. Drink from your canteen.")
    print(" B. Ahead moderate speed.")
    print(" C. Ahead full speed.")
    print(" D. Stop for the night.")
    print(" E. Status check.")
    print(" Q. Quit.")
    user_choice: str = input("What is your choice? ")

    if random.randrange(20) == 0:

        DRINKS_LEFT_IN_CANTEEN = 3
        CAMEL_TIREDNESS = 0
        THIRST = 0
        print("YOU FOUND AN OASIS!!!")
    else:
        print("NO OASIS.")



    if user_choice.upper() == "Q":
        done = True
        print("You Just Quit")
        print("HIGH SCORE")
        status()

    elif user_choice.upper() == "A":
        print("You took a drink")
        DRINKS_LEFT_IN_CANTEEN -=1
        THIRST -= 4
        print(DRINKS_LEFT_IN_CANTEEN, "drinks left")

    elif user_choice.upper() == "B":
        MILES_TRAVELED =  random.randrange(5,13) + MILES_TRAVELED
        DISTANCE_NATIVES_TRAVELED = random.randrange(7,14) + DISTANCE_NATIVES_TRAVELED
        THIRST +=1
        CAMEL_TIREDNESS +=1
        print(MILES_TRAVELED, "total miles traveled")

    elif user_choice.upper() == "C":
        MILES_TRAVELED = random.randrange(10, 21) + MILES_TRAVELED
        DISTANCE_NATIVES_TRAVELED = random.randrange(7, 14) + DISTANCE_NATIVES_TRAVELED
        THIRST += 1
        CAMEL_TIREDNESS = random.randrange(1, 3) + CAMEL_TIREDNESS
        print(MILES_TRAVELED, "total miles traveled")
        print(MILES_TRAVELED, "total miles traveled")

    elif user_choice.upper() == "D":
        print("You camped for the night")
        NIGHTS_CAMPED +=1
        DISTANCE_NATIVES_TRAVELED += 0
        CAMEL_TIREDNESS = 0
        print("your camel is happy")
        THIRST = 0
        A=7
        B=14
        DISTANCE_NATIVES_TRAVELED  = random.randrange(7,14) + DISTANCE_NATIVES_TRAVELED
        print(NIGHTS_CAMPED, "total nights camped")

    elif user_choice.upper() == "E":
        print("You current status")
        status()

    if MILES_TRAVELED >= 200:
        done = True
        status()
        print("You have made it")

    if THIRST >= 4:
        print("You are thirsty!! Watch out")

    if THIRST >= 6:
        done = True
        print("you have died from thirst, try again")

    if CAMEL_TIREDNESS >= 5:
        print("Your camel is getting tiered, watch out!!")

    if CAMEL_TIREDNESS >=8:
        done = True
        print("your camel has died, try again")

    if DRINKS_LEFT_IN_CANTEEN <= -1:
        done = Truec

        print("No drinks left,try again")

    if DISTANCE_NATIVES_TRAVELED < 10 * MILES_TRAVELED and CAMEL_TIREDNESS >= 4:
        print("The natives are getting close!")

    elif DISTANCE_NATIVES_TRAVELED >= 15 * MILES_TRAVELED:
        print("you are ahead now!")

    elif MILES_TRAVELED >= 200:
            print("you made it")

    if DISTANCE_NATIVES_TRAVELED >= MILES_TRAVELED:
        done = True
        status()
        print("you have been caught!!")
print ("Thanks for playing")






