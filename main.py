'''
This is just a short mad-libs game i coded

'''
import random

def userinp():
    inpFromUser = input("Please type a noun, verb or something fun: ")

    return inpFromUser


def game():
    
    uinp_list = [

    ]

    while len(uinp_list) < 3:
        uinp = userinp()
        uinp_list.append(uinp)
    
        

    choice1 = random.choice(uinp_list).lower()
    choice2 = random.choice(uinp_list).lower()
    choice3 = random.choice(uinp_list).lower()
    
    print(f"""
           
            Roses are {choice1} 
            Voilets are {choice2}
            Honey is {choice3}
            And so are you!
            
            """)

game()