import random

TEAM_SIZE = 5
GAME_LENGTH = 48

class Team:
    def __init__(self, name):
        self.__name = name
        self.__team = []
        self.__points = 0
        for i in range(TEAM_SIZE):
            player = BasketballPlayer(i+1) # i+1 is the number for the player
            self.__team.append(player)

    def play_offence(self):
        random_index = random.randint(0, TEAM_SIZE-1)
        self.__points += self.__team[random_index].shoot_ball()

    def get_player_with_highest_score(self):
        highest_player = self.__team[0]
        for player in self.__team:
            if player > highest_player:
                highest_player = player
                
        return highest_player

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def __str__(self):
        the_str = ''
        for player in self.__team:
            the_str += str(player)
        return the_str


class BasketballPlayer:
   def __init__(self, number):
      self.__number = number
      self.__points = 0

   def shoot_ball(self):
      shot = random.randint(0,1)
      if shot == 1:
         self.__points += 2
         return 2
      else:
         return 0

   def __gt__(self, other):
      return self.__points > other.__points

   def __str__(self):
      return "Number: {} Points: {}\n".format(self.__number, self.__points)
    

def print_winner(team_a, team_b):
   ''' You need to implement this function. Print out:
      which team won (if tie, print "Tie!")
   '''
   team_a_points = team_a.get_points()
   team_b_points = team_b.get_points()

   winner = ""
   if team_a_points > team_b_points:
      winner = team_a.get_name()
   elif team_a_points < team_b_points:
      winner = team_b.get_name()
   else:
      print("Tie!")
      return None

   print("{} won!".format(winner))


def print_scores(team_a, team_b):
   ''' You need to implent this function.  Print out:
      how many points each team scored
      the scoring of each player in each team
      the highest scoring player in each team  
   '''
   team_a_points = team_a.get_points()
   team_b_points = team_b.get_points()

   team_a_name = team_a.get_name()
   team_b_name = team_b.get_name()

   team_a_highest = team_a.get_player_with_highest_score()
   team_b_highest = team_b.get_player_with_highest_score()

   print("{} scored {} points!".format(team_a_name, team_a_points))
   print("{} scored {} points!".format(team_b_name, team_b_points))

   print("\n{} scoring:".format(team_a_name))
   print(team_a)

   print("\n{} scoring:".format(team_b_name))
   print(team_b)

   print("{} highest scoring player:".format(team_a_name))
   print(team_a_highest)

   print("{} highest scoring player:".format(team_b_name))
   print(team_b_highest)


   
    

def play(team_a, team_b):
    for _ in range(GAME_LENGTH):
        team_a.play_offence()    
        team_b.play_offence()
        
def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)

def main():
    # You are not allowed to change this main function
    random_seed()
    chicago_bulls = Team("Chicago Bulls")
    la_lakers = Team("LA Lakers")

    play(chicago_bulls, la_lakers)
    print_winner(chicago_bulls, la_lakers)
    print_scores(chicago_bulls, la_lakers)

main()