import random
number=random.randint(1,9)
chances=0
while chances < 5 :
    un=int(input("Enter the number : "))
    if(number==un):
        print("Congratulation You WON")
        break
    elif(un<number):
        print("your guess is too low: guess a number higher than ",un)
    else:
        print("your guess is too high: guess a number lower than ",un)
    chances+=1
if(chances>= 5):
    print("YOU LOSE !!! The Number is ",number)
