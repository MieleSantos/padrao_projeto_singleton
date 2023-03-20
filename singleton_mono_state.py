class Monostate:
    __estado = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__estado
        return obj


m1 = Monostate()
print(f"M1 Id: {id(m1)}")
print(m1.__dict__)

# nova instancia
m2 = Monostate()
print(f"M2 Id: {id(m2)}")
print(m2.__dict__)

# mudando estado d m1
m1.nome = "Felicity"

print(f"M1: {m1.__dict__}")
print(f"M2: {m2.__dict__}")

# executando as instancias tem o mesmo estado
# M1 Id: 2292219035312
# {}
# M2 Id: 2292219035264
# {}
# M1: {'nome': 'Felicity'}
# M2: {'nome': 'Felicity'}
