# A program that picks a random number between 1-20 and gived the user 7 chance to guess.
import random

def chances(left):
    z = 7 - left
    return z

print("Hello, what's your name?")
name = input()
answer = random.randint(1, 20)
print("Welcome, " + name + ". I'm thinking of a number between 1-20. You have 7 chances")

#Gives them 6 chances. Starts at 1 and goes up to but doesn't include 7
for guesses in range(1, 7):
    try:
        print("Take a gander.")
        guess = int(input())
        if guess > answer:
            print ("Try again. Your answer is too big")
        elif guess < answer:
            print ('Try again. Too small')
        else:
            break #if they guess correctly
    except ValueError: #runs when an error occurs in a try block
        print("That's not a valid number")

if guess == answer:
    print("Nicely Done, you may pass. You had " + str(chances(guesses)) " left.")
else:
    print('Too bad. The answer was ' + str(answer))
