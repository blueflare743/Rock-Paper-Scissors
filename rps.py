import random
from player import Player



class Rps(Player):
    def __init__(self, ):
 
        def random(self):
            num  = random.randint(0,3)
            list = ['Rock', 'Paper', 'Scissors']
            generated =  list[num]
            self.comp_choice = generated
            return self.comp_choice
            
    def win_condition_double(self):
        #check if someone wins or not
        # using a tuple
        while True:
            p1 = Player()
            rps = Rps()
            p1.select_twoplayer()
            p1.select()
            
            if (p1.choice, p1.choice2) == ('Rock', 'Paper'):
                print('Player two Won!')
                return True
                break
            elif (p1.choice, p1.choice2) == ('Paper', 'Scissors'):
                print('Player two Won!')
                return True
                break
            elif (p1.choice, p1.choice2) == ('Rock', 'Scissors'):
                return True
                print('Player One Wins!')
                break   
            elif (p1.choice, p1.choice2) == ('Paper', 'Rock'):
                print('Player One Won!')
                return True
                break
            elif (p1.choice, p1.choice2) == ('Scissors', 'Paper'):
                print('Player One Won!')
                return True
                break
            elif (p1.choice, p1.choice2) == ('Scissors', 'Rock'):
                return True
                print('Player Two Wins!')
                break    
            else:
                rps.select_twoplayer()
                rps.select()
                continue
    def win_conditiion_single(self):
         while True:
            p1 = Player()
            p1.select_singleplayer()
            rps = Rps()
            num  = random.randint(0,3)
            list = ['Rock', 'Paper', 'Scissors']
            generated =  list[num]
            self.comp_choice = generated
         

            if (p1.choice, self.comp_choice) == ('Rock', 'Paper'):
                print(self.comp_choice)
                print("The computer chose {}".format(self.comp_choice))
                print('You lost.')
                return True
                break
            elif (p1.choice, self.comp_choice) == ('Paper', 'Scissors'):
                print("The computer chose {}".format(self.comp_choice))
                print('You lost')
                return True
                break
            elif (p1.choice, self.comp_choice) == ('Rock', 'Scissors'):
                print("The computer chose {}".format(self.comp_choice))
                print('You Won!')
                return True
                break   
            elif (p1.choice, self.comp_choice) == ('Paper', 'Rock'):
                print("The computer chose {}".format(self.comp_choice)) 
                print('You Won')
                return True
                break
            elif (p1.choice, self.comp_choice) == ('Scissors', 'Paper'):
                print("The computer chose {}".format(print(generated))) 
                print('You Won!')
                return True
                break
            elif (p1.choice, self.comp_choice) == ('Scissors', 'Rock'): 
                 print("The computer chose {}".format(print(generated))) 
                 print('You Lost!')
                 return True
                 break
            else:
                print("The computer chose {}".format(print(self.comp_choice))) 
                rps.select_singleplayer()
                continue
            
             
