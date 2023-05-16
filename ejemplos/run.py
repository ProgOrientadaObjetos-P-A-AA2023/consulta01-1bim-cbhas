
import mis_clases

persona1 = mis_clases.Persona("1105747016", "Sebastián", "Calderón", 18)
print(persona1)


nombre = input(str("\nIngrese su nombre:\n> "))
apellido = input(str("Ingrese su apellido:\n> "))
cedula = input(str("Ingrese su cedula:\n> "))
edad = int(input("Ingrese su edad:\n> "))

persona2 = mis_clases.Persona(nombre, apellido, cedula, edad)
print(f"\n{persona2}")
