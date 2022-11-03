from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):
#Constructor que coge el dicc y lo pasa a atributos
    def __init__(self, data: dict): # le pasamos data y le decimos que este debe ser un dicc
        for key, value in data.items: # Conv el dicc en un listado de tuplas
            setattr(self, key, value) # Aqui cada clave se convierte en un atributo