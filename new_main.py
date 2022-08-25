import csv

class Item(): #create a new class
    pay_rate = 0.8 #class attribute for payrate after 20% discount
    all = [] #empty list to hold all instances created
    def __init__(self, name: str, price: float, quantity = 0):
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is negative"
        assert quantity >= 0, f"Quantity {quantity} is negative"


        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self) #append all items in one list

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


    # read in data. 
    # convert this method to a class method by using a decorator
    @classmethod #to manipulate different structures of data to instantiate objects, e.g. csv, json
    def instantiate_from_csv(cls): #class object passed as the first argument instead of self
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity= int(item.get('quantity'))
            )
    
    @staticmethod #used on something that should not be unique per instance
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            False

    def __repr__(self): #represent all our instances
        return f"Item('{self.name}', {self.price}, {self.quantity})"


class Phone(Item): #Child class that inherits from parent class 
    pass

phone1 = Item("phone10", 400, 5)
phone1.broken_phones = 1
phone2 = Item("phone20", 500, 7)
phone2.broken_phones = 1



