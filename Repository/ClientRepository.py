from Domain.Client import Client
from Utils.JsonManager import JsonManager, open_json, update_json


class ClientRepository:

    def __init__(self):
        self._jsonPath = "/Data/ClientData.json"
        self._jsonManager = JsonManager()

    def save(self, client: Client):
        clients = open_json(self._jsonPath)
        if len(clients) != 0:
            for item in clients:
                if item['CPF'] == client.get_cpf():
                    print("Cliente já existe.")
                    break
                else:
                    clients.append({"name": client.get_name(), "CPF": client.get_cpf(), "rebate": client.get_rebate()})
                    print("Cliente cadastrado com sucesso.")
                    break
        else:
            clients.append({"name": client.get_name(), "CPF": client.get_cpf(), "rebate": client.get_rebate()})
            print("Cliente cadastrado com sucesso.")

        update_json(self._jsonPath, clients)

    def clients(self):
        clients = open(self._jsonPath)
        return clients

    def client(self, cpf: int):
        clients = open_json(self._jsonPath)
        for client in clients:
            if client["CPF"] == cpf:
                return client
        raise ValueError("Cliente não encontrado.")

    def update(self, client: Client):
        clients = open_json(self._jsonPath)
        for item in clients:
            if item["CPF"] == client.get_cpf():
                item["name"] = client.get_name()
                item["rebate"] = client.get_rebate()
                update_json(self._jsonPath, clients)
                return "Cliente atualizado com sucesso."
        raise ValueError("Cliente não encontrado.")

    def delete(self, cpf: int):
        clients = open_json(self._jsonPath)
        for index in range(len(clients)):
            if clients[index]["CPF"] == cpf:
                clients.pop(index)
                update_json(self._jsonPath, clients)
                return "Cliente deletado com sucesso."
        raise ValueError("Cliente não encontrado.")
