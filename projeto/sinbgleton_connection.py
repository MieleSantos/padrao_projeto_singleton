import sqlite3


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Database:
    connection = None

    def connect(self):
        if self.connection is None:
            print("não temos ainda uma conexão... vamos cria-la...")
            self.connection = sqlite3.connect("db.geek")
            self.cursor = self.connection.cursor()
        return self.cursor


def1 = Database().connect()

def2 = Database().connect()
