
import random

# error_number = 3
term = 3
your_score = 0
computer_score = 0

x = int(input("Before we start the game mention the range for the number: "))
print("")
print("_____Let's start the Game______")







def guess(x):

    

    error_number = 3
    global your_score
    random_number = random.randint(1,x)
    guess = 0
    
    while True:
            guess = int(input(f"Enter your number : "))

            if error_number == 1:
                
                print(f"You have lost the number was: {random_number}")
                print("*******************************************")
                print("")
                print("")
                break
            
            if guess == random_number:
                print("")
                print(f" *****  Yay you got the number : {random_number}  *****")
                print("")
                your_score +=1
                break  
            elif guess > random_number:
                print("try agian number too high")
                error_number -= 1
                print(f"Tries remaning : {error_number}")
                print("")
            elif guess < random_number:
                print("try again number too low")
                error_number -= 1
                print(f"Tries remaning : {error_number}")
                print("")
            
        
    
    

def computer_guess(x):

    print("Now it's Computer's turn")

    error_number = 3
    global computer_score
    feedback = 0
    low = 0
    high = x
    
    
    while True:
            if low != high:
                guess = random.randint(low,high)
            else:
                guess = low
            
            feedback = input(f"Is the {guess} too high: 'h', too low: 'l', correct: 'c' ")
            print("")
            if error_number == 1:
                print("Computer has lost")
                print("******************************************************")
                print("")
                
                print("")
                
                break
            if feedback == 'c':
                print("")
                print(f"*****  Yay computer guessed correctly the number: {guess}  *****")
                print("")
                
                computer_score +=1
                break
            
            if feedback == 'h':
                high = guess -1
                error_number -=1
                
            elif feedback == 'l':
                low = guess + 1
                error_number -=1
            # elif error_number <= 1:
            #     print("Computer lost")
            #     computer_score -=1
            #     print("")
                
            #     break
    
    
    



while term != 0:
    print("Your turn to guess the number")
    print("")
    guess(x)
    computer_guess(x)
    term -=1

print("")
print("")
print(f"Your score = {your_score}  & Computer score = {computer_score}")


