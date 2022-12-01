def validate_ticket(matches):
    match_id = input("Please enter the match id: ")
    for match in matches:
        if match_id == match.id:
            ticket_id = input("Please enter the ticket id: ")
            found = False
            for ticket in match.sold_tickets: 
                if ticket.id == ticket_id:
                    found = True
                    match.sold_tickets.remove(ticket)
                    match.used_tickets.append(ticket)
            if not found:
                for ticket in match.used_tickets: 
                    if ticket.id == ticket_id:
                        found = True
                        print("The ticket has already been used.")
            if not found:
                print("The ticket id does not match to any of the tickets registered in the system.")
    else:
        print("Match not found.")