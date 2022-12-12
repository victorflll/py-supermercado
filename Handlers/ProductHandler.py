from Domain.Product import Product
from Services.ProductService import ProductService


class ProductHandler:
    def __init__(self):
        self._product_service = ProductService()

    def save(self):
        product_id = int(input("Digite o código do produto: "))
        name = input("Digite o nome do produto: ")
        value = float(input("Digite o preço do produto: "))
        quantity = int(input("Digita a quantidade de produtos: "))

        product = Product(product_id, name, value, quantity)

        self._product_service.save(product)

    def products(self):
        products = self._product_service.products()
        if products:
            for product in products:
                print("Id: {}\n"
                      "Produto: {}\n"
                      "Preço: {}\n"
                      "Quantidade: {}"
                      .format(product["id"], product["name"], product["value"], product["quantity"]))
        elif not products:
            print("Nenhum dado encontrado.")

    def product(self):
        product_id = int(input("Digite o código do produto: "))
        try:
            product = self._product_service.product(product_id)
            print("Id: {}\n"
                  "Produto: {}\n"
                  "Preço: {}\n"
                  "Quantidade: {}"
                  .format(product["id"], product["name"], product["value"], product["quantity"]))
        except ValueError as err:
            print(err)

    def update(self):
        product_id = int(input("Digite o código do produto: "))
        name = input("Digite o nome do produto: ")
        value = float(input("Digite o preço do produto: "))
        quantity = int(input("Digita a quantidade de produtos: "))

        product = Product(product_id, name, value, quantity)

        try:
            print(self._product_service.update(product))
        except ValueError as err:
            print(err)

    def delete(self):
        product_id = int(input("Digite o código do produto: "))

        try:
            print(self._product_service.delete(product_id))
        except ValueError as err:
            print(err)

    def product_to_sale(self, product_id: int):
        product = self._product_service.product(product_id)
        return product
