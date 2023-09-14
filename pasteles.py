class Pasteles:
    #constructor de la clase y sus atributos
    def __init__(self, sabor, precio):
        self.sabor = sabor
        self.precio = precio

    #definir metodos de la clase
    def info(self):
        print(f"Bienvenido, el sabor de este pastel es de {self.sabor} y tiene un precio de {self.precio} pesos.")

#crear objetos
pastel1 = Pasteles("helado de vainilla con fresas", 350)
pastel2 = Pasteles("chocolate con nuez", 400)

#Llamar al método
pastel1.info()
pastel2.info()
