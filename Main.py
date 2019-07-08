from player import Player, list_of_players
from team import Team, list_of_teams
from match import Match, list_of_matches
from tournament import Tournament
import random

names = ["Lenny Gabbert","Thurman Clermont","Aurelio Arp","Jackson Tomas","William Hartness","Kristopher Yadao",
          "Garfield Star","Kris Robinette","Grant Mccurley","Connie Turney","Bradly Sadowski","Shannon Lindgren",
          "Johnie Raffaele","Miquel Goodin","Young Gallivan","Jim Mastroianni","Ellis Blocher","Dorian Lanoue",
          "Isiah Kornfeld","Aaron Deines","Reed Sturm","Elwood Lindholm","Garrett Burley","Ulysses Galan","Williams Haltom",
          "Ahmed Melito","Merle Berk","Marion Goodpasture","Gregory Villalvazo","Donny Geisel","Russel Ronald","Loyd Kluck",
          "Rigoberto Millar","Francisco Chaplin","Vincent Kendra","Wesley Clinard","Victor Heflin","Joey Bourassa","Abel Penta",
          "Desmond Blum","Rodger Mccleary","Sanford Moscoso","Brant Colligan","Marco Durkee","Jeremiah Madril","Santo Waugh",
          "Beau Schwein","Glen Louviere","Edwardo Mango","Jayson Drennen"]

def create_list_players(num_players):
    players = []
    for i in range(num_players):
        players.append(Player(random.choice(names),random.randint(16,42),random.randint(68,94)))
        list_of_players.append(players[i])
    return players

def create_team(name):
    return Team(name)

def add_players_team(players, Team):
    for player in players:
        Team.players.append(player)

barcelona = create_team('Barcelona')
list_of_teams.append(barcelona)
add_players_team(create_list_players(11), barcelona)
barcelona.calculate_average_overall()

realmadrid = create_team('Real Madrid')
list_of_teams.append(realmadrid)
add_players_team(create_list_players(11), realmadrid)
realmadrid.calculate_average_overall()

juventus = create_team('Juventus')
list_of_teams.append(realmadrid)
add_players_team(create_list_players(11), juventus)
juventus.calculate_average_overall()

atl_madrid = create_team('Atletico Madrid')
list_of_teams.append(realmadrid)
add_players_team(create_list_players(11), atl_madrid)
atl_madrid.calculate_average_overall()

milan = create_team('Milan')
list_of_teams.append(realmadrid)
add_players_team(create_list_players(11), milan)
milan.calculate_average_overall()

inter = create_team('Inter')
list_of_teams.append(realmadrid)
add_players_team(create_list_players(11), inter)
inter.calculate_average_overall()

torneio = Tournament([milan, realmadrid, barcelona, inter, juventus, atl_madrid])
torneio.create_games()
torneio.simulate_games()
torneio.assign_points()


while True:
    print("Menu")
    print("1-Criar lista jogadores para um time")
    print("2-Criar um time")
    print("3-Simular Partida")
    comando = input()
    if comando == '1':
        nome_time = input("Digite o nome do time que deseja adicionar jogadores")
        for time in list_of_teams:
            if time.name == nome_time:
                qtd_jogadores = int(input("Digite a quantidade de jogadores que deseja adicionar ao time"))
                lista_jogadores = create_list_players(qtd_jogadores)
                add_players_team(list_of_players, time)
                break
        else:
            print("Time não encontrado")
    if comando == '2':
        nome_time = input("Digite o nome do time a ser criado")
        list_of_teams.append(Team(nome_time))
    if comando == '3':
        nome_time1 = input("Digite o nome do time mandante")
        nome_time2 = input("Digite o nome do time visitante")
        for time in list_of_teams:
            if time.name == nome_time1:
                time1 = time
                time1.calculate_average_overall()
            elif time.name == nome_time2:
                time2 = time
                time2.calculate_average_overall()
        else:
            print("Time não encontrado")

        partida = Match(time1, time2)
        list_of_matches.append(partida)
        partida.simulate_game()


















'''


partida = Match(barcelona, realmadrid)
partida.calculate_match_win_odd()
partida.simulate_game()
partida.determine_match_winner()
partida.print()
partida.print_goals()
'''