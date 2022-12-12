from Handlers.CashHandler import CashHandler


class CashOptions:
    def __init__(self):
        self._cashHandler = CashHandler()
        self._options()

    def _options(self):
        print("1 - Iniciar venda\n"
              "2 - Exibir dinheiro\n"
              "3 - Dar desconto")
        choice = int(input())

        match choice:
            case 1:
                self._cashHandler.start_sale()
            case 2:
                self._cashHandler.money()
            case 3:
                self._cashHandler.apply_rebate()
