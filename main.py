from player import Player
from rps import Rps
decision = 'g'
while decision != 's' and  decision != 't':
    decision = input('Welcome to Rock Paper Scissors! Would you like to player single player or two player?')
    print(decision)
if decision == 't':


    name = input('Player one pick your Name:')
    name2 = input('Player two pick your Name:')
    rps = Rps()
    rps.win_condition_double()
else:
    rps1 = Rps()
    rps1.win_conditiion_single()


