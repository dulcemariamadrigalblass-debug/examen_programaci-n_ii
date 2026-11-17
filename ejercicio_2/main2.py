
class Producto(object): 
    def __init__(self, base, altura): 
        self.base = base
        self.altura = altura
        self.Area = 0 
    
    def calcularArea(self, cantidad): 
        self.Area = self.altura * cantidad 

    def mostrarArea(self): 
        print(f"Rectangulo: {self.base}") 
        print(f"Area: ${self.Area:.2f}") 

def main():
    Rectangulo = Producto("Cuaderno", 35) 
    Rectangulo.calcularArea(3) 
    Rectangulo.mostrarArea()
    
    # COMPLETAR: crear un objeto con base 8 y altura 5 
    rectangulo2 = Producto(8, 5)
    
    # COMPLETAR: llamar al método para mostrar el área 
    rectangulo2.calcularArea(1)  # Se calcula el área multiplicando la altura por la cantidad
    rectangulo2.mostrarArea()

if __name__ == "__main__":
    main()