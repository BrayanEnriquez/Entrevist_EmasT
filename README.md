## Parte 2: cálculo de precios

### Defectos corregidos

1. **Descuentos no acumulados:** con un producto digital y stock mayor a 50,
	el descuento de stock reemplazaba el precio ya rebajado y se calculaba
	sobre el precio base. Se corrigió aplicando ambos descuentos de forma
	secuencial.
2. **Filtro de bajo stock incompleto:** `productos_bajo_stock` retornaba al
	encontrar el primer producto que no cumplía el umbral, por lo que no
	revisaba los productos siguientes. Se corrigió para recorrer toda la
	colección.
3. **Alerta mezclada con el cálculo:** la alerta se imprimía desde el método
	de precio, dificultando su uso por una interfaz o API. Ahora se expone en
	`producto.alertas` como estado consultable.

### Diseño y orden de aplicación

`ProductoDigital` y `ProductoFisico` heredan de `Producto` y redefinen
`calcular_precio_final()` mediante polimorfismo. El cupón se habilita con
`aplicar_cupon=True`.

El orden implementado es: descuento propio del tipo, descuento por stock
mayor a 50, cupón del 10% limitado a $20.000, costo de envío físico al final
y piso del 60% del precio base. La alerta se registra cuando el precio final
queda por debajo de $5.000.

### Pruebas

Desde la raíz del repositorio ejecutar:

```text
python -m unittest -v Parte_2.test_fns
```
