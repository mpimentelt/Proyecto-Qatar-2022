import itertools
from classes.ticket import *

def show_matches(matches):
    print("*********** MATCHES ***********")
    for match in matches:
        match.show()
        print("====================================================================")

def get_fangs(number):
    number = str(number)
    num_combinations = itertools.permutations(number, len(number))
    for num_list in num_combinations:
        v = ''.join(num_list)
        x, y = v[:int(len(v)/2)], v[int(len(v)/2):]
        if x[-1] == '0' and y[-1] == '0':
            continue
        if int(x) * int(y) == int(number):
            return x,y
        continue
    return False

def is_vampire(number):
    if len(str(number)) % 2 == 1:
        return False
    fangs = get_fangs(number)
    if not fangs:
        return False
    return True

def get_discount(ci, price):
    discount = 0
    if is_vampire(ci):
        discount += price*0.5
    return discount

def print_tentative(ticket, ci):
    discount = get_discount(ci, ticket.price)
    iva = ticket.price*0.16
    print("Seat: ", ticket.seat)
    print(f'''{ticket.type}: {ticket.price} $''')
    print("IVA: ", iva)
    if discount != 0:
        print("You have a 50% discount.")
        print("Discount: ", discount)
    print("Total: ", ticket.price - discount + iva)
    return ticket.price - discount + iva

def take_seat(ticket,stadiums):
    if ticket.type == "VIP":
        for stadium in stadiums:
            if ticket.stadium == stadium.id:
                stadium.stadium_map[0][ticket.seat[0]][ticket.seat[1]] = "_x_"
    else:
        for stadium in stadiums:
            if ticket.stadium == stadium.id:
                stadium.stadium_map[1][ticket.seat[0]][ticket.seat[1]] = "_x_"
    return stadiums

def get_ticket(matches,stadiums,ci):
    seat = []
    match_id = input("Please enter the id of the match you'd like to assist to: ")
    while not match_id.isnumeric():
        match_id = input("Please enter the id of the match you'd like to assist to: ")
    ticket_option = input("Please enter the type of ticket you would like to buy:\nG - General\nV - VIP\n->").upper()
    while not ticket_option == "G" or ticket_option == "V":
        ticket_option = input("Invalid input. Please enter the type of ticket you would like to buy:\nG - General\nV - VIP\n->").upper()
    while True:
        for match in matches:
            if match_id == match.id:
                match_ticket = match_ticket
                for stadium in stadiums:
                    if match.stadium == stadium.id:
                        stadium.show_stadium_map()
                        stadium_ticket = stadium
        row_num = input("Enter the number of the number of the row you wish to purchase: ")
        while not row_num.isnumeric():
            row_num = input("Invalid input. Enter the number of the number of the row you wish to purchase: ")
        seat_num = input("Enter the number of the seat you wish to purchase: ")
        while not seat_num.isnumeric():
            seat_num = input("Invalid input. Enter the number of the seat you wish to purchase: ")
        if ticket_option == "V":
            if len(stadium.stadium_map[0])>=row_num:
                if seat_num<=10:
                    seat.append(row_num)
                    seat.append(seat_num)
            if stadium.stadium_map[0][row_num-1][seat_num-1] == "_x_":
                print("This seat is already taken. Please choose another one.")
                continue
            else:
                ticket = TVip(match_id,stadium_ticket.id,seat,len(match_ticket.sold_tickets))
                total = print_tentative(ticket)
                if input("Would you like to confirm your purchase? Y-yes or Other-no: ").upper() == "Y":
                    stadiums = take_seat(ticket,stadiums)
                    return ticket,stadiums,total
                else:
                    break
        if ticket_option == "G":
            if len(stadium.stadium_map[1])>=row_num:
                if seat_num<=10:
                    seat.append(row_num)
                    seat.append(seat_num)
            if stadium.stadium_map[1][row_num-1][seat_num-1] == "_x_":
                print("This seat is already taken. Please choose another one.")
                continue
            else:
                ticket = TGeneral(match_id,stadium_ticket.id,seat,len(match_ticket.sold_tickets))
                total = print_tentative(ticket)
                if input("Would you like to confirm your purchase? Y-yes or Other-no: ").upper() == "Y":
                    stadiums = take_seat(ticket,stadiums)
                    return ticket,stadiums,total
                else:
                    break   
    
def get_client(matches,stadiums, vip_clients, general_clients):
    tickets = []
    name = input("Please enter your name: ")
    while not name.isalpha():
        name = input("Invalid input. Please enter your name: ")
    id = input("Please enter your id: ")
    while not id.isnumeric():
        id = input("Invalid input. Please enter your id: ")
    age = input("Please enter your age: ")
    while not age.isnumeric():
        age = input("Invalid input. Please enter your age: ")
    while True:
        ticket,stadiums,total = get_ticket(matches,stadiums)
        tickets.append(ticket)
        for match in matches:
            if match.id == ticket.match:
                match.sold_tickets.append(ticket)
        if input("Would you like to buy another ticket? N-no or Other-Yes").upper() == "N":
            break
    for ticket in tickets:
        if ticket.type == "General":
            client = CGeneral(name, id, age, tickets, total)
            general_clients.append(client)
        else:
            client = CVip(name, id, age, tickets, total)
            vip_clients.append(client)
    return matches, stadiums, vip_clients, general_clients