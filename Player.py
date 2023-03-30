class Player:
    def __init__(self, player_id, name, games, plate_appearances, homeruns, walks, strikeouts, batting_avg, obp, slugging):
        self.slugging = slugging
        self.obp = obp
        self.batting_avg = batting_avg
        self.strikeouts = strikeouts
        self.walks = walks
        self.homeruns = homeruns
        self.plate_appearances = plate_appearances
        self.games = games
        self.name = name
        self.player_id = player_id

    def __str__(self):
        return "Name: %s, Batting Average: %s" % (self.name, self.batting_avg)