a = '''
/===============================================================================\\
|   _____    ______   ______   ______   __    __       ______  ______  ______   |
|  /\  __ \./\  == \ /\  ___\ /\  __ \ /\ "-./  \     /\  == \/\  ___\/\__  _\  |
|  \ \ \/\ \\ \  __< \ \  __\ \ \  __ \\ \ \-./\ \    \ \  _-/\ \  __\\/_/\ \/  |
|   \ \____ /\ \_\ \_\\ \_____\\ \_\ \_\\ \_\ \ \_\    \ \_\   \ \_____\ \ \_\  |
|    \/____/  \/_/ /_/ \/_____/ \/_/\/_/ \/_/  \/_/     \/_/    \/_____/  \/_/  |
\===============================================================================/
'''
print(a) 
b = '''
==================================GAME SETUP====================================
'''
print(b)
#initialising variables
#code for 1 pet
player_name = input("Welcome to Dream Pet. May I grab your name please. ")
print("Nice to see you " + player_name + ". I hope you enjoy our short interaction.")
print()
pet_count = int(input("Now, tell me " + player_name + ", would you like one or two pets? (1/2) "))
if pet_count > 2 or pet_count < 1:
    print("Please choose a number between 1 and 2")
    exit()
if pet_count == 1:
    pet_type = input("What type of animal is your pet? (Cat/Dog)? ")
    if pet_type.lower() == "cat" or pet_type.lower() == "dog":
        pet_name = input("What is this " + pet_type + " called? ")
        if type(pet_name) == str:
            pet_location = input("Where is " + pet_name + " right now? (Living Room/Kitchen/Garden) ")
            if pet_location.lower() == "living room" or pet_location.lower() == "kitchen" or pet_location.lower() == "garden":
                pet_hunger = int(input("What is " + pet_name + "'s hunger value? "))
                if pet_hunger > 0 and pet_hunger < 101:
                    pet_happiness = int(input("What is " + pet_name + "'s happiness value? "))
                    if pet_happiness > 0 and pet_happiness < 101:
                        pet_type = pet_type
                        pet_name = pet_name
                        pet_location = pet_location
                        pet_hunger = pet_hunger
                        pet_happiness = pet_happiness
                    else:
                        print("Invalid output: Provide a number between 0 and 100")
                        exit()
                else:
                        print("Invalid output: Provide a number between 0 and 100")
                        exit()
            else:
                        print("Invalid output: Provide a location between options provided")
                        exit()
        else:
                        print("Invalid output")
                        exit()
    else:
                        print("Invalid output: State dog or cat")
                        exit()
else:
    pet1_type = input("What type of animal is your first pet? (Cat/Dog)? ")
    if pet1_type.lower() == "cat" or pet1_type.lower() == "dog":
        pet1_name = input("What is this " + pet1_type + " called? ")
        if type(pet1_name) == str:
            pet1_location = input("Where is " + pet1_name + " right now? (Living Room/Kitchen/Garden) ")
            if pet1_location.lower() == "living room" or pet1_location.lower() == "kitchen" or pet1_location.lower() == "garden":
                pet1_hunger = int(input("What is " + pet1_name + "'s hunger value? "))
                if pet1_hunger > 0 and pet1_hunger < 101:
                    pet1_happiness = int(input("What is " + pet1_name + "'s Happiness value? "))
                    if pet1_happiness > 0 and pet1_happiness < 101:
                        pet2_type = input("What type of animal is your second pet? (Cat/Dog)? ")
                        if pet2_type.lower() == "cat" or pet2_type.lower() == "dog":
                            pet2_name = input("What is this " + pet2_type + " called? ")
                            if type(pet2_name) == str:
                                pet2_location = input("Where is " + pet2_name + " right now? (Living Room/Kitchen/Garden) ")
                                if pet2_location.lower() == "living room" or pet2_location.lower() == "kitchen" or pet2_location.lower() == "garden":
                                    pet2_hunger = int(input("What is " + pet2_name + "'s hunger value? "))
                                    if pet2_hunger > 0 and pet2_hunger < 101:
                                        pet2_happiness = int(input("What is " + pet2_name + "'s Happiness value? "))
                                        if pet2_happiness > 0 and pet2_happiness < 101:
                                            pet1_type = pet1_type
                                            pet1_name = pet1_name
                                            pet1_location = pet1_location
                                            pet1_hunger = pet1_hunger
                                            pet1_happiness = pet1_happiness
                                            pet2_type = pet2_type
                                            pet2_name = pet2_name
                                            pet2_location = pet2_location
                                            pet2_hunger = pet2_hunger
                                            pet2_happiness = pet2_happiness
                                        else:
                                            print("Invalid output: Provide a number between 0 and 100")
                                            exit()
                                    else:
                                            print("Invalid output: Provide a number between 0 and 100")
                                            exit()
                                else:
                                            print("Invalid output: Provide a location between options provided")
                                            exit()
                            else:
                                            print("Invalid output")
                                            exit()
                        else:
                                            print("Invalid output: State dog or cat")
                                            exit()
                    else:
                                            print("Invalid output: Provide a number between 0 and 100")
                                            exit()
                else:
                                            print("Invalid output: Provide a number between 0 and 100")
                                            exit()
            else:
                                            print("Invalid output: Provide a location between options provided")
                                            exit()
        else:
                                            print("Invalid output")
                                            exit()
    else:
                                            print("Invalid output: State dog or cat")
                                            exit()                  
