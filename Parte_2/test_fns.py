import unittest

from Parte_2.fns import ProductoDigital, ProductoFisico


class CalculoPrecioTest(unittest.TestCase):
    def test_descuentos_digital_y_stock_son_acumulativos(self):
        producto = ProductoDigital("Curso", 10_000, 51)

        self.assertEqual(producto.calcular_precio_final(), 8_075)

    def test_cupon_tiene_tope_y_se_aplica_despues_de_descuentos(self):
        producto = ProductoDigital("Licencia", 300_000, 51)

        self.assertEqual(producto.calcular_precio_final(aplicar_cupon=True), 222_250)

    def test_borde_stock_50_no_recibe_descuento_de_stock(self):
        producto = ProductoFisico("Libro", 10_000, 50, costo_envio=500)

        self.assertEqual(producto.calcular_precio_final(), 10_500)

    def test_piso_minimo_y_alerta_de_margen(self):
        producto = ProductoDigital("Icono", 1_000, 0)

        self.assertEqual(producto.calcular_precio_final(aplicar_cupon=True), 600)
        self.assertEqual(producto.alertas, ["Revisión de margen necesaria"])


if __name__ == "__main__":
    unittest.main()
