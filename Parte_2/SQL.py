"""

SELECT p.nombre
	, c.nombre
FROM productos p
INNER JOIN categorias c
ON p.categoria_id = c.id
WHERE p.activo = 1 AND p.stock <10
ORDER BY p.stock ASC

SELECT c.nombre
	, AVG(p.precio) AS precio_prom
FROM categorias c
LEFT JOIN productos p
ON p.categoria_id = c.id
GROUP BY c.Nombre


SELECT p.Nombre
	, SUM(cantidad)
FROM productos p
RIGHT JOIN movimientos m
ON p.id = m.producto_id
WHERE tipo = 'entrada'
GROUP BY p.Nombre

"""