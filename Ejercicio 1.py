class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @codigo.setter
    def nombre(self, valor):
        self.__nombre = valor
        
    @property
    def precio(self):
        return self.__precio
    
    @codigo.setter
    def precio(self, valor):
        self.__precio = valor
    
    def calcular_total(self, unidades):
        return self.precio * unidades


    def __str__(self):
        return 'Código: ' + str(self.__codigo) + ', nombre: ' + str(self.__nombre) + ', precio final: ' + str(self.__precio) + ' euros'
    
p1 = Producto(1, 'Producto 1', 5)
p2 = Producto(2, 'Producto 2', 10)
p3 = Producto(3, 'Producto 3', 20)

print(p1)
print(p2)
print(p3)