# initialize all main requirements here 
happy_sounds_dog = "Woof"
happy_sounds_cat = "Meow"
Angry_sounds_dog = "Grrrrrr"
Angry_sounds_cat = "Hisssss"
player_position = "living room"
#split for code starts from here
#one pet
if pet_count == 1:
    #hunger condition
    if pet_hunger >= 90:
        pet_location = "kitchen"
    
    #start status here
    print()
    c = '''
=====================================STATUS======================================
'''
    print(c)
    print(player_name + ", here is a summary of the current status of your pets:")
    print("Your little " + pet_type + ", " + pet_name + ", is in the " + pet_location + " and is {:.2f}% happy and {:.2f}% hungry.".format(pet_happiness, pet_hunger))
    print("\n===================================GAME START====================================")
    print()
    d = """
               _     _       _              ______                      
              | |   (_)     (_)             | ___ \                     
              | |    ___   ___ _ __   __ _  | |_/ /___   ___  _ __ ___  
              | |   | \ \ / / | '_ \ / _` | |    // _ \ / _ \| '_ ` _ \ 
              | |___| |\ V /| | | | | (_| | | |\ \ (_) | (_) | | | | | |
              \_____/_| \_/ |_|_| |_|\__, | \_| \_\___/ \___/|_| |_| |_|
                                      __/ |                             
                                     |___/ 
"""
    print(d)
    print()
    livingroom_action = input("We are in the living room, which of the following actions would you like to perform? (Interact/Find/Leave) ")
    if livingroom_action.lower() == "interact" or livingroom_action.lower() == "find" or livingroom_action.lower() == "leave":
        #interact 
        if livingroom_action.lower() == "interact":
            #if pet is in kitchen
            if pet_location.lower() == "kitchen":
                Livingroom_pet_or_play = input(player_name + ", do you want to pet or play with " + pet_name + "? (Pet/Play) ")
                if Livingroom_pet_or_play.lower() == "pet" or Livingroom_pet_or_play.lower() == "play":
                    if Livingroom_pet_or_play.lower() == "pet":
                        if pet_type.lower() == "dog":
                            print(happy_sounds_dog + ", " + pet_name + "is really enjoying that rub in the tummy!!")
                            pet_happiness = pet_happiness + 9.6
                        else:
                            print(happy_sounds_cat + ", " + pet_name + "is really enjoying that rub in the tummy!!")
                            pet_happiness = pet_happiness + 9.6
                    else:
                        if pet_type.lower() == "dog":
                            print(happy_sounds_dog + ", " + pet_name + " is chasing after that ball! It's so excited it almost knocked over the table!!")
                            pet_happiness = pet_happiness + 13.21
                            pet_hunger = pet_hunger + 10.90
                        else:
                            print(happy_sounds_cat + ", " + pet_name + " loves pouncing at that cat wand! Such a predator!")
                            pet_happiness = pet_happiness + 13.21
                            pet_hunger = pet_hunger + 10.90
                else:
                    print("Invalid action: please select (pet or play)")
            #location not kitchen                    
            else:
                Living_room_call = input(pet_name + " is not in the living room, do you want to call it? (Yes/No) ")
                if Living_room_call.lower() == "yes" or Living_room_call.lower() == "no":
                    if Living_room_call.lower() == "yes":
                        if pet_happiness >= 20 and pet_hunger < 90:
                            pet_location = "kitchen"
                            #repeat code for pet location == kitchen
                            if pet_location.lower() == "kitchen":
                                Livingroom_pet_or_play = input(player_name + ", do you want to pet or play with " + pet_name + "? (Pet/Play) ")
                                if Livingroom_pet_or_play.lower() == "pet" or Livingroom_pet_or_play.lower() == "play":
                                    if Livingroom_pet_or_play.lower() == "pet":
                                        if pet_type.lower() == "dog":
                                            print(happy_sounds_dog + ", " + pet_name + "is really enjoying that rub in the tummy!!")
                                            pet_happiness = pet_happiness + 9.6
                                        else:
                                            print(happy_sounds_cat + ", " + pet_name + "is really enjoying that rub in the tummy!!")
                                            pet_happiness = pet_happiness + 9.6
                                    else:
                                        if pet_type.lower() == "dog":
                                            print(happy_sounds_dog + ", " + pet_name + " is chasing after that ball! It's so excited it almost knocked over the table!!")
                                            pet_happiness = pet_happiness + 13.21
                                            pet_hunger = pet_hunger + 10.90
                                        else:
                                            print(happy_sounds_cat + ", " + pet_name + " loves pouncing at that cat wand! Such a predator!")
                                            pet_happiness = pet_happiness + 13.21
                                            pet_hunger = pet_hunger + 10.90
                        else:
                            if pet_type.lower() == "dog":
                                print(Angry_sounds_dog + "! Oh no, " + pet_name + " is a bit angry, it doesn't want to come!")
                                Livingroom_failed_call = input(player_name + "which one of the following actions would you like to perform next? (Find/Leave) ")
                                #find or leave again
                                if Livingroom_failed_call.lower() == "find" or Livingroom_failed_call.lower() == "leave":
                                    if Livingroom_failed_call.lower() == "find":
                                        livingroom_find_food = input("Which type of pet food do you want to look for? (Simple/Lavish) ")
                                        if livingroom_find_food.lower() == "simple" or livingroom_find_food.lower() == "lavish":
                                            if livingroom_find_food.lower() == "simple":
                                                print("Looking around the room, you found the simple pet food stored in the corner of the overhead cupboard.")
                                                print("Great, now we have some pet food, lets go to the kitchen!")
                                                player_position = "kitchen"
                                            else:
                                                print("You remembered that the lavish pet food was delivered yesterday, and you grabbed it out of the box.")
                                                print("Great, now we have some pet food, lets go to the kitchen!")
                                                player_position = "kitchen"
                                        else:
                                            print("Invalid action: please select (Simple/Lavish)")
                                            exit()
                                    else:
                                        print("Alright, lets move on to the kitchen immediately!")
                                        player_position = "kitchen"   
                                else:
                                    print("Invalid action: please select (Find/Leave)")
                                    exit()
                                    
                            else:
                                print(Angry_sounds_cat + "! Oh no, " + pet_name + " is a bit angry, it doesn't want to come!")
                                Livingroom_failed_call = input(player_name + "which one of the following actions would you like to perform next? (Find/Leave) ")
                                #find or leave again
                                if Livingroom_failed_call.lower() == "find" or Livingroom_failed_call.lower() == "leave":
                                    if Livingroom_failed_call.lower() == "find":
                                        livingroom_find_food = input("Which type of pet food do you want to look for? (Simple/Lavish) ")
                                        if livingroom_find_food.lower() == "simple" or livingroom_find_food.lower() == "lavish":
                                            if livingroom_find_food.lower() == "simple":
                                                print("Looking around the room, you found the simple pet food stored in the corner of the overhead cupboard.")
                                                print("Great, now we have some pet food, lets go to the kitchen!")
                                                player_position = "kitchen"
                                            else:
                                                print("You remembered that the lavish pet food was delivered yesterday, and you grabbed it out of the box.")
                                                print("Great, now we have some pet food, lets go to the kitchen!")
                                                player_position = "kitchen"
                                        else:
                                            print("Invalid action: please select (Simple/Lavish)")
                                            exit()
                                    else:
                                        print("Alright, lets move on to the kitchen immediately!")
                                        player_position = "kitchen"   
                                else:
                                    print("Invalid action: please select (Find/Leave)")
                                    exit()
                    else:
                        Livingroom_No_call = input(player_name + "which one of the following actions would you like to perform next? (Find/Leave) ")
                        if Livingroom_No_call.lower == "find" or Livingroom_No_call.lower == "leave":
                            if Livingroom_No_call.lower == "find":
                                livingroom_find_food = input("Which type of pet food do you want to look for? (Simple/Lavish) ")
                                if livingroom_find_food.lower() == "simple" or livingroom_find_food.lower() == "lavish":
                                    if livingroom_find_food.lower() == "simple":
                                        print("Looking around the room, you found the simple pet food stored in the corner of the overhead cupboard.")
                                        print("Great, now we have some pet food, lets go to the kitchen!")
                                        player_position = "kitchen"
                                    else:
                                        print("You remembered that the lavish pet food was delivered yesterday, and you grabbed it out of the box.")
                                        print("Great, now we have some pet food, lets go to the kitchen!")
                                        player_position = "kitchen"
                                else:
                                    print("Invalid action: please select (Simple/Lavish)")
                                    exit()
                            else:
                                print("Alright, lets move on to the kitchen immediately!")
                                player_position = "kitchen"
                                         
                        else:
                            print("Invalid action: please select (Find/Leave)")
                            exit()
   
                else:
                    print("Invalid action: please select (Yes/No)")
                    exit()
                    

        if livingroom_action.lower() == "find":
            livingroom_find_food = input("Which type of pet food do you want to look for? (Simple/Lavish) ")
            if livingroom_find_food.lower() == "simple" or livingroom_find_food.lower() == "lavish":
                if livingroom_find_food.lower() == "simple":
                    print("Looking around the room, you found the simple pet food stored in the corner of the overhead cupboard.")
                    print("Great, now we have some pet food, lets go to the kitchen!")
                    player_position = "kitchen"
                else:
                    print("You remembered that the lavish pet food was delivered yesterday, and you grabbed it out of the box.")
                    print("Great, now we have some pet food, lets go to the kitchen!")
                    player_position = "kitchen"
            else:
                print("Invalid action: please select (Simple/Lavish)")
                exit()

        if livingroom_action.lower() == "leave":
            print("Alright, lets move on to the kitchen immediately!")
            player_position = "kitchen"
    else:
        print("Invalid action: please select (Interact/Find/Leave)")
        exit()

    print(c)
    print(player_name + ", here is a summary of the current status of your pets:")
    print("Your little " + pet_type + ", " + pet_name + ", is in the " + pet_location + " and is {:.2f}% happy and {:.2f}% hungry.".format(pet_happiness, pet_hunger))

    e = """
                     _   __ _  _          _
                    | | / /(_)| |        | |
                    | |/ /  _ | |_   ___ | |__    ___  _ __
                    |    \ | || __| / __|| '_ \  / _ \| '_ \
                    | |\  \| || |_ | (__ | | | ||  __/| | | |
                    \_| \_/|_| \__| \___||_| |_| \___||_| |_|
            
"""
    print(e)
    player_position = "kitchen"
    pet_location = "kitchen"
    print()
    print("Your pet heard that you're making food and decided to join you!")

    # prepare food methodical // chaotic 

    kitchen_prompt = input(player_name + ", do you want to make food methodically or chaotically, type M for methodically, C for chaotic ")
    if kitchen_prompt.lower() == "m" or kitchen_prompt.lower() == "c":
        if kitchen_prompt.lower() == "m":
            print("Answer the following question properly and we should be good!!")
            print()
            kitchen_methodquiz = input("Can" + pet_name + " eat chocolate??: (type Y for yes, N for no) ")
            if kitchen_methodquiz.lower() == "y" or kitchen_methodquiz.lower() == "n":
                if kitchen_methodquiz.lower() == "y":
                    print("HOORAY!!")
                    pet_happiness = pet_happiness + 10
                    pet_hunger = pet_hunger - 50
                    if pet_type.lower() == "dog":
                        print(happy_sounds_dog)
                    else:
                        print(happy_sounds_cat)
                else:
                    print("WRONG ANSWER!!")
                    if pet_type.lower() == "dog":
                        print(Angry_sounds_dog)
                    else:
                        print(Angry_sounds_cat)
                    exit()
            else:
                print("Invalid input: please type Y or N")
                exit()
        else:
            if kitchen_prompt.lower() == "c":
                chaotic_decision = input("Are you sure you want to continue? (Y/N): ")
                if chaotic_decision.lower() == "y" or chaotic_decision.lower() == "n":
                    if chaotic_decision.lower() == "y":
                        print("Alright sure but this will make your pet a bit mad")
                        pet_happiness = pet_happiness - 20
                        pet_hunger = pet_hunger - 25
                        if pet_type.lower() == "dog":
                            print(Angry_sounds_dog)
                        else:
                            print(Angry_sounds_cat)
                else:
                    print("Invalid input: please type Y or N")
                    exit()         
    else:
        print("Invalid input: please type M or C")
        exit()
    # play
    print("Now that we have fed our pet!!")
    kitchen_pet_or_play = input(player_name + ", do you want to pet or play with " + pet_name + "? (Pet/Play) ")
    if kitchen_pet_or_play.lower() == "pet" or kitchen_pet_or_play.lower() == "play":
        if kitchen_pet_or_play.lower() == "pet":
            if pet_type.lower() == "dog":
                print(happy_sounds_dog + ", " + pet_name + "is really enjoying that rub in the tummy!!")
                pet_happiness = pet_happiness + 9.6
            else:
                print(happy_sounds_cat + ", " + pet_name + "is really enjoying that rub in the tummy!!")
                pet_happiness = pet_happiness + 9.6
        else:
            if pet_type.lower() == "dog":
                print(happy_sounds_dog + ", " + pet_name + " is chasing after that ball! It's so excited it almost knocked over the table!!")
                pet_happiness = pet_happiness + 13.21
                pet_hunger = pet_hunger + 10.90
            else:
                print(happy_sounds_cat + ", " + pet_name + " loves pouncing at that cat wand! Such a predator!")
                pet_happiness = pet_happiness + 13.21
                pet_hunger = pet_hunger + 10.90
    else:
        print("Invalid action: please select (pet or play)")

    # leave to kitchen 

    print("Alright!! now that we have had our fun in the kitchen!! lets end with a beautiful view by the garden")
    view_prompt = input("Are you ready to go off into the kitchen: (Y/N): ")
    if view_prompt.lower == "n":
        exit()
    else: 
        print("Well done!")

    f = """
                    _____                   _              
                    |  __ \                 | |             
                    | |  \/  __ _  _ __   __| |  ___  _ __  
                    | | __  / _` || '__| / _` | / _ \| '_ \ 
                    | |_\ \| (_| || |   | (_| ||  __/| | | |
                     \____/ \__,_||_|    \__,_| \___||_| |_|        

"""
    print(f)

    print(player_name + ", Well done on going so far, lets see if you passed or failed")
    print("Bare in mind that to pass, your pets happiness level must be over 50 and your pets hunger must be below 50")

    if pet_happiness > 100:
        pet_happiness = 100 
    if pet_hunger > 100:
        pet_hunger = 100

    if pet_happiness > 50 and pet_hunger < 50:
        print("WOOHOOO YOU PASSED!!!!")
        if pet_type.lower() == "dog":
            print(happy_sounds_dog)
        else:
            print(happy_sounds_cat)
    else:
        print("Unfortunately you didnt pass :( feel free to try again)")
        exit()
    g = """
====================================GAME END=====================================
"""
    print(g)

