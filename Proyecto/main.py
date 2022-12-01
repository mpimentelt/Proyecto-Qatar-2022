import requests
import json
from functions.matches_stadiums_management import *
from functions.match_security_check import *
from functions.restaurant_management import *
from functions.restaurants_sales import *
from functions.statistics import *
from functions.ticketing import *

def print_welcome():
    print("******* WELCOME *******")

def print_thanks():
    print("Thank you for your visit")

def get_option():
    option = input("Please enter a valid option: 1. Buy ticket\n2. Search matches by filter \n3. Buy product at a restaurant\n4. Validate a Ticket\n5. View statistics\n6. Exit\n->")
    while not option.isnumeric():
        option = input("Please enter a valid option: 1. Buy ticket\n2. Search matches by filter \n3. Buy product at a restaurant\n4. Validate a Ticket\n5. View statistics\n6. Exit\n->")
    else:
        return int(option)

def save_data(stadiums,matches,vip_clients,general_clients):
    with open("stadium.json", "w") as w:
        s = json.dumps(stadiums)
        w.write(s)
        w.close()
    with open("matches.json", "w") as w:
        m = json.dumps(matches)
        w.write(m)
        w.close()
    with open("clients.json", "w") as w:
        vip = json.dumps(vip_clients)
        gen = json.dumps(general_clients)
        w.write(vip,gen)
        w.close()
    
def main(): 
    stadiums_edd = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json").json()
    matches_edd = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json").json()
    teams_edd = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json").json()
    stadiums = register_stadiums(stadiums_edd)
    matches = register_matches(matches_edd)
    teams = register_teams(teams_edd)
    general_clients = []
    vip_clients = []

    print_welcome()
    while True:
        option = get_option()
        if option == 1:
            show_matches()
            matches, stadiums, vip_clients, general_clients = get_client(matches,stadiums, vip_clients, general_clients)
        elif option == 2:
            search_filter_stadium(matches)
        elif option == 3:
            stadiums, vip_clients = buy_product(stadiums, vip_clients)
        elif option == 4:
            validate_ticket(matches)
        elif option == 5:
            vip_average_consumption(vip_clients)
            match_assistance(matches)
            match_sold_tickets(matches)
            sold_product(stadiums)
            top_clients(general_clients,vip_clients)
        elif option == 6:
            break
        else:
            continue
    
    print_thanks()

    save_data(stadiums,matches,teams,vip_clients,general_clients)

main()
