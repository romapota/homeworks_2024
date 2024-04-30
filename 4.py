import random
class Server:
    buffer = []
    different_ip = [i for i in range(0, 100)]
    def __init__(self):
        try:
            self.ip = Server.different_ip[0]
            Server.different_ip.pop(0)
        except: print("Превышенно максимально количество серверов, новый сервер не может быть добавлен в сеть")
        self.buffer = []
        self.router = None
    def send_data(self, data):
        try:
            self.router.buffer.append(data)
        except: print(f"Сервер не подключен к роутеру")
    def get_data(self):
        data = [i for i in self.buffer]
        self.buffer = []
        return data
    def get_ip(self):
        return self.ip
class Router:
    buffer = []
    ip = dict()
    def __init__(self):
        self.to_ip = None
    def link(self, server):
        self.ip[server.get_ip()] = server
        server.router = self
    def unlink(self, server):
        Router.ip.pop(server.get_ip())
    def send_data(self):
        try:
            for i in range(len(self.buffer)):
                self.ip[self.buffer[i].to_ip].buffer.append(self.buffer[i].data)
        except: print("Сервер не подключен к роутеру. Сообщение не отправлено.")
class Data:
    def __init__(self, data, to_ip):
        self.data = data
        self.to_ip = to_ip
