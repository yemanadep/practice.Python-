import random
randNumber = random.randint(1,100)
#print(randNumber)


#userGuess = int(input("Enter you Guess :"))
userGuess = None
guessNum = 0
while randNumber != userGuess:
    userGuess = int(input("Guess the number:"))
    guessNum +=1
    if userGuess>randNumber:
        print("Guessed number is big , Guess less :")
    else:
        print("Guesssed number is less, Guess big :")

    
print(f"You Guessed it right in {guessNum} guess")

