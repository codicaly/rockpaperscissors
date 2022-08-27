import random

#Global Variables
usr_score = 0
comp_score = 0
objects = ["rock","scissor","paper"]

def final_result():
    global usr_score,comp_score
    if (usr_score > comp_score):
        print("Congrats, you won by ",usr_score-comp_score," points.")
    elif (comp_score < usr_score):
        print("Sorry, you lost by ",comp_score-usr_score," points")
    else :
        print("It's a draw. You and Computer have scored same points")

def select_comp():
    return random.choice(objects)

def result(usr,comp):
    global usr_score, comp_score
    if usr == "s" :
        if comp == "paper" :
            usr_score += 1
            return "Congrats! you won!!!"
        elif comp == "rock":
            comp_score += 1
            return "Sorry! Computer won..."
        else :
            return "It's a draw!!!"
    
    elif usr == "r":
        if comp == "paper":
            comp_score += 1
            return "Sorry! Computer won..."
        elif comp == "scissor":
            usr_score += 1
            return "Congrats! you won!!!"
        else :
            return "It's a draw!!!"
    else : #user selected paper
        if comp == "scissor":
            comp_score += 1
            return "Sorry! computer won..."
        elif comp == "rock":
            usr_score += 1
            return "Congrats! you won!!!"

def main():
    print("Welcome y'all!!!")
    print("Enter r for rock, s for scissor and p for paper")
    print("Enter 0 to exit and see the final results")
    print("Game starts. Make selection\n")
    while True :
        usr = input("Enter : ")
        if usr in ["p","r","s","0"]:
            if usr == "0":
                print("\n\n")
                final_result()
                break
            elif usr == "p":
                print("User selected paper")
            elif usr == "r":
                print("User selected rock")
            else :
                print("User selected scissors")
        else :
            print("Invalid input")
            continue
        comp = select_comp()
        print("Computer selected ",comp)
        statement = result(usr,comp)
        print(statement)   
        print("User score :",usr_score," Computer score :",comp_score,"\n")     
main()

    
