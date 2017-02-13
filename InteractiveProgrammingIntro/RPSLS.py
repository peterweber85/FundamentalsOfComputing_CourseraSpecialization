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

# helper functions
import random as random

def name_to_number(name):
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print 'Error: unknown name'
    return number
   
def number_to_name(number):
    if number == 0:
        name = 'Rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print 'Error: number must in the range 0 to 4'
    return name
    

def rpsls(player_choice): 
    print 'Player chooses', player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5, 1)
    comp_choice = number_to_name(comp_number)
    print 'Computer chooses', comp_choice
    difference = player_number - comp_number    
    if 1<= difference % 5 <= 2:
        print 'Player wins'
    elif 4>= difference % 5 >= 3:
        print 'Computer wins'
    else:
        print 'Its a draw!!'
    print '\n'


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




