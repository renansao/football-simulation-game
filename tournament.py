from match import Match, list_of_matches
from team import Team, list_of_teams

class Tournament:

    def __init__(self, teams):
        self.teams = teams
        self.points = [0,0,0,0,0,0]
        self.list_matches_tournament = []


    def create_games(self):
        for team in self.teams:
            for team2 in self.teams:
                if team != team2:
                    self.list_matches_tournament.append(Match(team, team2))

    def simulate_games(self):
        for partida in self.list_matches_tournament:
            partida.simulate_game()

    def assign_points(self):
        for partida in self.list_matches_tournament:
            if partida.match_winner == 'Draw':
                partida.team1.points += 1
                partida.team2.points += 1
            elif partida.match_winner == partida.team1.name:
                partida.team1.points += 3
            elif partida.match_winner == partida.team2.name:
                partida.team2.points += 3


    def simulate_tournament(self):
        self.create_games()
        self.simulate_games()
        self.assign_points()