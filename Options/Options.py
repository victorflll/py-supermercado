from Options.ClientOptions import ClientOptions
from Options.ProductOptions import ProductOptions
from Options.CashOptions import CashOptions


def _loop():
    while True:
        print("1 - Cliente\n"
              "2 - Produtos\n"
              "3 - Caixa\n"
              "0 - Sair")
        choice = int(input())

        match choice:
            case 0:
                break
            case 1:
                ClientOptions()
            case 2:
                ProductOptions()
            case 3:
                CashOptions()


class Options:
    def __init__(self):
        _loop()
