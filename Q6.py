class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def __str__(self):
        print(f"Name: {self.name} and Quantity: {self.quantity}")


class Inventory():
    def __init__(self, products: list):
        self.products = products

    def add_products(self, new_product):
        self.products.append(new_product)

    def __len__(self):
        return len(self.products)

    def __getitem__(self):
        return sorted(self.products)

    def search_by_name(self, name:str):
        for product in self.products:
            if name is product:
                return product
            else:
                return "Not Found"

