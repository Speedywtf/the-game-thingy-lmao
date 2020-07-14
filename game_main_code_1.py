import time 
import os

player_input_value = open("Userinput.txt", "wt")


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

try:
    os.remove("Userinputs.txt")
except FileNotFoundError: 
    f = open("Userinputs.txt", "x") 

def family_name(player_gender):
    while loop_end == 3:          #WORKING
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
            print("That is not a valid input, input male for male or female for female")
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


while name_loop <= 6:  #DONE ERROR CHECKED 
    if player_gender == str("Male") or player_gender == str("male"):
        if player_name == wife_name or player_name == son_name or player_name == daughter_name or wife_name == son_name or wife_name== daughter_name or son_name == daughter_name: 
            time.sleep(1)
            print('')
            print("Two people cannot have the same name, please try again...") 
            family_name(player_gender) 
            if name_loop >= 6: 
                print('')
                time.sleep(1)
                print("Come on dude how hard is it to give people different names? im shutting off")
                exit()
            else: 
                pass 
            name_loop += 1
        else:
             pass 
    elif player_gender == str("Female") or player_gender == str("female"): 
        if player_name == husband_name or player_name == son_name or player_name == daughter_name or husband_name == son_name or husband_name== daughter_name or son_name == daughter_name: 
            time.sleep(1)
            print('')
            print("Two people cannot have the same name, please try again...")
            family_name(player_gender)   
        name_loop += 1 

        pass 
    

starting()     

optionone = 0    
optiontwo = 0

#Stay inside home first option

def sons_room():    #Check for errors pending, Finish print statements 
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
        print("Hello!")
        print('')
        time.sleep(1)
        print("I stopped you because I have a certain object I got given to deliver to you")
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
    def first_choice(optionone):        
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

