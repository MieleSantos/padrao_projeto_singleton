# usando o Lazy, permite criar uma classe sem a inicialização do objeto
# ele é inicialição quando é chamado
class Singleton:
    __instance = None

    def __init__(self) -> None:
        if not Singleton.__instance:
            print("O metodo __init__ foi chamado...")
        else:
            print(f"A instância já foi criada: {self.get_instance()}")

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


# a classe é inicializadao mas o objeto não é criado
s1 = Singleton()

print(f"Objeto criado agora: {Singleton.get_instance()}")

# instancia já criada
s2 = Singleton()
