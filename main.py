import time # Adds time delay in seconds
    # time.sleep(2)
    # time.sleep(2)
    # time.sleep(2)
    # time.sleep(3)
    # time.sleep(4)
    # time.sleep(5)


from termcolor import colored # Changes text colours
    # Available colors = ['pink', 'yellow', 'cyan', 'magenta', 'blue', 'gray', 'default', 'black', 'green', 'white', 'red']
    # print(colored('Hello, World!', 'red'))

# to clear the screen
class cls(object):
    def __repr__(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear') # works on windows and linux
        return ''
cls = cls() # print(cls) to clear screen

# easier to call than print
def clearScreen():
    print(cls, end="")

# Defining variables
enter = ''
action = 0
yourName = ''
hotelRestaurant = ''
optionA = ''
optionB = ''
optionC = ''

# Defining colored variables
Pablo = colored('   Pablo:', 'red',)
Police = colored('   Officer:', 'blue')
You = colored('   You:', 'green',)
OptionA = colored('Option A:', 'yellow')
OptionB = colored('Option B:', 'yellow')
OptionC = colored('Option C:', 'yellow')

# Defining image text
youDied = colored('''

▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██  █████ ▓█████▄
 ▒██  ██  ██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌ ██  █   ▀ ▒██▀ ██▌
  ▒██ ██ ▒██░  ██▒ ██  ▒██░   ░██   █▌ ██  ███   ░██   █▌
  ░ ▐██▓  ██   ██░ ▓█  ░██░   ░▓█▄   ▌ ██  ▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓   ████▓▒  ▒█████▓    ░▒████▓  ██  ▒████ ░▒████▓
   ██▒▒▒ ░ ▒░▒░▒░  ▒▓▒ ▒ ▒     ▒▒▓  ▒  ▓  ░░ ▒░   ▒▒▓  ▒
 ▓██ ░▒░   ░ ▒ ▒░  ░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░
 ░ ░                           ░                  ░
''', 'red')

youAreRighteous = colored('''
__   __              ___             ______ _       _     _
\ \ / /             / _ \            | ___ (_)     | |   | |
 \ V /___  _   _   / /_\ \_ __ ___   | |_/ /_  __ _| |__ | |_ ___  ___  _   _ ___
  \ // _ \| | | |  |  _  | '__/ _ \  |    /| |/ _` | '_ \| __/ _ \/ _ \| | | / __|
  | | (_) | |_| |  | | | | | |  __/  | |\ \| | (_| | | | | ||  __/ (_) | |_| \__ \\
  \_/\___/ \__,_|  \_| |_/_|  \___|  \_| \_|_|\__, |_| |_|\__\___|\___/ \__,_|___/
                                               __/ |
                                              |___/
''', 'blue')

youAreATraitor = colored('''
_____ ___                                                    __                 __  __
\__  |   | ____  __ __   _____  ______   ____    _____     _/  |_____________  |__|/  |_  ___________
 /   |   |/  _ \|  |  \  \__  \ |  __ \_/ __ \   \__  \    \   __\_  __ \__  \ |  \   __\/  _ \_  __ \\
 \____   (  <_> )  |  /   / __ \|  | \/\  ___/    / __ \_   |  |  |  | \// __ \|  ||  | (  <_> )  | \/
 / ______|\____/|____/   (____  /__|    \___  >  (____  /   |__|  |__|  (____  /__||__|  \____/|__|
 \/                           \/            \/        \/                     \/
''', 'red')

youAreSympatheticText = colored('''
__  __                 ___                   _____                             __  __         __  _
\ \/ /___  __  __     /   |  ________       / ___/__  ______ ___  ____  ____ _/ /_/ /_  ___  / /_(_)____
 \  / __ \/ / / /    / /| | / ___/ _ \      \__ \/ / / / __ `__ \/ __ \/ __ `/ __/ __ \/ _ \/ __/ / ___/
 / / /_/ / /_/ /    / ___ |/ /  /  __/     ___/ / /_/ / / / / / / /_/ / /_/ / /_/ / / /  __/ /_/ / /__
/_/\____/\__,_/    /_/  |_/_/   \___/     /____/\__, /_/ /_/ /_/ .___/\__,_/\__/_/ /_/\___/\__/_/\___/
                                               /____/         /_/
''', 'yellow')

youAreLoyal = colored('''
 _                        _
| |                      | |
| |      ___  _   _ _____| |
| |     / _ \| | | (____ | |
| |____| |_| | |_| / ___ | |
|_______)___/ \__  \_____|\_)
             (____/
''', 'green')

# Defining functions
# Breaks scenes and clears screen
def enterContinue():
    input(colored('Press Enter to Continue', 'cyan', attrs=['blink']))
    clearScreen()
    # replit.clear()

# Options function
def action(rep):
  # sets a global variable: choice
  global choice
  # For options A or B
  while rep == 1:
    # User input for options A and B
    print('------------------------------------------------------------------')
    action = input(colored('Enter your choice [A/B]: ', 'cyan'))
    print('------------------------------------------------------------------')
    # if the user iputs a lower or higher case A or B
    if action == "a" or action == "A":
      choice = "a"
      rep = 0
    elif action == "b" or action == "B":
      choice = "b"
      rep = 0
    # If the user inputs anything other than the options
    else:
      print(colored('Please only input either: a/A or b/B', 'cyan'))
      rep = 1
  # For option A, B or C
  while rep == 2:
    # User input for options A, B and C
    print('------------------------------------------------------------------')
    action = input(colored('Enter your choice [A/B/C]:', 'cyan'))
    print('------------------------------------------------------------------')
      # if the user iputs a lower or higher case A, B or C
    if action == "a" or action == "A":
      choice = "a"
      rep = 0
    elif action == "b" or action == "B":
      choice = "b"
      rep = 0
    elif action == "c" or action == "C":
      choice = "c"
      rep = 0
        # If the user inputs anything other than the options
    else:
      print(colored('Please only input either: a/A, b/B or c/C', 'cyan'))
      rep = 2
  # Returns the variable to outside the function
  enterContinue()
  return choice


# Intro
def intro():
    global yourName
    # replit.clear()
    clearScreen()
    print('\nWelcome!')
    time.sleep(2)
    print('This is a Text-Based Adventure!')
    time.sleep(2)
    print('You will be given different options to choose from.')
    time.sleep(2)
    print('Your choices will effect the outcome of the game, choose wisely.')
    time.sleep(2)
    print('------------------------------------------------------------------')
    yourName = input("Enter your name: ")
    print('------------------------------------------------------------------')
    time.sleep(2)
    print('\nWelcome', yourName, ', thanks for playing this game')
    time.sleep(2)
    print('\nAre you ready to start?\n')
    time.sleep(1)
    enterContinue()
    return yourName

# Game Intro
def gameIntro():
    global hotelRestaurant
    print('')
    print(yourName, "!!!,")
    time.sleep(1)
    print("\nYou have been in prison for 3 months for being involved with the infamous, Pablo Escobar.")
    time.sleep(3)
    print("However, Pablo Escobar hasn't been caught yet.")
    time.sleep(2)
    print("Due to your involvement with Pablo, the police want you to help get evidence to put Pablo behind bars.")
    time.sleep(3)
    print("They have sent you to do a drug deal with him.")
    time.sleep(2)
    print("\nWhere would you like to meet Pablo?")
    print('\n------------------------------------------------------------------')
    print(OptionA, 'Restaurant')
    time.sleep(1)
    print(OptionB, 'Hotel')
    time.sleep(1)
    action(1)
    if choice == "a":
        hotelRestaurant = "restaurant"
        print("\nYou have decided to meet Pablo at an italian restaurant.")
    elif choice == "b":
        hotelRestaurant = "hotel"
        print("\nYou have decided to meet Pablo at a 5 star hotel.")
    time.sleep(2)
    print("\nYou have done business with him before in the past so he believes that you are trustworthy.\n")
    introDialogue()
    return hotelRestaurant

# Intro dialogue
def introDialogue():
    time.sleep(2)
    print(Pablo, "It has been a very long time since I met you.\n")
    time.sleep(2)
    print(You, "Yes it has my brother ... do you have the stuff?\n")
    time.sleep(2)
    print(Pablo, "Yes my brother. I have a whopper load of crack in the bag. However, you can only get the stash if you got the cash.\n")
    time.sleep(3)
    print('------------------------------------------------------------------')
    print(OptionA, 'Consult with police on what to do next')
    time.sleep(2)
    print(OptionB, 'Accept deal without consulting with police')
    time.sleep(2)
    action(1)
    if choice == "a":
        toilet()
    elif choice == "b":
        print('------------------------------------------------------------------\n')
        accept()

# intro dialogue: Option A
def toilet():
    print('------------------------------------------------------------------\n')
    print(You, "Excuse me Pablo, I have to use the restroom.\n")
    time.sleep(2)
    print("You have excused yourself and are now on the phone with the police\n")
    time.sleep(3)
    print(You, "I have met Pablo and he said that he has a 'whopper load of crack'.\n")
    time.sleep(3)
    print(Police, "Hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm... Okay ... Ask Pablo for his address. We need the address of his headquarters where he keeps his drugs.\n")
    time.sleep(4)
    print('------------------------------------------------------------------')
    print(OptionA, 'Follow officers command')
    time.sleep(1)
    print(OptionB, "Don't follow officers command and take the drug deal")
    action(1)
    print('------------------------------------------------------------------\n')
    print(You, "Okay officer.\n")
    time.sleep(1)
    print("You step out of the toilet and you walk towards Pablo\n")
    if choice == "a":
        address()
    elif choice == "b":
        accept()

# toilet: Option A
def address():
    print(You, "Unfortunately, I do not have the cash required at the moment. Can you give me your headquarters address? I will send you the cash when I get it.\n")
    time.sleep(2)
    print(Pablo, "Hmmmmmmmmmmmmmmmmmmmmmmmmmm ... Unfortunately I cannot trust anyone with my address.\n")
    time.sleep(1)
    print(You, "You can trust me\n")
    time.sleep(1)
    print(Pablo, "No I cannot, you have just been released from prison. Not to mention that you are known to be a very untrustworthy person.\n")
    time.sleep(2)
    print(You, " ... \n")
    time.sleep(1)
    print(Pablo, "I had a hunch that you working for the police. I cannot trust you with my address.\n")
    time.sleep(3)
    print("*Pablo draws his pistol and points it at you*\n")
    time.sleep(2)
    print(Pablo, "Any last words,", yourName, "?\n")
    time.sleep(1)
    lastWords = input (colored ("   You (Enter your last words): ", 'green'))
    time.sleep(2)
    print('\nPablo: ', '"', lastWords, '"' , '?, really is that it?')
    time.sleep(2)
    print("\n*Pablo shoots you point blank in the head...*\n")
    time.sleep(2)
    print(You, "died\n", youDied, '\n\n')
    time.sleep(2)
    print("Ending:\n")
    time.sleep(1)
    print("Pablo kills you and flees the", hotelRestaurant, "in a helicopter. Your body was buried and you were forgotten. Pablo was captured and sent to prison 2 years later but he escaped the next day. He died 3 years later in a shootout.\n")
    time.sleep(4)
    print("You are a traitor./n", youAreATraitor)

# intro dialogue/toilet: Option A
def accept():
    print(You, "Do not fear I have the required cash.\n")
    time.sleep(2)
    print(Pablo, "I knew I could trust you brother.\n")
    time.sleep(2)
    print("* Pablo takes out briefcase stuffed with crack *\n")
    time.sleep(2)
    print(You, "Fantastic\n")
    time.sleep(1)
    print("* You take out briefcase with the money *\n")
    time.sleep(2)
    print("* You both exchange briefcases *\n")
    time.sleep(2)
    print(Pablo, "Here is my address, It is confidential so you must not tell anyone that you even know my address.\n")
    time.sleep(3)
    print(You, "Okay\n")
    time.sleep(1)
    print(Pablo, "If you ever want crack in the future you can contact me. I will give you a loyalty discount\n")
    time.sleep(3)
    print("* Pablo hands over his new business card to you *\n")
    time.sleep(2)
    print('------------------------------------------------------------------')
    time.sleep(1)
    print(OptionA, "betray Pablo and give the address and the evidence of Pablo drug dealing to the police.")
    time.sleep(2)
    print(OptionB, "betray the police and get back into drug dealing along side Pablo.")
    time.sleep(2)
    print(OptionC, "play a dirty trick on Pablo. When he isn't looking switch the briefcase with money that you gave him with a briefcase filled with paper. So you then have both the briefcase with money and cocaine.")
    time.sleep(4)
    action(2)
    if choice == "a":
        betrayPablo()
    elif choice == "b":
        betrayPolice()
    elif choice == "c":
        switchBriefcase()

# accept: Option A
def betrayPablo():
    print('------------------------------------------------------------------\n')
    print("You chose to betray Pablo and give the address and the evidence of Pablo drug dealing to the police.\n")
    time.sleep(3)
    print(You, "It has been good doing business with you.\n")
    time.sleep(2)
    print("*You leave*\n\n")
    time.sleep(1)
    print("Ending:\n")
    time.sleep(1)
    print("You leave the deal with what the police wanted. You later give the police Pablo's address. The police release you from jail and lock up Pablo.\n")
    time.sleep(4)
    print("You are righteous\n", youAreRighteous)

# accept: Option B
def betrayPolice():
    print('------------------------------------------------------------------\n')
    print("You chose to betray the police and get back into drug dealing along side Pablo.\n" )
    time.sleep(3)
    print(You, "It has been good doing business with you.\n")
    time.sleep(2)
    print(Pablo, "Yes it has, but we have to get out quick before anyone gets suspicious.\n")
    time.sleep(3)
    print(You, "Yes brother, we must flee. The police tried to set you up. They sent me to find out information about you.\n")
    time.sleep(3)
    print(Pablo, "Foolish police, they will never learn\n")
    time.sleep(2)
    print(You, "Yes lets go\n\n")
    time.sleep(1)
    print("Ending:\n")
    time.sleep(1)
    print("You and Pablo leave the", hotelRestaurant," and helicopter away to Pablo's den. You lost all contact with the police. Three years later Pablo died in a shootout.\n")
    time.sleep(4)
    print("You are loyal\n", youAreLoyal)

# accept: Option C
def switchBriefcase():
    print('------------------------------------------------------------------\n')
    print(You, "It has been good doing business with you.\n")
    time.sleep(2)
    print("* Pablo accidently spills some cocaine on the floor *\n")
    time.sleep(2)
    print(Pablo, "Bollox, I spilled some crack on the floor. I need to clean it up before anyone sees.\n")
    time.sleep(3)
    print("Pablo awkwardly leans down and suspiciously cleans cocaine of the floor with a tissue.\n")
    time.sleep(3)
    print(colored('   You (aside):', 'green'), "This is my chance\n")
    time.sleep(2)
    print("*You switch briefcases*\n")
    time.sleep(1)
    print(Pablo, "Did anyone see?\n")
    time.sleep(1)
    print(You, "No\n")
    time.sleep(1)
    print('------------------------------------------------------------------')
    print(OptionA, "Try run away with the cash and drugs")
    time.sleep(1)
    print(OptionB, "Wait until the deal is over and hope Pablo doesn't notice")
    time.sleep(1)
    action(1)
    if choice == "a":
        switchBriefcaseRun()
    elif choice == "b":
        waitForPablo()

# switchBriefcase: Option A
def switchBriefcaseRun():
    print('------------------------------------------------------------------\n')
    print("You chose to try run away with the cash and drugs\n")
    time.sleep(2)
    print(You,"Pablo!\n")
    time.sleep(.5)
    print(Pablo,"What!?\n")
    time.sleep(1)
    print(You,"Look behind you!\n")
    time.sleep(1)
    print("Pablo turns his head and you sprint for the exit with the cocaine and cash\n")
    time.sleep(2)
    print(Pablo,"What there's nothing there ... Wait! where are you going!?\n")
    time.sleep(2)
    print("Pablo notices that you're running away with two suitcases\n")
    time.sleep(2)
    print(colored('   Pablo (aside):', 'red'), "I knew I couldn't trust him\n")
    time.sleep(2)
    print("* Pablo takes out his pistol and shoots you in right in the head *\n")
    time.sleep(1)
    print("You died", youDied, '\n\n')
    print("Ending:\n")
    print("Pablo kills you and flees the", hotelRestaurant, "in a helicopter. Pablo was captured and sent to prison two months after you died but he escapes the next day. He died three years later in a shootout. Your body was buried and you were forgotten.\n")
    time.sleep(5)
    print("You are a traitor.\n", youAreATraitor)

# switchBriefcase: Option B
def waitForPablo():
    print('------------------------------------------------------------------\n')
    print("You chose to wait until the deal is over and hope Pablo doesn't notice.\n")
    time.sleep(3)
    print(You, "Okay, I must get going now\n")
    time.sleep(2)
    print(Pablo, "Okay my brother, goodbye\n")
    time.sleep(2)
    print("* You and Pablo exit the", hotelRestaurant, "*\n" )
    time.sleep(2)
    print("5 minutes later after the deal, you and Pablo take seperate ways. Pablo is in his helicopter.\n")
    time.sleep(2)
    print(Pablo, " Hmmmmmmmmmmmmmmm, this briefcase feels a bit different.\n")
    time.sleep(2)
    print("* Pablo opens the briefcase *\n")
    time.sleep(2)
    print(Pablo,"Well, it appears I have been fooled.\n")
    time.sleep(2)
    print(colored('   Pablo (orders pilot):', 'red'), " Turn the helicopter around!\n")
    time.sleep(3)
    print(colored('   Pilot:', 'yellow'), " Roger sir!\n")
    time.sleep(2)
    print("You are currently on the streets, hoping Pablo doesn't find you.\n")
    time.sleep(3)
    print('------------------------------------------------------------------')
    time.sleep(1)
    print(OptionA, 'Go to the police and give the police his address.')
    time.sleep(2)
    print(OptionB, "Don't go to police and take the cocaine and money with you.")
    time.sleep(2)
    action(1)
    if choice == "a":
        police()
    elif choice == "b":
        leaveWithCases()

# waitForPablo: Option A
def police():
    print('------------------------------------------------------------------\n')
    print("You chose to go to the police and give the police his address.\n")
    time.sleep(3)
    print("You run to the police station to give the police Pablo's address.\n")
    time.sleep(3)
    print(Police,"Did you get his address and evidence?\n")
    time.sleep(2)
    print(You, "Yup.\n")
    time.sleep(1)
    print("You quickly reach your hand into your pocket and give the police Pablo's business card.\n")
    time.sleep(3)
    print(Police, "Good job", yourName,"\n")
    time.sleep(2)
    print(You,"Am I released from jail now?!\n")
    time.sleep(2)
    print(Police ,"Yes you are. Just give me the briefcases and you are set free.\n")
    time.sleep(3)
    print('------------------------------------------------------------------')
    time.sleep(1)
    print(OptionA, 'Give the officer the briefcases')
    time.sleep(2)
    print(OptionB, "Don't give the officer the briefcases and run away with them.")
    time.sleep(3)
    action(1)
    if choice == "a":
        giveBriefcases()
    elif choice == "b":
        runFromOfficer()

# police: Option A
def giveBriefcases():
    print('------------------------------------------------------------------\n')
    print("You chose to give the officer the briefcases.\n")
    time.sleep(2)
    print(You,"here.\n")
    time.sleep(1)
    print("* Gives officer briefcases *\n")
    time.sleep(2)
    print(Police, "Okay, you may leave now.\n")
    time.sleep(2)
    print("Ending:\n")
    time.sleep(1)
    print("You were released from prison and lived happily ever after. Although Pablo was put in prison and later he died a shootout.\n")
    time.sleep(4)
    print("You are righteous.\n", youAreRighteous)

# police: Option B
def runFromOfficer():
    print('------------------------------------------------------------------\n')
    print("You chose to not give the officer the briefcases and run away with them.\n")
    time.sleep(3)
    print(You,"Okay officer, can you just tell me where the restroom is please?\n")
    time.sleep(3)
    print(Police,"Yes, it's just over there, why?\n")
    time.sleep(2)
    print("The officer turns his head  and points behind him and you try run for the exit\n")
    time.sleep(3)
    print("* Officer turns his head *\n")
    time.sleep(2)
    print(colored('   Officer (shouts):', 'blue'), "Hey!\n")
    time.sleep(1)
    print("* draws pistol and shoots you *\n")
    time.sleep(2)
    print("You died\n", youDied)
    time.sleep(2)
    print("Ending:\n")
    time.sleep(1)
    print("Your body was buried and you were forgotten. Pablo didn't know you died until a month later. It was rumoured that Pablo went to your grave and destroyed it.\n")
    time.sleep(4)
    print("You are a traitor.\n", youAreATraitor)

# wait: Option B
def leaveWithCases():
    print('------------------------------------------------------------------\n')
    print("You chose to not go to police and take the cocaine and money with you.\n")
    time.sleep(3)
    print("Pablo has spotted you in his helicopter.")
    time.sleep(2)
    print(Pablo,"There he is!\n")
    time.sleep(2)
    print("* Pablo takes his sniper out *\n")
    time.sleep(2)
    print(Pablo,"Time to die\n")
    time.sleep(1)
    print("Pablo places his finger on the trigger\n")
    time.sleep(2)
    print("* Pablo places his foot forward but stumbles and falls out of the helicopter *\n")
    time.sleep(3)
    print(Pablo,"Bollox\n")
    time.sleep(1)
    print("Pablo's body plummets from the sky and he drops dead on the ground beside you.\n")
    time.sleep(3)
    print(You,"Pablo!?\n")
    time.sleep(1)
    print("Moments later, an ambulance arrives and takes Pablo's body away.\n")
    time.sleep(2)
    print('------------------------------------------------------------------')
    time.sleep(1)
    print(OptionA, 'Attend funeral')
    time.sleep(2)
    print(OptionB, "Don't give the officer the briefcases and run away with them.")
    time.sleep(3)
    action(1)
    if choice == "a":
        youAreSympathetic()
    elif choice == "b":
        dontAttendFuneral()

# leave: option A
def youAreSympathetic():
    print('------------------------------------------------------------------\n')
    print("Ending:\n")
    time.sleep(1)
    print("The following day you go to Pablo's funeral. You place both briefcases beside his grave to show your respect.\n")
    time.sleep(3)
    print("You are sympathetic towards Pablo.", youAreSympatheticText)

# leave: option B
def dontAttendFuneral():
    print('------------------------------------------------------------------\n')
    print("Ending:\n")
    time.sleep(1)
    print("The following day you leave and live your life funded by drug money always looking over your shoulder. You die with a guilty consience.\n")
    time.sleep(3)
    print("You feel guilty.")

# Start
intro()
gameIntro()