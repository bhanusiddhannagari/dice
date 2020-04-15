import random

roll_again = "yes"

while roll_again == "yes" or roll_again == "y" or roll_again == "Y":

    print ("Rolling the dices...")
    print ("The values are....")
    a=random.choice([1,2,3,0])
    b=random.choice([1,2,3,0])
    print (a,b)
    
    if (a,b) == (0,1) or (a,b) == (1,0) or (a,b) == (0,0) :
        roll_again = "yes"
     
   
    else :
        roll_again = "."
        print("      these are your total dice values  ")

        print("------------------**********-----------------")