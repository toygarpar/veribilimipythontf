import random

def number_guessing():

    secret_number = random.randint(1,100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the number guessing game!")
    print(f"I am thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it")


    while attempts < max_attempts:
        try:

            #get player's guess input
            guess = int(input("Enter your guess as an integer: "))
            attempts +=1


            #check if the guess is correct

            if guess == secret_number:
                print(f"Congratz! You have guessed the number in {attempts} attempts")
                return
            
            #Give hinst to the player

            elif guess < secret_number:
                print("Too Lo! Try Again with a higher number")
    
            else:
                print("Too Hi! Try with a lower number")


            #Tell player how many attempts are left
            print(f"You have {max_attempts - attempts} attempts left in the game")

        except Exception as err:
            print("Please enter a valid integer number", err)

        except ValueError as err:
            print("Please enter a valid integer number", err)



    #if player runs out of attempts
    print("Game Over! The number was {secret_number}")


#start the game
number_guessing()

