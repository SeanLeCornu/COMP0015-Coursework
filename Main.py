## 
#  This application is a fair grade allocator based on the work by: 
#  A. Procaccia, J. Goldman, N. Shah and D. Kurokawa.
#  Author: Group X
#  Date: Novemeber 2018


# imports modules used
import time
import os
import verify_funcs as vf
import sic
import calcs


# all definitions
def menu_screen():
    """This function prints the menu options.
    Note that it is only visual, so when called
    later it just reminds the user of possible 
    choices, it's not a recursive call"""
    
    os.system('clear')
    print("Welcome to Split-it!")

    print('''
    About          (A)
    Create Project (C)
    Enter Votes    (V)
    Show Projects  (S)
    Test           (T)
    Quit           (Q)
    ''')

    
def menu_redirect():
    """This function redirects the user to a different page.
    The user provides an input and is then redirected
    to the corresponding page. If an invalid choice is entered
    then the user is prompted to make another choice.
    This function is only called once!"""

    app_open = "*"
    while app_open != "q": 
        global menu_choice
        menu_choice = str(input("Please choose an " 
                                "option and press <Enter>: "))
        menu_choice = menu_choice.upper()

        if menu_choice == "A":
            about()
        elif menu_choice == "C":
            create_project()
        elif menu_choice == "V":
            enter_votes()
        elif menu_choice == "S":
            show_projects()
        elif menu_choice =="T":
            test_project()
        elif menu_choice == "Q":
            os.system('clear')
            print("Thanks for using Split-it! Closing application...")
            time.sleep(2)
            os.system('clear')
            app_open = "q"
        else:
            print("Please choose again")
            time.sleep(2)
            menu_screen ()
            
            
def menu():
    """This starts off the programme
    by calling the visual display and the 
    actual loop which requires input"""
    
    global project_dict
    project_dict = {}
    menu_screen()
    menu_redirect()


def enter_votes():
    """This looks up the project entered
    then prints the number of members 
    attribute of the project. Then it 
    allows team members to enter votes 
    for each other with validation
    constraints to stop bad input"""

    os.system('clear')
    global menu_choice
    global project_dict
    menu_choice = ""
    
    lookup = str(input("Enter the project name: " ))
    
    if lookup in project_dict:
        number = project_dict[lookup].NoOfMems
        proname = project_dict[lookup].name
        print("There are {} team members in {}"
              .format(number, proname))
        
        i = 0
        while i < number:
            votecount = 0 
            votedict = {}
            askvote1 = project_dict[lookup].members[i].name
            print ("Enter {}'s points the number must add up to 100"
                   .format(askvote1))
              
            for item in project_dict[lookup].members:
                askvote2 = str(item.name)
                if askvote1 == askvote2:
                    continue 
                else:
                    vote = input("\tEnter {}'s points for {} "
                                 .format(askvote1, askvote2))
                    vote = vf.voteInput(vote)
                    votecount += vote 
                    votedict[askvote2] = vote 
            
            if votecount != 100:
                print ("Sorry the votes you have "
                       "entered do not add up to 100")
            else: 
                project_dict[lookup].members[i].votes.update (votedict)
                i += 1
                
        else: 
            print ("All votes have been successfully entered")  
             
    else:
        print ("This project does not exist in the database")
        
    input("\n\nPress <Enter> to return to the main menu.")
    menu_screen()


def show_projects():
    """This displays a message for 
    two seconds then clears the console."""
    
    os.system('clear')
    global menu_choice
    global project_dict
    menu_choice = ""

    lookup = str(input("Enter the project name: "))

    if lookup in project_dict:
        number = project_dict[lookup].NoOfMems
        print("There are {} team members".format(number))

        if number == 3:
            member1 = calcs.member_creator(theLookup=lookup, search_dict=project_dict, index=0)
            print(member1.votes)
            print(member1.name, calcs.score_calc(member1))

            member2 = calcs.member_creator(theLookup=lookup, search_dict=project_dict, index=1)
            print(member2.votes)
            print(member2.name, calcs.score_calc(member2))

            member3 = calcs.member_creator(theLookup=lookup, search_dict=project_dict, index=2)
            print(member3.votes)
            print(member3.name, calcs.score_calc(member3))


        else:
            print("Only teams with 3 members can be processed")

    else:
        print ("This project does not exist in the database")

    input("\n\nPress <Enter> to return to the main menu.")
    menu_screen()


def about():
    """This displays information about the 
    programme and returns to the menu 
    screen on the user's command """

    os.system('clear')
    global menu_choice
    menu_choice = ""
    print("This is Split-it a coursework marking app")
    input("\n\nPress <Enter> to return to the main menu.")
    menu_screen()
    

def create_project():
    """This function allows the user to
    add a new team and participants."""

    os.system('clear')
    global menu_choice
    menu_choice = ""
    projectName = vf.getProjectName()
    teamSize = vf.getTeamSize()
    members = vf.getTeamNames(teamSize, projectName)

    global project_dict
    project_dict = {}
    project_dict[projectName] = sic.Project(theName=projectName, 
                                            theNoOfMems=teamSize, 
                                            theMembers=members)

  
    input("\n\nPress <Enter> to return to the main menu.")
    menu_screen()
    


 ######################################################################################### 
    
def test_project():
    
    os.system('clear')
    global menu_choice
    menu_choice = ""
    global project_dict
    #print (project_dict)
    
    masterstring = ''
    
    for item in project_dict:
        lookup = project_dict[item].name
        masterstring += (project_dict[item].name) + ','
        masterstring += str((project_dict[item].NoOfMems)) + ','
        
        i = 0
        for item in project_dict[lookup].members:
                masterstring += project_dict[lookup].members[i].name + ','
                i += 1
        
        i = 0
        for item in project_dict[lookup].members:
                masterstring += project_dict[lookup].members[i].name + ','
                votestring = str(project_dict[lookup].members[i].votes)
                votestring = votestring.replace('{', '')
                votestring = votestring.replace('}', '')
                votestring = votestring.replace(':', '')
                
                votelist = votestring.split()
                votestring = ''
                j = 0
                
                for item in votelist:
                    word = item
                    if j == 0: 
                        word = word[1:-1]
                        word = str(word)
                        votestring += word + ','                   
                        j += 1
                    else:
                        if word [-1:] == ',':
                            word = word[:-1]
                            word = str(word)
                        else: 
                            word = str(word)  
                        votestring += word + ','
                        j += -1 
                
                masterstring += votestring 
                i += 1
                
    print (masterstring)      
        
    input("\n\nPress <Enter> to return to the main menu.")
    menu_screen()

    
    ######################################################################################### 
       
    
#Calls the menu function which begins the programme
menu()




