class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print(f'Ресторан {self.restaurant_name} открыт')

    def set_number_served(self, count):
        self.number_served = count

    def increment_number_served(self, counter):
        self.number_served += counter



sushied = Restaurant('SUHIED', 'Japanese')
kofan = Restaurant('KOFAN', 'evropean')
obama = Restaurant('OBAMA BURGER', 'american')
sushied.set_number_served(5)
sushied.increment_number_served(6)
print(sushied.number_served)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def list_ice_cream(self):
        print(self.flavors)

rojok = IceCreamStand('Ice Delight', 'sweet', ['vaflya', 'strambery', 'chokolate'])
print(rojok.flavors[1])
rojok.list_ice_cream()
