
class Producto(object): 
    def __init__(self, nombre, precio): 
        self.nombre = nombre
        self.precio = precio
        self.total = 0 
    
    def calcularTotal(self, cantidad): 
        self.total = self.precio * cantidad 

    def mostrarTotal(self): 
        print(f"Producto: {self.nombre}") 
        print(f"Total: ${self.total:.2f}") 

def main():
    producto1 = Producto("Cuaderno", 35) 
    producto1.calcularTotal(3) 
    producto1.mostrarTotal()

   
if __name__ == "__main__":
    main()
