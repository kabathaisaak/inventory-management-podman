class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = float(price)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }