from Handlers.ClientHandler import ClientHandler


class ClientOptions:
    def __init__(self):
        self._clientHandler = ClientHandler()

        self._options()

    def _options(self):
        print("1 - Criar Cliente\n"
              "2 - Exibir Clientes\n"
              "3 - Buscar Cliente\n"
              "4 - Atualizar Cliente\n"
              "5 - Deletar Cliente")
        choice = int(input())

        match choice:
            case 1:
                self._clientHandler.save()
            case 2:
                self._clientHandler.clients()
            case 3:
                self._clientHandler.client()
            case 4:
                self._clientHandler.update()
            case 5:
                self._clientHandler.delete()
