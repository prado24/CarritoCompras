from Varios import Varios


class Productos(Varios):
    productos = []

    def __init__(self):
        self.Insertar()
        self.MostrarP()

    def reg(self, *datos):
        return datos

    def Insertar(self):
        self.productos.append(self.reg(1, "Producto 1", 10.00,
                                       "Este es el producto número 1."))
        self.productos.append(self.reg(2, "Producto 2", 20.00,
                                       "Este es el producto número 2."))
        self.productos.append(self.reg(3, "Producto 3", 30.00,
                                       "Este es el producto número 2."))
        self.productos.append(self.reg(4, "Producto 4", 40.00,
                                       "Este es el producto número 2."))
        self.productos.append(self.reg(5, "Producto 5", 50.00,
                                       "Este es el producto número 2."))
        self.productos.append(self.reg(6, "Producto 6", 60.00,
                                       "Este es el producto número 2."))
        self.productos.append(self.reg(7, "Producto 7", 70.00,
                                       "Este es el producto número 2."))
        self.productos.append(self.reg(8, "Producto 8", 80.00,
                                       "Este es el producto número 2."))
        self.productos.append(self.reg(9, "Producto 9", 90.00,
                                       "Este es el producto número 2."))
        self.productos.append(self.reg(10, "Producto 10", 100.00,
                                       "Este es el producto número 10."))

    def MostrarP(self):
        for producto in self.productos:
            no, nombre, precio, descripcion = producto
            print("Id:", no)
            print("Nombre:", nombre)
            print("Precio:", precio)
            print("Descripción:", descripcion)
            print()
