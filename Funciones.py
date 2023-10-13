from Varios import Varios
from Productos import Productos


class Funciones(Varios and Productos):
    carrito = []
    total = 0.0
    viejo = 0.0
    nuevo = 0.0
    # no = 0
    # nombre = ""
    # precio = 0.0
    # descripcion = ""

    # def __init__(self):
    #     self.InsertarCarrito()
    #     self.InsertarCarrito()
    #     self.EliminarCarrito()
    #     self.ModificarCarrito()
    #     self.FinalizarCompra()
    #     self.MostrarCarrito()

    def MostrarCarrito(self):
        for c in self.carrito:
            no, nombre, precio, descripcion, can = c
            print()
            print("ID:", no)
            print("Nombre:", nombre)
            print("Precio:", precio)
            print("Descripción:", descripcion)
            print("Cantidad:", can)
            print()
        print(f"Total: {self.total}")

    def InsertarCarrito(self):
        prod = self.LeerString("Ingresa el producto que desea comprar: ")
        if prod == "":
            print()
            print("Ingrese un producto")
        else:
            for p in self.productos:
                no, nombre, precio, descripcion = p
                if (p[1] == prod):
                    # can = int(input("Cantidad que desea agregar: "))
                    can = self.LeerInt("Cantidad que desea agregar: ")
                    print("Producto: ")
                    self.carrito.append(
                        self.reg(no, nombre, precio, descripcion, can))
                    pre = float(precio)*can
                    self.total += pre

    def EliminarCarrito(self):
        if (self.total != 0.0):
            nom = self.LeerString(
                "Ingresa el producto que deseas eliminar de la lista: ")
            for c in self.carrito:
                no, nombre, precio, descripcion, can = c
                if (c[1] == nom):
                    self.carrito.remove(c)
                    pre = float(precio)*can
                    self.total -= pre
        else:
            print("Agrega algunos productos a tu carrito primero")

    def ModificarCarrito(self):
        if (self.total != 0.0):
            nom = input(
                "Ingresa el producto que deseas modificar de la lista: ")
            for c in self.carrito:
                no, nombre, precio, descripcion, can = c
                if (c[1] == nom):
                    print("bien")
                    self.viejo = precio*can
                    # print(f"vieja cantidad {viejo}")
                    if (can != 0):
                        # can = int(input("Nueva cantidad mien: "))
                        can = self.LeerInt("Nueva cantidad: ")
                        c = no, nombre, precio, descripcion, can
                        self.carrito[c.index(no)] = c
                        self.nuevo = precio*can
                        self.total -= self.viejo
                        self.total += self.nuevo
                    # print(f"Nueva cantidad {nuevo}")
        else:
            print("Agrega algunos productos a tu carrito primero")

    def FinalizarCompra(self):
        if (self.total != 0.0):
            print("Deseas realizar la compra de estos productos: ")
            self.MostrarCarrito()
            respuesta = self.LeerString(
                "Escribe confirmar para proceder con la compra o en caso contrario escribe cancelar: ")
            if (respuesta == "confimar" or respuesta == "Confirmar"):
                print()
                print("Compra realizada con exito")
                print()
                self.carrito.clear()
                self.total = 0.0
            elif (respuesta == "cancelar" or respuesta == "Cancelar"):
                print("Esperaremos a que estes listo para realizar tu compras")
            else:
                print("Esta opcion no es valida, elige confirmar o cancelar")
            # print(f"Total: {total}")
        else:
            print()
            print("Agrega algunos productos a tu carrito primero")
