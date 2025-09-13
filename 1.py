class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, stock=0):
        # Validate the received arguments
        assert price > 0, f"Price {price} is not greater than zero!"
        assert stock >= 0, f"Stock {stock} is not greater than or equal to zero!"
        # Pass values
        self.name = name
        self.price = price
        self.stock = stock
        # Actions to execute
        Item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.stock

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def initiate_from_csv(cls, path):
        import csv
        with open(path, 'r') as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                stock=int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.stock})"
print(Item.is_integer(1.0))
Item.initiate_from_csv('1.csv')
print(Item.all)