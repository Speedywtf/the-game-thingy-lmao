import time 

player_input_value = open("Userinput.txt", "wt")
player_input_value.write("Here are all the palyer input values")

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

def save_user_input(player_gender):
    if player_gender == str("Male") or player_gender == str("male"):
        player_input_value.write("Here are all the palyer input values")
        player_input_value.write("Player Username: " + player_name)
        player_input_value.write("Player Gender: " + player_gender)
        player_input_value.write("Player Wife Name: " + wife_name)
        player_input_value.write("Player Son Name: " + son_name)
        player_input_value.write("Player Daughter Name: " + daughter_name)
    elif player_gender == str("female") or player_gender == str("Female"): 
        player_input_value.write("Here are all the palyer input values")
        player_input_value.write("Player Username: " + player_name)
        player_input_value.write("Player Gender: " + player_gender)
        player_input_value.write("Player Husband Name: " + husband_name)
        player_input_value.write("Player Son Name: " + son_name)
        player_input_value.write("Player Daughter Name: " + daughter_name)
    else: 
        pass 

    save_user_input(player_gender)

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

family_info = []

def List_Add(wife_name, husband_name, son_name, daughter_name):
    if player_gender == str("male") or player_gender == str("Male"):  #Not tested 
        family_info.append(wife_name)
        family_info.append(son_name) 
        family_info.appent(daughter_name)
        print(family_info)
    elif player_gender == str("female") or player_gender == str("Female"):  #fuck u
        family_info.append(husband_name)
        family_info.append(son_name)
        family_info.appent(daughter_name)
        print(family_info)
    else: 
        pass 


 
    
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
    else: 
        pass 

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

def sons_room():    #Check for errors pending, Finish 
    print('')
    time.sleep(1)
    sons_room_optiontwo = str(input("Do you (1) Wake him up or (2) Leave the room "))
    if sons_room_optiontwo == str("1"): 
        print('')
        time.sleep(1)
        print("You woke " + son_name + " up, he gets very angry and tries to...") #FInish later 
    elif sons_room_optiontwo == str("2"):
        print("You leave " + son_name + " in peace, and decide to leave his name.") 
    else: 
        print("Invalid input, 1 to wake him up or 2 to leave room") 
        sons_room_optiontwo()


def gender_call(): 
    if player_gender == str("male") or player_gender == str("Male"): 
        return("Sir")
    elif player_gender == str("female") or player_gender == str("Female"): 
        return("Ma'am")
    else: 
        pass

#Deciding to go out the house first option 
   
def out_of_house(): 
    time.sleep(1)
    print('')
    global outside_one_prompt
    outside_one_prompt = str(input("You go out and spot an injured bird on the pavement, do you (1) Leave it there or (2) Take it to the vet? "))
    if outside_one_prompt == str("1"): 
        time.sleep(1)
        print('')
        print("You have decided to leave the poor old bird on the pavement. You walk towards your workplace as you get stopped by a stranger")
        print('')
        time.sleep(1)
        print(".....Hello, " + gender_call() + "!") 
        print('')
        time.sleep(0.5)
        print("\033[1;31;40m Hello! \n")
        print("\033[1;32;40m I stopped you because I have a certain object I got given to deliver to you  \n")
    elif outside_one_prompt == str("2"): 
        time.sleep(1)
        print('')
        print("You have decided to take it to the vet...")
    else: 
        time.sleep(1)
        print('')
        print("Invalid input, 1 for Ignoring the bird and 2 for Taking it the the vet... Please try again")

#STARTING GAME FIRST OPTION

try:
    def first_choice(optionone):        #NOT WORKING DOING ELSE COMMAND FOR 1 INPUT
         if optionone == 1: 
            time.sleep(1)
            print('')
            print("You have chosen to get out of the house for once")  #optiontwo still finish 
            out_of_house()
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

