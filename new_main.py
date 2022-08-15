
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

    





item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


for instance in Item.all:
    print(instance.quantity)
