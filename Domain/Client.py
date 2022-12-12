class Client:
    def __init__(self, cpf: int, name):
        self._cpf = cpf
        self._name = name
        self._rebate: float = 0

    def get_name(self):
        return self._name

    def get_cpf(self):
        return self._cpf

    def get_rebate(self):
        return self._rebate

    def set_rebate(self, rebate: float):
        self._rebate = rebate
