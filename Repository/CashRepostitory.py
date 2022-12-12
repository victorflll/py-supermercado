from Utils.JsonManager import JsonManager, update_json, open_json


class CashRepository:

    def __init__(self):
        self._jsonClientPath = "/Data/ClientData.json"
        self._jsonProductsPath = "/Data/ProductData.json"
        self._jsonPath = "/Data/CashRegister.json"
        self._jsonManager = JsonManager()

    def sale(self, cash: float):
        value: float = open_json(self._jsonPath, {"money": 0.0})

        new_value = value["money"] + cash
        data = {"money": new_value}
        update_json(self._jsonPath, data)

    def get_product(self, product_id: int):
        products = open_json(self._jsonProductsPath)
        for product in products:
            if product['id'] == product_id:
                return product
        raise ValueError("Produto não encontrado.")

    def update_product(self, product_id: int, quantity: int):
        product = self.get_product(product_id)

        new_quantity = product['quantity']-quantity

        try:
            products = open_json(self._jsonProductsPath)
            for item in products:
                if item['id'] == product['id']:
                    item['name'] = product['name']
                    item['value'] = product['value']
                    item['quantity'] = new_quantity
                    update_json(self._jsonProductsPath, products)
                    return "Produto atualizado com sucesso."
            raise ValueError("Produto não encontrado.")

        except ValueError as err:
            print(err)

    def get_client(self, cpf: int):
        clients = open_json(self._jsonClientPath)
        for client in clients:
            if client['CPF'] == cpf:
                return client
        raise ValueError("Cliente não encontrado.")

    def apply_rebate(self, cpf: int, rebate: float):
        clients = open_json(self._jsonClientPath)
        for item in clients:
            if item['CPF'] == cpf:
                item["rebate"] = rebate
                update_json(self._jsonClientPath, clients)
                print("Desconto para o cliente atualizado com sucesso.")

    def money(self):
        return open_json(self._jsonPath, {"money": 0.0})
