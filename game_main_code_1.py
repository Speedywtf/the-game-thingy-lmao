import time 

"""STARTING 
ISTABLISHING BASIC VARIABLES SUCH AS PLAYERS USERNAME"""

print('') 
print('Hey there!')
time.sleep(1)
print('')

game_name = "Not bothered to name this tbh"
player_name = str(input('What is your username? '))
time.sleep(1)
print('')


time.sleep(0.5)

game_information = "This game is based on you. All the choices you make, all the options you those affect the ending. Furthermore, There are many other factors that decide your ending, these will be revealed to you when the time is right "

print("Welcome, " + player_name + "!")
print('')

background_information = "You are a ordinary Joe going about living your life, getting by just fine with a decent house and a great family. This game is based on your everyday life, make the right decisions, good luck!"

#optiontwo prompt, do it if leave house


"""def option_two_choice():
     if option_two == str("1"): 
        time.sleep(1)
        print('')
        print("You carry the bird to the vet, and carry on your day...")
     elif option_two == str("2"): 
        time.sleep(1)
        print('')
        print("You leave the bird, and carry on with your day...")
     else: 
        print("Please chose a valid option, either 1 to help the bird or 2 to leave it")
        option_two_choice( )""" 

    


#STARTING MORNING 

def ready_Confirm():
    time.sleep(1)
    print('')
    print("DAY ONE, Good Luck " + player_name)
    time.sleep(2)
    print("-----------------------------------------")
    print("GOOD MORNING! Today is your first day! what would you like to do?")
    print('')
    
   
        
#ARE YOU READY PROMPT

def ready(): 
    time.sleep(1)
    player_ready = str(input("When you are ready, please press R: "))
    if player_ready == "r" or player_ready == "R": 
        ready_Confirm()
    else: 
        time.sleep(1)
        print('')
        print("please select a valid input")
        ready()
    
#GAME INFORMATION

a = 0 
def starting(): 
    print("-----------------------------------------")
    print("Welcome to " + game_name)
    time.sleep(1)
    print("-----------------------------------------")
    print(game_information)
    print("-----------------------------------------")
    time.sleep(1)
    print("-----------------------------------------")
    print(background_information) 
    print("-----------------------------------------")
    time.sleep(1)
    print("-----------------------------------------")
    time.sleep(2)
    print('')
    ready() 


loop_end = 3


player_gender = str(input("Are you male or female? "))

def family_name(player_gender):
    while loop_end == 3:          #ELSE STATEMENT DOES NOT WORK 
        if player_gender == str("Male") or player_gender == str("male"): 
            print('')
            global wife_name
            wife_name = str(input("What is your wifes name? "))
            print('')
            global son_name
            son_name = str(input("Whats your sons name? "))
            print('')
            global daughter_name
            daughter_name = str(input("Whats your daughters name? "))
            break
        elif player_gender == str("Female") or player_gender == str("female"): 
            print('')
            global husband_name 
            husband_name = str(input("What is your husbands name? "))
            print('')
            son_name = str(input("Whats your sons name? "))
            print('')
            daughter_name = str(input("Whats your daughters name? "))
            break
        else: 
            print('')
            print("That is not a valid input, input male for male or female or female")
            print('')
            player_gender = str(input("Are you male or female? "))
            continue
    
family_name(player_gender)

name_loop = 3 


while name_loop ==3: 
    if player_gender == str("Male") or player_gender == str("male"):
        if player_name == wife_name or player_name == son_name or player_name == daughter_name or wife_name == son_name or wife_name== daughter_name or son_name == daughter_name: 
            time.sleep(1)
            print('')
            print("Two people cannot have the same name, please try again...") 
            family_name
        else:
             pass 
    elif player_gender == str("Female") or player_gender == str("female"): 
        if player_name == husband_name or player_name == son_name or player_name == daughter_name or husband_name == son_name or husband_name== daughter_name or son_name == daughter_name: 
            time.sleep(1)
            print('')
            print("Two people cannot have the same name, please try again...")
            family_name(player_gender)   #Not running???? wtf xD

    name_loop += 1

    if name_loop >= 6:
        time.sleep(1)
        print('') 
        print("Too many invalid inputs, game shutting down")
        time.sleep(0.3)
        print(".")
        time.sleep(0.3)
        print("..")
        time.sleep(0.3)
        print("...")
        exit()
    else: 
        continue

   


starting()       #ALL WORKING UNTILL HERE

optionone = 0    #DEFINING BOTH VARIABLES 
optiontwo = 0

#Stay inside home first option

def sons_room(): 
    print('')
    sons_room_optiontwo = str(input("Do you (1) Wake him up or (2) Leave the room "))


#STARTING GAME FIRST OPTION

try:
    def first_choice(optionone):        #NOT WORKING DOING ELSE COMMAND FOR 1 INPUT
         if optionone == 1: 
            time.sleep(1)
            print('')
            print("You have chosen to get out of the house for once")  #optiontwo still finish 
         elif optionone == 2: 
            time.sleep(1)
            print('')
            print("You go to " + son_name + "'s room to find him sleeping peacefully")   
            sons_room() 
         else: 
            time.sleep(1)
            print('')
            print("please choose a valid option") 
except ValueError: 
    print("Please chose a valid input, 1 for Leaving The House and 2 for Staying inside")
    first_choice(int(input("It is now morning, would you like to (1) Leave your house or (2) Do some chores? ")))


first_choice(int(input("It is now morning, would you like to (1) Leave your house or (2) Do some chores? ")))  #CALLING FUNCTION WITH A PROMPT 

