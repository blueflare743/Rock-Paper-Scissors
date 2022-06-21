
class Player():
    def select_twoplayer(self):
         self.choice = input('Player one select Rock, Paper, or Scissors') 
     
    def select(self):
          self.choice2 = input('Player two select Rock, Paper, or Scissors') 
          
    def select_singleplayer(self):
        
        self.choice = input('Player one select Rock, Paper, or Scissors.')
    def game_on(self):

      p2 = Player()
      p2.select_twoplayer()
      p2.select()

      

          