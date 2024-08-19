import random
'''
1 for snake
-1 for water
0 for gun

'''
computer = random.choice([-1,0,1])
youstr= input("enter your choice: ")
youdict={"s":1,"w":-1,"g":0}
reversedict = {1:"snake",-1:"water",0:"gun"}

you = youdict[youstr]
print(f"You chose {reversedict[you]}\n Computer chose {reversedict[computer]}")

if(computer==you):
    print("It's a tie")
    
else:
    if(computer==-1 and you==1):
        print("You win")
        
    elif(computer==-1 and you==0):
        print("Computer wins")
        
    elif(computer==1 and you==-1):
        print("Computer wins")
        
    elif(computer== 1 and you==0):
        print("You win")
        
    elif(computer== 0 and you==-1):
        print("You win")
    
    elif(computer==0 and you==1):
        print("Computer wins")
    else:
        print("sometging wrong, Please Try  again")
    
    # You win on (1 and -2)
    # Computer  wins on (-1 and 2)
    # by using martix of (a(-)b)