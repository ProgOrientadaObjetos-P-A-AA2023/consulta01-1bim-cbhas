
class Persona:
    def __init__(self, cedula, nombre, apellido, edad):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def establecerC (self, c):
        self.cedula = c

    def establecerN (self, n):
        self.nombre = n

    def establecerA (self, a):
        self.apellido = a

    def establecerE (self, e):
        self.edad = e
    
    def obtenerC (self):
        return self.cedula

    def obtenerN (self):
        return self.nombre

    def obtenerA (self):
        return self.apellido

    def obtenerE (self):
        return self.edad
    
    def __str__(self):
        mensaje = (f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCédula: {self.cedula}\nEdad: {self.edad}")
        return mensaje
    

class Casa:
    def __init__(self, ubicacion, pisos, color, ventanas):
        self.ubicacion = ubicacion
        self.pisos = pisos
        self.color = color
        self.ventanas = ventanas

    def establecerC (self, u):
        self.ubicacion = u

    def establecerN (self, p):
        self.pisos = p

    def establecerA (self, c):
        self.color = c

    def establecerE (self, v):
        self.ventanas = v
    
    def obtenerC (self):
        return self.ubicacion

    def obtenerN (self):
        return self.pisos

    def obtenerA (self):
        return self.color

    def obtenerE (self):
        return self.ventanas
    
    def __str__(self):
        mensaje = (f"Ubicación: {self.ubicacion}\nNúmero de Pisos: {self.pisos}\nColor de la Casa: {self.color}\nNúmero de Ventanas: {self.ventanas}")
        return mensaje
