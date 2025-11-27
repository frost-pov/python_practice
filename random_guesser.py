import random
#to generate a random number we use random.randrange("the smallest number ","the largest number")
 #random.randrange(-1,11)
#now lets create a variable top_range to store user input
name= input("Enter your Name: ").lower()
print(f"hello "+str(name))
play=input("Do you wanna play the guessing game :) ...(yes/no) ").lower()
if play == "yes":
    top_range= input("type a number: ")
else:
    print("Okay, maybe next time")
    quit
#now to analyse and determine if user input is a digit we use .isdigit()
while True:
    if top_range.isdigit():
    #to convert our number int to an interger
        top_range=int(top_range)
    break
    #to determine our the input
    if top_range  <=  0:
        print("please enter a number larger than zero next time")
        quit()
        continue
else:
    print("Please enter a number")
    
random = random.randrange(0,top_range)

print(" You get five attempts")
attempts=1
while True:
    if attempts<=5:
        user_guess= input ("guess the number! ")
    else:
        print("Sorry, you run out of attempts")
        quit()
    if user_guess.isdigit():
        user_guess=int(user_guess)
        attempts= attempts+1
    else:
        print("Enter a number!")
        continue
   
    if user_guess ==random :
        print(f"You got it! "+str(attempts)+" Attempts")

        break 

    else:
        print("try again")
        continue
    

else: 
    quit()
