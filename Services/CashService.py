from Repository.CashRepostitory import CashRepository


class CashService:

    def __init__(self):
        self._cashRepository = CashRepository()

    def sale(self, cash: float):
        return self._cashRepository.sale(cash)

    def get_product(self, product_id: int):
        return self._cashRepository.get_product(product_id)

    def update_product(self, product_id: int, quantity: int):
        return self._cashRepository.update_product(product_id, quantity)

    def get_client(self, cpf: int):
        return self._cashRepository.get_client(cpf)

    def apply_rebate(self, cpf: int, rebate: float):
        return self._cashRepository.apply_rebate(cpf, rebate)

    def money(self):
        return self._cashRepository.money()
