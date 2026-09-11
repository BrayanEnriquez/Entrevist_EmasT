"""Pricing rules for physical and digital products."""

from abc import ABC, abstractmethod


DESCUENTO_DIGITAL = 0.15
DESCUENTO_STOCK_ALTO = 0.05
UMBRAL_STOCK_ALTO = 50
DESCUENTO_CUPON = 0.10
TOPE_DESCUENTO_CUPON = 20_000
PRECIO_MINIMO_RELATIVO = 0.60
UMBRAL_REVISION_MARGEN = 5_000
MENSAJE_REVISION_MARGEN = "Revisión de margen necesaria"


class Producto(ABC):
    """Shared product data and discount rules."""

    def __init__(self, nombre, precio, stock):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        self.nombre = nombre
        self.precio = precio  # precio base en COP
        self.stock = stock
        self.alertas = []

    def _precio_con_descuentos(self, aplicar_cupon=False):
        precio = self.precio
        if self.stock > UMBRAL_STOCK_ALTO:
            precio *= 1 - DESCUENTO_STOCK_ALTO
        if aplicar_cupon:
            descuento_cupon = min(precio * DESCUENTO_CUPON, TOPE_DESCUENTO_CUPON)
            precio -= descuento_cupon
        return precio

    def _registrar_alerta_margen(self, precio_final):
        self.alertas.clear()
        if precio_final < UMBRAL_REVISION_MARGEN:
            self.alertas.append(MENSAJE_REVISION_MARGEN)

    @abstractmethod
    def calcular_precio_final(self, aplicar_cupon=False):
        """Return the final price and update ``alertas``."""

    @staticmethod
    def productos_bajo_stock(productos, umbral=10):
        return [producto for producto in productos if producto.stock < umbral]


class ProductoDigital(Producto):
    def calcular_precio_final(self, aplicar_cupon=False):
        precio = self.precio * (1 - DESCUENTO_DIGITAL)
        # Orden: descuento digital, descuento por stock, cupón, piso mínimo.
        precio = precio * (1 - DESCUENTO_STOCK_ALTO) if self.stock > UMBRAL_STOCK_ALTO else precio
        if aplicar_cupon:
            precio -= min(precio * DESCUENTO_CUPON, TOPE_DESCUENTO_CUPON)
        precio = max(precio, self.precio * PRECIO_MINIMO_RELATIVO)
        self._registrar_alerta_margen(precio)
        return precio


class ProductoFisico(Producto):
    def __init__(self, nombre, precio, stock, costo_envio=0):
        super().__init__(nombre, precio, stock)
        if costo_envio < 0:
            raise ValueError("El costo de envío no puede ser negativo")
        self.costo_envio = costo_envio

    def calcular_precio_final(self, aplicar_cupon=False):
        # Orden: descuentos, cupón, envío al final y piso mínimo sobre el total.
        precio = self._precio_con_descuentos(aplicar_cupon)
        precio += self.costo_envio
        precio = max(precio, self.precio * PRECIO_MINIMO_RELATIVO)
        self._registrar_alerta_margen(precio)
        return precio