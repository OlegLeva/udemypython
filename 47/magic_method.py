class Chain:
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return 'Chain with ' + str(self.number_of_items) + ' items'

    def __len__(self):
        return self.number_of_items


item = Chain(3)
print(item)
print(len(item))
