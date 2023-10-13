from Varios import Varios
from Productos import Productos
from Funciones import Funciones
p = Productos()


class Menu(Varios and Productos and Funciones):
    def __init__(self):
        p
        self.MenuCarrito()

    def MenuCarrito(self):
        while True:
            print("Menu:")
            print("1. Agregar un producto al carrito")
            print("2. Elimiar un producto del carrito")
            print("3. Modificar producto agregado")
            print("4. Finalizar Compra")
            print("5. Salir del programa")
            op = self.LeerString("Selecciona una opción: ")
            if op == "1":
                print("Has seleccionado la Opción 1.")
                self.InsertarCarrito()
            if op == "2":
                print("Has seleccionado la Opción 2.")
                self.EliminarCarrito()
            if op == "3":
                print("Has seleccionado la Opción 3.")
                self.ModificarCarrito()
            if op == "4":
                print("Has seleccionado la Opción 4.")
                self.FinalizarCompra()
            elif op == "5":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")
            self.MostrarCarrito()
