class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        # list_by_letter = []
        # for product in self.products:
        #     if product[0] == first_letter:
        #         list_by_letter.append(product)
        # return list_by_letter
        return [product for product in self.products if product.startswith(first_letter)]


    def __repr__(self):
        self.products.sort()
        # result = f"Items in the {self.name} catalogue:"
        # for item in self.products:
        #     result += f"\n{item}"
        # return result
        returning_string = f"Items in the {self.name} catalogue:"
        returning_string += "\n".join(sorted(self.products))
        return returning_string



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)


