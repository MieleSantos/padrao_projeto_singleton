# Padrão de projeto Singleton


class Singleton(object):
    def __new__(cls):
        """
        __new__ cria um novo objeto, é executando antes do __init__
        """
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f"Criando o objeto {cls.instance}")
        return cls.instance


s1 = Singleton()
print(f"Instância 1: {id(s1)}")


s2 = Singleton()
print(f"Instância 2: {id(s1)}")
