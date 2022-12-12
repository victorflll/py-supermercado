from Handlers.ProductHandler import ProductHandler


class ProductOptions:
    def __init__(self):
        self._product_handler = ProductHandler()

        self._options()

    def _options(self):
        print("1 - Criar Produto\n"
              "2 - Exibir Produtos\n"
              "3 - Buscar Produto\n"
              "4 - Atualizar Produto\n"
              "5 - Deletar Produto\n")
        choice = int(input())

        match choice:
            case 1:
                self._product_handler.save()
            case 2:
                self._product_handler.products()
            case 3:
                self._product_handler.product()
            case 4:
                self._product_handler.update()
            case 5:
                self._product_handler.delete()

