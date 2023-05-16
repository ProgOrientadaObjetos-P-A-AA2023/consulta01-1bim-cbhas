
import mis_clases

casa1 = mis_clases.Casa("Pitas", 3, "Blanco", 6)
print(casa1)


ubicacion = input(str("\nIngrese la ubicación:\n> "))
pisos = int(input("Ingrese el número de pisos:\n> "))
color = input(str("Ingrese el color de la casa:\n> "))
ventanas = int(input("Ingrese el número de ventanas:\n> "))

casa2 = mis_clases.Casa(ubicacion, pisos, color, ventanas)
print(f"\n{casa2}")
