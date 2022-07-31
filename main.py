import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
       self.price = self.price * self.quantity * self.pay_rate

    @classmethod # Decorator to change the behavior of the instance and create class method below
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'), 
                price = float(item.get('price')), 
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        """count out floats that are point zero"""
        if isinstance(num, float):
            #count out floats that are point zero
            return num.is_integer
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


print(Item.is_integer(7.1))


