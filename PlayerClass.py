class Player:
## constructor
    def __init__(self,name):
        ## class members
        self.name = name
        self.points_total = 0
        self.points_castle = 0
        self.points_farmer = 0
        self.points_farmer_house = 0
        self.points_shepherd = 0
        self.points_highwayman = 0
        self.points_cloister = 0
        self.points_goodies = 0
        self.points_market = 0
        self.points_ransom = 0
        self.time_steps = [0.00]
        self.points_total_array = [0]
        self.points_castle_array = [0]
        self.points_farmer_array = [0]
        self.points_farmer_house_array = [0]
        self.points_shepherd_array = [0]
        self.points_highwayman_array = [0]
        self.points_cloister_array = [0]
        self.points_goodies_array = [0]
        self.points_market_array = [0]
        self.points_ransom_array = [0]
        print('hi', name, 'you are sucessfully registered!')

##  set functions
    def add_points_castle(self,points):
        self.points_castle = points + self.points_castle
    def add_points_farmer(self,points):
        self.points_farmer = points + self.points_farmer
    def add_points_farmer_house(self,points):
        self.points_farmer_house = points + self.points_farmer_house
    def add_points_shepherd(self,points):
        self.points_shepherd = points + self.points_shepherd
    def add_points_highwayman(self,points):
        self.points_highwayman = points + self.points_highwayman
    def add_points_cloister(self,points):
        self.points_cloister = points + self.points_cloister
    def add_points_market(self,points):
        self.points_market = points + self.points_market
    def add_points_ransom(self,points):
        self.points_ransom = points + self.points_ransom
    def add_points_goodies(self,points):
        self.points_goodies = points + self.points_goodies
    def set_points_total(self,points):
        self.points_total = points

## custom functions
    def add_up_all_points(self):
        points = self.points_castle+self.points_farmer+self.points_farmer_house+self.points_shepherd+\
        self.points_highwayman+self.points_cloister+self.points_goodies+self.points_market+self.points_ransom

        self.set_points_total(points)

    def return_player_stats(self):
        return(self.name +  ': ' + str(self.points_total))

    def update_points(self,point_category,points):
        check = 0
        if (point_category == 'a'):
            self.add_points_castle(points)
        elif (point_category == 'b'):
            self.add_points_farmer(points)
        elif (point_category == 'c'):
            self.add_points_farmer_house(points)
        elif (point_category == 'd'):
            self.add_points_shepherd(points)
        elif (point_category == 'e'):
            self.add_points_highwayman(points)
        elif (point_category == 'f'):
            self.add_points_cloister(points)
        elif (point_category == 'g'):
            self.add_points_goodies(points)
        elif (point_category == 'h'):
            self.add_points_market(points)
        elif (point_category == 'i'):
            self.add_points_ransom(points)
        else:
            print('unknown category')
            check = 1
        return check
                        
    def update_class_arrays(self,time):
        self.time_steps.append(time)
        self.points_total_array.append(self.points_total)
        self.points_castle_array.append(self.points_castle)
        self.points_farmer_array.append(self.points_farmer)
        self.points_farmer_house_array.append(self.points_farmer_house)
        self.points_shepherd_array.append(self.points_shepherd)
        self.points_highwayman_array.append(self.points_highwayman)
        self.points_cloister_array.append(self.points_cloister)
        self.points_goodies_array.append(self.points_goodies)
        self.points_market_array.append(self.points_market)
        self.points_ransom_array.append(self.points_ransom)

            