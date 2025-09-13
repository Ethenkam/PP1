from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, stock=0, broken_phones=0):
        super().__init__(
            name, price, stock
        )
        # Validate the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

        self.broken_phones = broken_phones