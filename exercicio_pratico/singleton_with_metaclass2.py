# usando a meta class para controla a criação de objeto singleton
class MetaSingleton(type):
    __instances = {}

    def __class__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
            return cls.__instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


log1 = Logger()

print(f"log 1: {id(log1)}")

log2 = Logger()
print(f"log 2: {id(log2)}")
