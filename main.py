'''
1 for snake
-1 for water
0 for Gun
'''
import random 
computer = random.choice([-1,0,1])
youstr = input("Enter your choice from s/w/g :\n")
youdict = {"s":1, "w":-1, "g":0}

reversedict = {1:"Snake", -1:"Water", 0:"Gun"}

you = youdict[youstr]

print(f"you chose {reversedict[you]}\n Computer chose {reversedict[computer]}")

if (computer==you):
    print("Its a Draw!")

else:
    if(computer == -1 and you==1):
        print("You win!")
    elif(computer == -1 and you==0):
        print("You Lose!")
    elif(computer == 1 and you==-1):
        print("You Lose!")
    elif(computer == 1 and you==0):
        print("You Win!")
    elif(computer == 0 and you==-1):
        print("You Win!")
    elif(computer == 0 and you==1):
        print("You Lose!")
    
    else:
        Print("Something went wrong")


