from Services.CashService import CashService


class CashHandler:
    def __init__(self):
        self._cashService = CashService()

    def start_sale(self):
        while True:
            print("Digite o código do produto: ")
            product_id = int(input())

            product = self._cashService.get_product(product_id)

            print("Digite a quantidade de produtos: ")
            quantity = int(input())

            print("Caso deseje finalizar a venda, digite 1\n"
                  "Caso não, digite 0.")
            choice = int(input())

            if choice == 1:
                print("Digite o CPF do cliente:")
                cpf = int(input())

                client = self._cashService.get_client(cpf)

                if client['CPF']:
                    value = product['value'] * quantity
                    total_value = value - (value * (client['rebate']/100))

                    print(f"Valor a ser pago: R$${total_value}")
                    print("Digite o dinheiro do cliente: ")
                    client_cash = float(input())

                    if client_cash > total_value:
                        transshipment = client_cash - total_value
                        print(f"Entregue ${round(transshipment, 2)} de troco ao cliente.")

                        self._cashService.apply_rebate(cpf, 0.0)
                        self._cashService.sale(client_cash-transshipment)
                        self._cashService.update_product(product_id, quantity)
                        break
                    elif client_cash < total_value:
                        print("O dinheiro é menor que o total.")
                else:
                    print("Impossível finalizar compra. Cliente não existe.")

            elif choice == 0:
                continue

    def money(self):
        money = self._cashService.money()
        print("Tem R${} no caixa.".format(money["money"]))

    def apply_rebate(self):
        print("Digite o CPF do cliente: ")
        cpf = int(input())

        client = self._cashService.get_client(cpf)

        if client['CPF']:
            print("Digite o desconto a ser dado na próxima compra: ")
            rebate = float(input())
            self._cashService.apply_rebate(cpf, rebate)
        elif not client['cpf']:
            print("Impossível aplicar desconto. Cliente não existe.")

