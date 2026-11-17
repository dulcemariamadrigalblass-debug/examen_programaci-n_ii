'''
1. ¿Cuál es el nombre de la clase? 
   = Producto
2. ¿Cuáles son sus propiedades? 
    = nombre, precio y total

3. ¿Cuáles son sus métodos? 
    = calcular el total y devolverlo, mostrándolo

4. ¿Qué función cumple __init__?
   Inicializa al objeto, en este caso el producto y le asigna valores a las propiedades

5. ¿Para qué se utiliza self?
   devuelve y llama a las propiedades y métodos y se puedan usar en otras partes dentro del código del programa

6. ¿En qué instrucción se crea un objeto?
    cuando se llama a la clase y le asigna una variable, por ejeplo en producto 1 es
     = producto("x", valor), qu en este caso sería producto1 = Producto("Cuaderno", 35) 

7. ¿Cuál es el nombre del objeto?
   es el producto1 

8. ¿Cómo se llama a calcularTotal()?
   producto1.calcularTotal()

9. ¿Qué valores recibe el constructor cuando se crea el objeto?
el nombre y valor, Cuaderno y 35

10. ¿Qué resultado mostrará el programa?
    el Producto que es Cuaderno, y el precio total con el símbolo $
'''



'''  
class Operacion(object): 
    def __init__(self, numero1, numero2): 
        self.numero1 = numero1 
        self.numero2 = numero2 
  
    def calcular(self): 
        return self.numero1 + self.numero2 
  
class Multiplicacion(Operacion): 
    def calcular(self): 
        return self.numero1 * self.numero2


operacion1 = Operacion(8, 4) 
operacion2 = Multiplicacion(8, 4) 
print(operacion1.calcular()) 
print(operacion2.calcular())

1. ¿Cuál es la clase padre? 
Operacion
2. ¿Cuál es la clase hija? 
multiplicacion

3. ¿Cómo se indica la herencia? 
devolviendo los valores, con return 

4. ¿Qué propiedades utiliza la clase hija? 
calcular, devolver y realizar la operación

5. ¿Por qué puede utilizarlas sin definir su propio __init__? 
porque init ya está dentro la clase padre, y como la está llamando, también está dentrp de la clase hija

6. ¿Por qué los métodos calcular() tienen resultados distintos? 
porque no son valores fijos, dependen de los valores que se le adjudiquen 

7. ¿Qué valores se imprimen? 
los de la operación

8. ¿Qué sucedería si eliminamos calcular() de Multiplicacion?
 no sumaría los 2 primero dígitos, no se realizaría la operación tampoco 
 ''' 