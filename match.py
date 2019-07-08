from team import Team
import time
import random

global list_of_matches
list_of_matches = []

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score = [0,0]
        self.time = 0
        self.match_win_odd = [0,0]
        self.match_winner = ''
        self.goals_scored = [[],[]]

    def calculate_match_win_odd(self):
        diff = self.team1.avg_overall - self.team2.avg_overall
        #print(self.team1.avg_overall, self.team2.avg_overall)
        self.match_win_odd[0] = 50 + diff
        self.match_win_odd[1] = 100 - self.match_win_odd[0]
        self.match_win_odd[0] = float(format(self.match_win_odd[0], '.2f'))
        self.match_win_odd[1] = float(format(self.match_win_odd[1], '.2f'))

    def print_goals(self):
        if len(self.goals_scored[0]) > 0:
            print("Os gols do ", self.team1.name, ", foram marcados por:")
            for list in self.goals_scored[0]:
                print(list[0].name, list[1],"'")
        if len(self.goals_scored[1]) > 0:
            print("Os gols do ", self.team2.name, ", foram marcados por:")
            for list in self.goals_scored[1]:
                print(list[0].name, list[1], "'")






    def print(self):
        if self.match_winner == 'Draw':
            print("A partida terminou empatada!")
        else:
            print("O vencedor da partida foi: ", self.match_winner)

    def assign_goal(self, Team):
        jogador = random.choice(Team.players)
        if Team == self.team1:
            self.goals_scored[0].append([jogador,self.time])
        else:
            self.goals_scored[1].append([jogador,self.time])
        return jogador.name


    def check_goal(self):
        goal = random.randint(1, 5000)
        if round(self.match_win_odd[0]) >= goal:
            self.score[0] += 1
            #print('GOOOOL!')
            self.assign_goal(self.team1)
        goal = random.randint(1, 5000)
        if round(self.match_win_odd[1]) >= goal:
            self.score[1] += 1
            #print('GOOOOL!')
            self.assign_goal(self.team2)

    def determine_match_winner(self):
        if self.score[0] > self.score[1]:
            self.match_winner = self.team1.name
        elif self.score[1] > self.score[0]:
            self.match_winner = self.team2.name
        else:
            self.match_winner = 'Draw'

    def simulate_game(self):
        self.calculate_match_win_odd()
        while self.time <= 90:
            #print(self.time,"'",end="")
            self.time +=1
            #print(" - ", self.team1.name," ",self.score[0] ," x ",self.score[1] ," ",self.team2.name)
            self.check_goal()
        print(self.team1.name," ",self.score[0] ," x ",self.score[1] ," ",self.team2.name)
        self.determine_match_winner()
        #self.print_goals()




'''
            clock = time.time()
            if clock_old + 1 < clock:
                clock_old += 1
                clock = time.time()
                
                            if self.time == 46:
                print("HALFTIME")
                time.sleep(2)
'''