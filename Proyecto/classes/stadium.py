class Stadium():
    def __init__(self, id, name, capacity, location, restaurants, stadium_map):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.location = location
        self.restaurants = restaurants
        self.stadium_map = stadium_map

    def show_stadium_map(self): 
        print("**************** FIELD ****************")
        print("=======================================")
        print("************** VIP ZONE ***************")
        print("Row number")
        n = 0
        for row in self.stadium_map[0]:
            n += 1
            print(n)
            for seat in row:
                print(seat,end=".")
            print("\n")
        print("************ GENERAL ZONE *************")
        n=0
        for row in self.stadium_map[1]:
            n+=1
            print(n)
            for seat in row:
                print(seat,end=".")
            print("\n")
        print(" 1   2   3   4   5   6   7   8   9   10  (seat number)")
    
    def check_seat(self, seat):
        pass