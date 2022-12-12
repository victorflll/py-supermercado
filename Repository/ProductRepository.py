from Domain.Product import Product
from Utils.JsonManager import JsonManager, open_json, update_json


class ProductRepository:

    def __init__(self):
        self._jsonPath = "/Data/ProductData.json"
        self._reportPath = "/Data/Report.json"
        self._jsonManager = JsonManager()

    def save(self, product: Product):
        products = open_json(self._jsonPath)
        products.append({"id": product.get_id(),
                         "name": product.get_name(),
                         "value": product.get_value(),
                         "quantity": product.get_quantity()})
        update_json(self._jsonPath, products)

        print("Produto cadastrado com sucesso.")

    def products(self):
        products = open_json(self._jsonPath)
        return products

    def product(self, product_id: int):
        products = open_json(self._jsonPath)
        for product in products:
            if product["id"] == product_id:
                return product
        raise ValueError("Produto não encontrado.")

    def update(self, product: Product):
        products = open_json(self._jsonPath)
        for item in products:
            if item["id"] == product.get_id():
                item["name"] = product.get_name()
                item["value"] = product.get_value()
                item["quantity"] = product.get_quantity()
                update_json(self._jsonPath, products)
                return "Produto atualizado com sucesso."
        raise ValueError("Produto não encontrado.")

    def delete(self, product_id: int):
        products = open_json(self._jsonPath)
        for index in range(len(products)):
            if products[index]["id"] == product_id:
                products.pop(index)
                update_json(self._jsonPath, products)
                return "Produto deletado com sucesso."
        raise ValueError("Produto não encontrado.")

