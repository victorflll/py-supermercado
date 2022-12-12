class Product:

    def __init__(self, product_id: int, name: str, value: float, quantity: int):
        self._product_id = product_id
        self._name = name
        self._value = value
        self._quantity = quantity

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> int:
        return self._product_id

    def get_value(self) -> float:
        return self._value

    def get_quantity(self) -> int:
        return self._quantity
