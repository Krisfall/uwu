numeracion=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 10, 2, 2, 2, 2, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
promedio=sum(numeracion) / len(numeracion)
numeracion_mayor=[numeracion for numeracion in numeracion if numeracion < promedio]
cantidad_mayor= [numeracion_mayor]
print(f"el promedio es: {promedio}")
print(f"la numeracion mayor: {numeracion_mayor")
print(f"la cantidad mayor es: {cantidad_mayor}")