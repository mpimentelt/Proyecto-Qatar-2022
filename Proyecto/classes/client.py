class Client():
    def __init__(self, name, id, age, tickets):
        self.name = name
        self.id = id
        self.age = age
        self.tickets = tickets

    def show(self):
        print(f'''Name: {self.name}
Id: {self.id}
Age: {self.age}
Tickets: ''')
        for ticket in self.tickets:
            ticket.show()

class CGeneral(Client):
    def __init__(self, name, id, age, tickets, total):
        super().__init__(name, id, age, tickets)
        self.total = total
    def show(self):
        print(f'''Name: {self.name}
Id: {self.id}
Age: {self.age}
Tickets: ''')
        for ticket in self.tickets:
            ticket.show()

class CVip(Client):
    def __init__(self, name, id, age, tickets, consumption):
        super().__init__(name, id, age, tickets)
        self.consumption = consumption
    def show(self):
        print(f'''Name: {self.name}
Id: {self.id}
Age: {self.age}
Tickets: ''')
        for ticket in self.tickets:
            ticket.show()