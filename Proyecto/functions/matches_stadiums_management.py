from classes.team import Team
from classes.stadium import Stadium
from classes.match import Match
from classes.product import *
from functions.restaurant_management import *

def register_teams(teams_edd):
    teams = []
    for team in teams_edd:
        name = team["name"]
        flag = team["flag"]
        fifa_code = team["fifa_code"]
        group = team["group"]
        id = team["id"]
        teams.append(Team(name,flag,fifa_code,group,id))
    return teams

def generate_stadium_rows(capacity):
    stadium_map = []
    general_rows_amount = capacity[0]/10
    vip_rows_amount = capacity[1]/10
    seat = "___"
    row = []
    while len(row)<10:
        row.append(seat)
    vip_rows = []
    general_rows = []
    while len(vip_rows)<vip_rows_amount:
        vip_rows.append(row)
    stadium_map.append(vip_rows)
    while len(general_rows)<general_rows_amount:
        general_rows.append(row)
    stadium_map.append(general_rows)
    return stadium_map

def register_stadiums(stadiums_edd):
    stadiums = []
    for stadium in stadiums_edd:
        id = stadium["id"]
        name = stadium["name"]
        capacity = stadium["capacity"]
        location = stadium["location"]
        restaurants = register_restaurants(stadium["restaurants"])
        stadium_map = generate_stadium_rows(capacity)
        stadiums.append(Stadium(id,name,capacity,location,restaurants,stadium_map))
    return stadiums

def register_matches(matches_edd):
    matches = []
    for match in matches_edd:
        home_team = match["home_team"]
        away_team = match["away_team"]
        date = match["date"]
        stadium = match["stadium_id"]
        id = match["id"]
        sold_tickets = []
        used_tickets = []
        matches.append(Match(home_team,away_team,date,stadium,id,sold_tickets, used_tickets))
    return matches

def search_filter_stadium(matches):
    option = input("Search by:\n1. Country\n2. Stadium\n3. Date\n->")
    if option.isnumeric():
        option = int(option)
        if option == 1:
            search_country_matches(matches)
        elif option == 2: 
            search_stadium_matches(matches)
        elif option == 3:
            search_date_matches(matches)
    print("Please enter a valid value.")
    return search_filter_stadium()

def search_country_matches(matches):
    country = input("Please enter the country's name: ")
    if country.isalpha():
        country = country.upper()
        for match in matches:
            if match.home_team == country:
                match.show()
            if match.away_team == country:
                match.show()
            else:
                print (f"There are no matches available for {country}")
    print("Please enter a valid country name.")
    return search_country_matches(matches)

def search_stadium_matches(matches):
    stadium = input("Please enter the stadium id: ")
    for match in matches:
        if match.stadium == stadium:
            match.show()
        else:
            print (f"There are no matches available for stadium with id {stadium}")

def search_date_matches(matches):
    date = input("Please enter the specific date: ")
    for match in matches:
        if date in match.date:
            match.show()
        else:
            print (f"There are no matches available for the date: {date}")