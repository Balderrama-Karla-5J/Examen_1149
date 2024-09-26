#zona de clase
class libros1149():
    #Inicializacion de datos
    IdLibro_1149 = 0
    Autor_1149 = ""
    Ilustrardor_1149=""
    Titulo_1149=""
    año_1149=0
    precio_1149=0
    stock_1149=0
    #Zona de funciones
    def mostrardatos1149(self):
        print("------Mostrar los datos---------")
        print(f"Id del libro: {self.IdLibro_1149} ")
        print(f"Autor: {self.Autor_1149}")
        print(f"Ilsutrador: {self.Ilustrardor_1149}")
        print(f"Titulo: {self.Titulo_1149}")
        print(f"Año de salida: {self.año_1149}")
        print(f"Precio: $ {self.precio_1149}")
        
    def listarAños1149(self):
        años = [1907, 2018, 1825, 2022, 1400, 1996, 2002]
        print(" \n-------Lista de años de salida--------")
        print(años)
        for c in años:
            print(c)
    def tuplaAutores1149(self):
        Autor=("Carlos Ruiz", "Julia Navarro", "Julio Cortazar", "Jane Austen", "Homero", "Miguel Cervantes", "J.K Rowling")
        print("\n--------Tupla de Autores-----------")
        print(Autor)
        for e in Autor:
            print(e)
    def DiccionarioLibros1149(self):
        Libros = {f"Sherlock Holmes: $": 299.00, "Seras: $":349.00, "El principito: $": 429.00, "La iliada: $" :500.00,
                  "Don quijote: $": 499.00, "Harry Potter: $":299.00, "Orgullo y Prejuicio: $": 349.00}
        print("\n--------Diccionario de Libros y Precios--------")
        print(Libros)
        for x,y in Libros.items():
            print(x,y)
    def alta1149(self):
        print("Libro registrado con exito")
    def baja1149 (self):
        print("Libro eliminado con exito")

#zona de creacion del obijeto
obj = libros1149()

#Uso del Objeto 
obj.IdLibro_1149=112
obj.Autor_1149= "Julio Cortazar"
obj.Ilustrardor_1149= "No ilustrado"
obj.Titulo_1149= "Cien años de soledad"
obj.año_1149= 1945
obj.precio_1149= 499.00
obj.stock_1149= 50


#zona de llamada de funciones
obj.mostrardatos1149()
obj.listarAños1149()
obj.tuplaAutores1149()
obj.DiccionarioLibros1149()
obj.alta1149()
obj.baja1149()