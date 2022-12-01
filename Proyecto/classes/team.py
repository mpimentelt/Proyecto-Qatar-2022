class Team():
    def __init__(self, name, flag, fifa_code, group, id):
        self.name = name
        self.flag = flag
        self.fifa_code = fifa_code
        self.group = group
        self.id = id
    
    def show(self):
        print(f'''Name: {self.name}
Flag: {self.flag}
Team FIFA Code: {self.fifa_code}
Team Group: {self.group}
Team id: {self.id}''')