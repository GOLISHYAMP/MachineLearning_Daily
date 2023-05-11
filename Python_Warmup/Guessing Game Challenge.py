# guess from the 1 to 100
#if the guessed number is 10 less than number return warm
#if the guessed number is 10 more than number return cold
#if the guessed number is even closer the previous difference than return warmer
#if the guessed number is farthen from the previous then return Colder
#if the guessed number is equal to the number then return urehhh and return the number of tries before
# LETS DO IT

import random
import time

prev = 11
count = 0
def func(diff):
    global prev
    global count
    count += 1
    print(f"Difference is {abs(diff)}")
    if diff > -10 and diff < 0:
        if abs(diff) < prev:
            return "Warmer"
        else:
            prev = abs(diff)
            return "Warm"
    elif diff>0 and diff <11:
        if abs(diff) > prev:
            return "Cold"
        else:
            prev = abs(diff)
            return "Colder"
    elif diff == 0:
        print(f"Total turn took is {count}")
        return "HURRY! YOU GOT IT!"
    else:
        return "Keeps Trying"


if __name__ == "__main__":
    print("Welcome to the world of Guessing")
    print("Lets start!")
    print("When you want to quit press 'q' else Enter the number")
    guess = 's'
    print("Plese select the toughness level : \n1. EASY --- Guess between 1 to 10\n2. Medium --- Guess between 1 to 50\n3.Hard --- Guess between 1 to 100\n")
    level = int(input())
    dic = {1 : 10, 2 : 50, 3 : 100}
    while True:
        guess = input("Enter the guessing number : ")
        if guess == 'q':
            print("Exiting...")
            time.sleep(1)
            exit()
        
        number = random.randint(1,dic[level])
        print(f"Number is {number}")
        res = func(int(guess)-number)
        print(f"***{res}***")
