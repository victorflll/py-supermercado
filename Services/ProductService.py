from Domain.Product import Product
from Repository.ProductRepository import ProductRepository


class ProductService:
    def __init__(self):
        self._product_repository = ProductRepository()

    def save(self, product: Product):
        self._product_repository.save(product)

    def products(self):
        return self._product_repository.products()

    def product(self, product_id: int):
        return self._product_repository.product(product_id)

    def update(self, product: Product):
        return self._product_repository.update(product)

    def delete(self, product_id: int):
        return self._product_repository.delete(product_id)

    def product_to_sale(self, product_id: int):
        return self._product_repository.product(product_id)
