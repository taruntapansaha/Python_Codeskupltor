# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random

# helper functions


def name_to_number(name):
    number = None
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print ("Please enter a valid choice")
    return number


def number_to_name(number):
    name = None
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print ("Please enter a valid choice")
    return name
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    print("")
    print "Player chooses ", player_choice 
    player_num = name_to_number(player_choice)
    
    comp_num = random.randrange(0,5)
    comp_choice = number_to_name(comp_num) 
    print "Computer chooses ", comp_choice
    
    cond = (comp_num - player_num)% 5
    
    if cond == 0:
        print "It is a Tie"
    elif (cond > 0 and cond <= 2):
        print "Comuter Wins"
    else:
        print "Player Wins"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