#second pet
if pet_count == 2:  
    #initialise hunger conditio  
    if pet1_hunger >= 90:
        pet1_location = "kitchen"
    if pet2_hunger >= 90:
        pet2_location = "kitchen"
    print()
    c = '''
=====================================STATUS======================================
'''
    print(c)
    print(player_name + ", here is a summary of the current status of your pets:")
    print("Your little " + pet1_type + ", " + pet1_name + ", is in the " + pet1_location + " and is {:.2f}% happy and {:.2f}% hungry.".format(pet1_happiness, pet1_hunger))
    print("Your little " + pet2_type + ", " + pet2_name + ", is in the " + pet2_location + " and is {:.2f}% happy and {:.2f}% hungry.".format(pet2_happiness, pet2_hunger))
    print("\n===================================GAME START====================================")
 

    d = """
               _     _       _              ______                      
              | |   (_)     (_)             | ___ \                     
              | |    ___   ___ _ __   __ _  | |_/ /___   ___  _ __ ___  
              | |   | \ \ / / | '_ \ / _` | |    // _ \ / _ \| '_ ` _ \ 
              | |___| |\ V /| | | | | (_| | | |\ \ (_) | (_) | | | | | |
              \_____/_| \_/ |_|_| |_|\__, | \_| \_\___/ \___/|_| |_| |_|
                                      __/ |                             
                                     |___/ 
"""
    print(d)
    print()
    livingroom_action = input("We are in the living room, which of the following actions would you like to perform? (Interact/Find/Leave) ")
    if livingroom_action.lower() == "interact" or livingroom_action.lower() == "find" or livingroom_action.lower() == "leave":
        #interact 
        if livingroom_action.lower() == "interact":
            #if pet is in kitchen
            which_pet = int(input("which pet do you want to interact with (1/2) "))
            if which_pet == 1 or which_pet == 2:
                if which_pet == 1:
                    if pet1_location.lower() == "kitchen":
                        Livingroom_pet_or_play = input(player_name + ", do you want to pet or play with " + pet1_name + "? (Pet/Play) ")
                        if Livingroom_pet_or_play.lower() == "pet" or Livingroom_pet_or_play.lower() == "play":
                            if Livingroom_pet_or_play.lower() == "pet":
                                if pet1_type.lower() == "dog":
                                    print(happy_sounds_dog + ", " + pet1_name + "is really enjoying that rub in the tummy!!")
                                    pet1_happiness = pet1_happiness + 9.6
                                else:
                                    print(happy_sounds_cat + ", " + pet1_name + "is really enjoying that rub in the tummy!!")
                                    pet1_happiness = pet1_happiness + 9.6
                            else:
                                if pet1_type.lower() == "dog":
                                    print(happy_sounds_dog + ", " + pet1_name + " is chasing after that ball! It's so excited it almost knocked over the table!!")
                                    pet1_happiness = pet1_happiness + 13.21
                                    pet1_hunger = pet1_hunger + 10.90
                                else:
                                    print(happy_sounds_cat + ", " + pet1_name + " loves pouncing at that cat wand! Such a predator!")
                                    pet1_happiness = pet1_happiness + 13.21
                                    pet1_hunger = pet1_hunger + 10.90
                        else:
                            print("Invalid action: please select (pet or play)")
                    #location not kitchen                    
                    else:
                        Living_room_call = input(pet1_name + " is not in the living room, do you want to call it? (Yes/No) ")
                        if Living_room_call.lower() == "yes" or Living_room_call.lower() == "no":
                            if Living_room_call.lower() == "yes":
                                if pet1_happiness >= 20 and pet1_hunger < 90:
                                    pet1_location = "kitchen"
                                    #repeat code for pet location == kitchen
                                    if pet1_location.lower() == "kitchen":
                                        Livingroom_pet_or_play = input(player_name + ", do you want to pet or play with " + pet1_name + "? (Pet/Play) ")
                                        if Livingroom_pet_or_play.lower() == "pet" or Livingroom_pet_or_play.lower() == "play":
                                            if Livingroom_pet_or_play.lower() == "pet":
                                                if pet1_type.lower() == "dog":
                                                    print(happy_sounds_dog + ", " + pet1_name + "is really enjoying that rub in the tummy!!")
                                                    pet1_happiness = pet1_happiness + 9.6
                                                else:
                                                    print(happy_sounds_cat + ", " + pet1_name + "is really enjoying that rub in the tummy!!")
                                                    pet1_happiness = pet1_happiness + 9.6
                                            else:
                                                if pet1_type.lower() == "dog":
                                                    print(happy_sounds_dog + ", " + pet1_name + " is chasing after that ball! It's so excited it almost knocked over the table!!")
                                                    pet1_happiness = pet1_happiness + 13.21
                                                    pet1_hunger = pet1_hunger + 10.90
                                                else:
                                                    print(happy_sounds_cat + ", " + pet1_name + " loves pouncing at that cat wand! Such a predator!")
                                                    pet1_happiness = pet1_happiness + 13.21
                                                    pet1_hunger = pet1_hunger + 10.90
                                else:
                                    if pet1_type.lower() == "dog":
                                        print(Angry_sounds_dog + "! Oh no, " + pet1_name + " is a bit angry, it doesn't want to come!")
                                        Livingroom_failed_call = input(player_name + "which one of the following actions would you like to perform next? (Find/Leave) ")
                                        #find or leave again
                                        if Livingroom_failed_call.lower() == "find" or Livingroom_failed_call.lower() == "leave":
                                            if Livingroom_failed_call.lower() == "find":
                                                livingroom_find_food = input("Which type of pet food do you want to look for? (Simple/Lavish) ")
                                                if livingroom_find_food.lower() == "simple" or livingroom_find_food.lower() == "lavish":
                                                    if livingroom_find_food.lower() == "simple":
                                                        print("Looking around the room, you found the simple pet food stored in the corner of the overhead cupboard.")
                                                        print("Great, now we have some pet food, lets go to the kitchen!")
                                                        player_position = "kitchen"
                                                    else:
                                                        print("You remembered that the lavish pet food was delivered yesterday, and you grabbed it out of the box.")
                                                        print("Great, now we have some pet food, lets go to the kitchen!")
                                                        player_position = "kitchen"
                                                else:
                                                    print("Invalid action: please select (Simple/Lavish)")
                                                    exit()
                                            else:
                                                print("Alright, lets move on to the kitchen immediately!")
                                                player_position = "kitchen"   
                                        else:
                                            print("Invalid action: please select (Find/Leave)")
                                            exit()
                                            
                                    else:
                                        print(Angry_sounds_cat + "! Oh no, " + pet1_name + " is a bit angry, it doesn't want to come!")
                                        Livingroom_failed_call = input(player_name + "which one of the following actions would you like to perform next? (Find/Leave) ")
                                        #find or leave again
                                        if Livingroom_failed_call.lower() == "find" or Livingroom_failed_call.lower() == "leave":
                                            if Livingroom_failed_call.lower() == "find":
                                                livingroom_find_food = input("Which type of pet food do you want to look for? (Simple/Lavish) ")
                                                if livingroom_find_food.lower() == "simple" or livingroom_find_food.lower() == "lavish":
                                                    if livingroom_find_food.lower() == "simple":
                                                        print("Looking around the room, you found the simple pet food stored in the corner of the overhead cupboard.")
                                                        print("Great, now we have some pet food, lets go to the kitchen!")
                                                        player_position = "kitchen"
                                                    else:
                                                        print("You remembered that the lavish pet food was delivered yesterday, and you grabbed it out of the box.")
                                                        print("Great, now we have some pet food, lets go to the kitchen!")
                                                        player_position = "kitchen"
                                                else:
                                                    print("Invalid action: please select (Simple/Lavish)")
                                                    exit()
                                            else:
                                                print("Alright, lets move on to the kitchen immediately!")
                                                player_position = "kitchen"   
                                        else:
                                            print("Invalid action: please select (Find/Leave)")
                                            exit()
                            else:
                                Livingroom_No_call = input(player_name + "which one of the following actions would you like to perform next? (Find/Leave) ")
                                if Livingroom_No_call.lower == "find" or Livingroom_No_call.lower == "leave":
                                    if Livingroom_No_call.lower == "find":
                                        livingroom_find_food = input("Which type of pet food do you want to look for? (Simple/Lavish) ")
                                        if livingroom_find_food.lower() == "simple" or livingroom_find_food.lower() == "lavish":
                                            if livingroom_find_food.lower() == "simple":
                                                print("Looking around the room, you found the simple pet food stored in the corner of the overhead cupboard.")
                                                print("Great, now we have some pet food, lets go to the kitchen!")
                                                player_position = "kitchen"
                                            else:
                                                print("You remembered that the lavish pet food was delivered yesterday, and you grabbed it out of the box.")
                                                print("Great, now we have some pet food, lets go to the kitchen!")
                                                player_position = "kitchen"
                                        else:
                                            print("Invalid action: please select (Simple/Lavish)")
                                            exit()
                                    else:
                                        print("Alright, lets move on to the kitchen immediately!")
                                        player_position = "kitchen"
                                                
                                else:
                                    print("Invalid action: please select (Find/Leave)")
                                    exit()
        
                        else:
                            print("Invalid action: please select (Yes/No)")
                            exit()
                if which_pet == 2:
                    if pet2_location.lower() == "kitchen":
                        Livingroom_pet_or_play = input(player_name + ", do you want to pet or play with " + pet2_name + "? (Pet/Play) ")
                        if Livingroom_pet_or_play.lower() == "pet" or Livingroom_pet_or_play.lower() == "play":
                            if Livingroom_pet_or_play.lower() == "pet":
                                if pet2_type.lower() == "dog":
                                    print(happy_sounds_dog + ", " + pet2_name + "is really enjoying that rub in the tummy!!")
                                    pet2_happiness = pet2_happiness + 9.6
                                else:
                                    print(happy_sounds_cat + ", " + pet2_name + "is really enjoying that rub in the tummy!!")
                                    pet2_happiness = pet2_happiness + 9.6
                            else:
                                if pet2_type.lower() == "dog":
                                    print(happy_sounds_dog + ", " + pet2_name + " is chasing after that ball! It's so excited it almost knocked over the table!!")
                                    pet2_happiness = pet2_happiness + 13.21
                                    pet2_hunger = pet2_hunger + 10.90
                                else:
                                    print(happy_sounds_cat + ", " + pet2_name + " loves pouncing at that cat wand! Such a predator!")
                                    pet2_happiness = pet2_happiness + 13.21
                                    pet2_hunger = pet2_hunger + 10.90
                        else:
                            print("Invalid action: please select (pet or play)")
                    #location not kitchen                    
                    else:
                        Living_room_call = input(pet2_name + " is not in the living room, do you want to call it? (Yes/No) ")
                        if Living_room_call.lower() == "yes" or Living_room_call.lower() == "no":
                            if Living_room_call.lower() == "yes":
                                if pet2_happiness >= 20 and pet2_hunger < 90:
                                    pet2_location = "kitchen"
                                    #repeat code for pet location == kitchen
                                    if pet2_location.lower() == "kitchen":
                                        Livingroom_pet_or_play = input(player_name + ", do you want to pet or play with " + pet2_name + "? (Pet/Play) ")
                                        if Livingroom_pet_or_play.lower() == "pet" or Livingroom_pet_or_play.lower() == "play":
                                            if Livingroom_pet_or_play.lower() == "pet":
                                                if pet2_type.lower() == "dog":
                                                    print(happy_sounds_dog + ", " + pet2_name + "is really enjoying that rub in the tummy!!")
                                                    pet2_happiness = pet2_happiness + 9.6
                                                else:
                                                    print(happy_sounds_cat + ", " + pet2_name + "is really enjoying that rub in the tummy!!")
                                                    pet2_happiness = pet2_happiness + 9.6
                                            else:
                                                if pet2_type.lower() == "dog":
                                                    print(happy_sounds_dog + ", " + pet2_name + " is chasing after that ball! It's so excited it almost knocked over the table!!")
                                                    pet2_happiness = pet2_happiness + 13.21
                                                    pet2_hunger = pet2_hunger + 10.90
                                                else:
                                                    print(happy_sounds_cat + ", " + pet2_name + " loves pouncing at that cat wand! Such a predator!")
                                                    pet2_happiness = pet2_happiness + 13.21
                                                    pet2_hunger = pet2_hunger + 10.90
                                else:
                                    if pet2_type.lower() == "dog":
                                        print(Angry_sounds_dog + "! Oh no, " + pet2_name + " is a bit angry, it doesn't want to come!")
                                        Livingroom_failed_call = input(player_name + "which one of the following actions would you like to perform next? (Find/Leave) ")
                                        #find or leave again
                                        if Livingroom_failed_call.lower() == "find" or Livingroom_failed_call.lower() == "leave":
                                            if Livingroom_failed_call.lower() == "find":
                                                livingroom_find_food = input("Which type of pet food do you want to look for? (Simple/Lavish) ")
                                                if livingroom_find_food.lower() == "simple" or livingroom_find_food.lower() == "lavish":
                                                    if livingroom_find_food.lower() == "simple":
                                                        print("Looking around the room, you found the simple pet food stored in the corner of the overhead cupboard.")
                                                        print("Great, now we have some pet food, lets go to the kitchen!")
                                                        player_position = "kitchen"
                                                    else:
                                                        print("You remembered that the lavish pet food was delivered yesterday, and you grabbed it out of the box.")
                                                        print("Great, now we have some pet food, lets go to the kitchen!")
                                                        player_position = "kitchen"
                                                else:
                                                    print("Invalid action: please select (Simple/Lavish)")
                                                    exit()
                                            else:
                                                print("Alright, lets move on to the kitchen immediately!")
                                                player_position = "kitchen"   
                                        else:
                                            print("Invalid action: please select (Find/Leave)")
                                            exit()
                                            
                                    else:
                                        print(Angry_sounds_cat + "! Oh no, " + pet2_name + " is a bit angry, it doesn't want to come!")
                                        Livingroom_failed_call = input(player_name + "which one of the following actions would you like to perform next? (Find/Leave) ")
                                        #find or leave again
                                        if Livingroom_failed_call.lower() == "find" or Livingroom_failed_call.lower() == "leave":
                                            if Livingroom_failed_call.lower() == "find":
                                                livingroom_find_food = input("Which type of pet food do you want to look for? (Simple/Lavish) ")
                                                if livingroom_find_food.lower() == "simple" or livingroom_find_food.lower() == "lavish":
                                                    if livingroom_find_food.lower() == "simple":
                                                        print("Looking around the room, you found the simple pet food stored in the corner of the overhead cupboard.")
                                                        print("Great, now we have some pet food, lets go to the kitchen!")
                                                        player_position = "kitchen"
                                                    else:
                                                        print("You remembered that the lavish pet food was delivered yesterday, and you grabbed it out of the box.")
                                                        print("Great, now we have some pet food, lets go to the kitchen!")
                                                        player_position = "kitchen"
                                                else:
                                                    print("Invalid action: please select (Simple/Lavish)")
                                                    exit()
                                            else:
                                                print("Alright, lets move on to the kitchen immediately!")
                                                player_position = "kitchen"   
                                        else:
                                            print("Invalid action: please select (Find/Leave)")
                                            exit()
                            else:
                                Livingroom_No_call = input(player_name + "which one of the following actions would you like to perform next? (Find/Leave) ")
                                if Livingroom_No_call.lower == "find" or Livingroom_No_call.lower == "leave":
                                    if Livingroom_No_call.lower == "find":
                                        livingroom_find_food = input("Which type of pet food do you want to look for? (Simple/Lavish) ")
                                        if livingroom_find_food.lower() == "simple" or livingroom_find_food.lower() == "lavish":
                                            if livingroom_find_food.lower() == "simple":
                                                print("Looking around the room, you found the simple pet food stored in the corner of the overhead cupboard.")
                                                print("Great, now we have some pet food, lets go to the kitchen!")
                                                player_position = "kitchen"
                                            else:
                                                print("You remembered that the lavish pet food was delivered yesterday, and you grabbed it out of the box.")
                                                print("Great, now we have some pet food, lets go to the kitchen!")
                                                player_position = "kitchen"
                                        else:
                                            print("Invalid action: please select (Simple/Lavish)")
                                            exit()
                                    else:
                                        print("Alright, lets move on to the kitchen immediately!")
                                        player_position = "kitchen"
                                                
                                else:
                                    print("Invalid action: please select (Find/Leave)")
                                    exit()
        
                        else:
                            print("Invalid action: please select (Yes/No)")
                            exit()

            else:
                print("Invalid action: please select (1/2)")
                exit()

        if livingroom_action.lower() == "find":
            livingroom_find_food = input("Which type of pet food do you want to look for? (Simple/Lavish) ")
            if livingroom_find_food.lower() == "simple" or livingroom_find_food.lower() == "lavish":
                if livingroom_find_food.lower() == "simple":
                    print("Looking around the room, you found the simple pet food stored in the corner of the overhead cupboard.")
                    print("Great, now we have some pet food, lets go to the kitchen!")
                    player_position = "kitchen"
                else:
                    print("You remembered that the lavish pet food was delivered yesterday, and you grabbed it out of the box.")
                    print("Great, now we have some pet food, lets go to the kitchen!")
                    player_position = "kitchen"
            else:
                print("Invalid action: please select (Simple/Lavish)")
                exit()

        if livingroom_action.lower() == "leave":
            print("Alright, lets move on to the kitchen immediately!")
            player_position = "kitchen"
    else:
        print("Invalid action: please select (Interact/Find/Leave)")
        exit()

    print(c)
    print(player_name + ", here is a summary of the current status of your pets:")
    print("Your little " + pet1_type + ", " + pet1_name + ", is in the " + pet1_location + " and is {:.2f}% happy and {:.2f}% hungry.".format(pet1_happiness, pet1_hunger))
    print("Your little " + pet2_type + ", " + pet2_name + ", is in the " + pet2_location + " and is {:.2f}% happy and {:.2f}% hungry.".format(pet2_happiness, pet2_hunger)) 
    e = """
                     _   __ _  _          _
                    | | / /(_)| |        | |
                    | |/ /  _ | |_   ___ | |__    ___  _ __
                    |    \ | || __| / __|| '_ \  / _ \| '_ \
                    | |\  \| || |_ | (__ | | | ||  __/| | | |
                    \_| \_/|_| \__| \___||_| |_| \___||_| |_|
            
"""
    print(e)
    player_position = "kitchen"
    pet1_location = "kitchen"
    pet2_location = "kitchen"
    print()
    print("Your pet heard that you're making food and decided to join you!")

    # prepare food methodical // chaotic 

    kitchen_prompt = input(player_name + ", do you want to make food methodically or chaotically, type M for methodically, C for chaotic ")
    if kitchen_prompt.lower() == "m" or kitchen_prompt.lower() == "c":
        if kitchen_prompt.lower() == "m":
            print("Answer the following question properly and we should be good!!")
            print()
            kitchen_methodquiz = input("Can" + pet_name + " eat chocolate??: (type Y for yes, N for no) ")
            if kitchen_methodquiz.lower() == "y" or kitchen_methodquiz.lower() == "n":
                if kitchen_methodquiz.lower() == "y":
                    print("HOORAY!!")
                    pet1_happiness = pet1_happiness + 10
                    pet2_happiness = pet2_happiness + 10
                    pet1_hunger = pet1_hunger - 50
                    pet2_hunger = pet2_hunger - 50
                    
                    if pet1_type.lower() == "dog":
                        print(happy_sounds_dog)
                    else:
                        print(happy_sounds_cat)

                    if pet2_type.lower() == "dog":
                        print(happy_sounds_dog)
                    else:
                        print(happy_sounds_cat)
                else:
                    print("WRONG ANSWER!!")
                    if pet1_type.lower() == "dog":
                        print(happy_sounds_dog)
                    else:
                        print(happy_sounds_cat)
                        
                    if pet2_type.lower() == "dog":
                        print(happy_sounds_dog)
                    else:
                        print(happy_sounds_cat)
            else:
                print("Invalid input: please type Y or N")
                exit()
        else:
            if kitchen_prompt.lower() == "c":
                chaotic_decision = input("Are you sure you want to continue? (Y/N): ")
                if chaotic_decision.lower() == "y" or chaotic_decision.lower() == "n":
                    if chaotic_decision.lower() == "y":
                        print("Alright sure but this will make your pet a bit mad")
                        pet1_happiness = pet1_happiness - 20
                        pet1_hunger = pet1_hunger - 25
                        pet2_happiness = pet2_happiness - 20
                        pet2_hunger = pet2_hunger - 25
                        if pet1_type.lower() == "dog":
                            print(happy_sounds_dog)
                        else:
                            print(happy_sounds_cat)
                            
                        if pet2_type.lower() == "dog":
                            print(happy_sounds_dog)
                        else:
                            print(happy_sounds_cat)
                else:
                    print("Invalid input: please type Y or N")
                    exit()         
    else:
        print("Invalid input: please type M or C")
        exit()
    # play
    print("Now that we have fed our pets!!")
    kitchenplay = int(input(player_name + ", which pet do you want to play with (1/2) "))
    if kitchenplay == 1 or kitchenplay == 2:
        if kitchenplay == 1:
            kitchen_pet_or_play = input(player_name + ", do you want to pet or play with " + pet1_name + "? (Pet/Play) ")
            if kitchen_pet_or_play.lower() == "pet" or kitchen_pet_or_play.lower() == "play":
                if kitchen_pet_or_play.lower() == "pet":
                    if pet1_type.lower() == "dog":
                        print(happy_sounds_dog + ", " + pet1_name + "is really enjoying that rub in the tummy!!")
                        pet1_happiness = pet1_happiness + 9.6
                    else:
                        print(happy_sounds_cat + ", " + pet1_name + "is really enjoying that rub in the tummy!!")
                        pet1_happiness = pet1_happiness + 9.6
                else:
                    if pet1_type.lower() == "dog":
                        print(happy_sounds_dog + ", " + pet1_name + " is chasing after that ball! It's so excited it almost knocked over the table!!")
                        pet1_happiness = pet1_happiness + 13.21
                        pet1_hunger = pet1_hunger + 10.90
                    else:
                        print(happy_sounds_cat + ", " + pet1_name + " loves pouncing at that cat wand! Such a predator!")
                        pet1_happiness = pet1_happiness + 13.21
                        pet1_hunger = pet1_hunger + 10.90
            else:
                print("Invalid action: please select (pet or play)")
        if kitchenplay == 2:
            kitchen_pet_or_play = input(player_name + ", do you want to pet or play with " + pet2_name + "? (Pet/Play) ")
            if kitchen_pet_or_play.lower() == "pet" or kitchen_pet_or_play.lower() == "play":
                if kitchen_pet_or_play.lower() == "pet":
                    if pet2_type.lower() == "dog":
                        print(happy_sounds_dog + ", " + pet2_name + "is really enjoying that rub in the tummy!!")
                        pet2_happiness = pet2_happiness + 9.6
                    else:
                        print(happy_sounds_cat + ", " + pet2_name + "is really enjoying that rub in the tummy!!")
                        pet2_happiness = pet2_happiness + 9.6
                else:
                    if pet2_type.lower() == "dog":
                        print(happy_sounds_dog + ", " + pet2_name + " is chasing after that ball! It's so excited it almost knocked over the table!!")
                        pet2_happiness = pet2_happiness + 13.21
                        pet2_hunger = pet2_hunger + 10.90
                    else:
                        print(happy_sounds_cat + ", " + pet2_name + " loves pouncing at that cat wand! Such a predator!")
                        pet2_happiness = pet2_happiness + 13.21
                        pet2_hunger = pet2_hunger + 10.90
            else:
                print("Invalid action: please select (pet or play)")

    else:
         print("Invalid action: please select (1/2)")
         exit()
    # leave to kitchen 

    print("Alright!! now that we have had our fun in the kitchen!! lets end with a beautiful view by the garden")
    view_prompt = input("Are you ready to go off into the kitchen: (Y/N): ")
    if view_prompt.lower == "n":
        exit()
    else: 
        print("Well done!")

    f = """
                    _____                   _              
                    |  __ \                 | |             
                    | |  \/  __ _  _ __   __| |  ___  _ __  
                    | | __  / _` || '__| / _` | / _ \| '_ \ 
                    | |_\ \| (_| || |   | (_| ||  __/| | | |
                     \____/ \__,_||_|    \__,_| \___||_| |_|        

"""
    print(f)

    print(player_name + ", Well done on going so far, lets see if you passed or failed")
    print("Bare in mind that to pass, both your pets happiness level must be over 50 and your pets hunger must be below 50")

    if pet1_happiness > 100:
        pet1_happiness = 100 
    if pet1_hunger > 100:
        pet1_hunger = 100
    if pet2_happiness > 100:
        pet2_happiness = 100 
    if pet2_hunger > 100:
        pet2_hunger = 100

    if pet2_happiness > 50 and pet1_hunger < 50 and pet2_happiness > 50 and pet2_hunger < 50:
        print("WOOHOOO YOU PASSED!!!!")
        if pet1_type.lower() == "dog":
            print(happy_sounds_dog)
        else:
            print(happy_sounds_cat)
        if pet2_type.lower() == "dog":
            print(happy_sounds_dog)
        else:
            print(happy_sounds_cat)
    else:
        print("Unfortunately you didnt pass :( feel free to try again)")
        exit()
    g = """
====================================GAME END=====================================
"""
    print(g)
