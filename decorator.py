import functools

# Creamos un decorador que nos ayude a medir el tiempo de ejecución
# Sin tener que escribirlo para cada función
# código basado en https://realpython.com/primer-on-python-decorators/#timing-functions
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Ejecutando función {func.__name__!r}")
        # ejecuta función con sus argumentos, y guarda valor retornado
        value = func(*args, **kwargs)
        # guarda tiempo de finalización
        print(f"Terminó función {func.__name__!r}")
        return value
    return wrapper