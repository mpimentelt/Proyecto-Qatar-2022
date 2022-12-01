class Ticket():
    def __init__(self, match, stadium, seat, id):
        self.match = match
        self.stadium = stadium
        self.seat = seat
        self.id = id
    def show(self):
        print(f'''Match id: {self.match}
Stadium id: {self.stadium}
Seat: {self.seat}
Id: {self.id}''')

class TGeneral(Ticket):
    def __init__(self, match, stadium, seat, id):
        super().__init__(match, stadium, seat, id)
        self.ticket_type = "General"
        self.price = 50
    def show(self):
        print(f'''Match id: {self.match}
Stadium id: {self.stadium}
Seat: {self.seat}
Id: {self.id}
Price: {self.price}
Ticket type: {self.ticket_type}''')

class TVIP(Ticket):
    def __init__(self, match, stadium, seat, id):
        super().__init__(match, stadium, seat, id)
        self.ticket_type = "VIP"
        self.price = 120
    def show(self):
        print(f'''Match id: {self.match}
Stadium id: {self.stadium}
Seat: {self.seat}
Id: {self.id}
Price: {self.price}
Ticket type: {self.ticket_type}''')