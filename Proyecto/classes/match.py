class Match():
    def __init__(self, home_team, away_team, date, stadium, id, sold_tickets, used_tickets):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.stadium = stadium
        self.id = id
        self.sold_tickets = sold_tickets
        self.used_tickets = used_tickets
    
    def show(self, teams):
        print("Local Team: ")
        for team in teams:
            if self.home_team == team.name:
                team.show()
        print("Local Team: ")
        for team in teams:
            if self.away_team == team.name:
                team.show()
        print(f'''Date and Time: {self.date}
Stadium id: {self.stadium}
Match id: {self.id}''')