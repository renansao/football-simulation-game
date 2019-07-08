global list_of_teams
list_of_teams = []

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.avg_overall = 0
        self.points = 0

    def calculate_average_overall(self):
        for player in self.players:
            self.avg_overall += player.overall
        self.avg_overall = self.avg_overall / len(self.players)

    def print(self):
        print('Time: ', self.name)
        for player in self.players:
            print(player.name,' ,' ,player.age,', Overall - ', player.overall)
            print()
        print('Team Overall: ', self.avg_overall)

