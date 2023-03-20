# a metaclass controla a criação da class e a instanciação de objetos
# com isso agente pode usar a metaclass para usar o singleton
class University(type):
    def __call__(cls, *args, **kwargs):
        print(f"=== Estes são os argumentos: {args}")
        return type.__call__(cls, *args, **kwargs)


class geek(metaclass=University):
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2


obj = geek(42, 23)
print(obj)
