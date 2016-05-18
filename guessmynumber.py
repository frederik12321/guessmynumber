from random import randint

random_number = randint(1,10)

guess_number = int(input("Guess my random number from 1 to 10: "))

while guess_number != random_number:
    if guess_number == 0:
        print("Ok! Stop!")
        break
    elif guess_number > random_number:
        print("Too high")
    elif guess_number < random_number:
        print ("Too low")
    guess_number = int(input("Try again! (type 0 to stop): "))
else:
    print("Found it!!")


