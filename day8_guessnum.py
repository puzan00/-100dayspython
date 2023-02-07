#guess the number python
import random
def guess(num):
    random_number=random.randint(1,num) # for creating random numbers
    guess=0
    while guess!=random_number:
        guess=int(input(f"can you guess the number from 1 to {num}:")) #take user input 
        if guess<random_number:
            print("Your guess is too low")
        elif guess>random_number:
            print("Your guess is too high")
    print(f"you have guessed the correct number!{random_number} ") #display if the guess is correct
guess(10)
