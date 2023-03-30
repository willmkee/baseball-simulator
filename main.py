import csv
import random

from Player import Player


def load_players(fileName, team):  # Method to load players into Hash Table
    # Opens csv file
    with open(fileName) as players:
        player_data = csv.reader(players, delimiter=',')
        next(player_data)
        # Iterates through each row in csv file and assigns player variables
        for row in player_data:
            name = row[0]
            games = int(row[1])
            plate_appearances = int(row[2])
            homeruns = int(row[3])
            walks = float(row[4])
            strikeouts = float(row[5])
            batting_avg = float(row[6])
            obp = float(row[7])
            slugging = float(row[8])
            player_id = int(row[9])

            # Creates new player object
            p = Player(player_id, name, games, plate_appearances, homeruns, walks, strikeouts, batting_avg, obp, slugging)
            team.append(p)

def probably(chance):
    return random.random() < chance

def play_inning(team):
    outs = 0
    at_bat = team
    current_batter = 0
    on_base = 0
    team_score = 0
    while outs < 3:
        if probably(at_bat[current_batter].batting_avg):
            print("%s got a hit!!!" % at_bat[current_batter].name)
            if current_batter < 8:
                current_batter += 1
            else:
                current_batter = 0
            on_base += 1
            if on_base > 3:
                team_score += on_base - 3
                print("Run Scored!!!")
                on_base = on_base - 1
        elif probably(at_bat[current_batter].walks):
            print("%s walks to first." % at_bat[current_batter].name)
            if current_batter < 8:
                current_batter += 1
            else:
                current_batter = 0
            on_base += 1
            if on_base > 3:
                team_score += on_base - 3
                print("Run Scored!!!")
                on_base = on_base - 1
        else:
            print("%s struck out!" % at_bat[current_batter].name)
            if current_batter < 8:
                current_batter += 1
            else:
                current_batter = 0
            outs += 1
    print("Inning over")
    return team_score
def gameplay(home_team, away_team):
    home_score = 0
    away_score = 0
    inning = 1

    while inning < 19:
        if inning % 2 != 0:
            away_score += play_inning(away_team)
            inning += 1
        elif inning % 2 == 0:
            home_score += play_inning(home_team)
            inning += 1
    print("Ballgame!")
    print("Home: %s, Away: %s" % (home_score, away_score))

    

    


home_team = []
away_team = []

load_players("Braves.csv", home_team)
load_players("phillies.csv", away_team)

gameplay(home_team, away_team)

