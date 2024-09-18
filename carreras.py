from grupos import Grupo
from alumnos import Alumno

class Carrera:
    def __init__(self, nombre=None, clave=None):
        self.nombre = nombre  # Nombre es opcional
        self.clave = clave  # Clave es opcional
        self.grupos = []

    def agregar_grupo(self, grupo: Grupo):
        self.grupos.append(grupo)

    def mostrar_grupos(self):
        nombre_str = self.nombre if self.nombre else "Nombre no asignado"
        clave_str = self.clave if self.clave else "Clave no asignada"

        print(f'Carrera: {nombre_str} - Clave: {clave_str}')
        for grupo in self.grupos:
            grupo.mostrar_alumnos()


if __name__ == "__main__":
    alumno1 = Alumno("Juan", "Pérez", "García", "CURP123", "M123")
    alumno2 = Alumno("Ana", "López", "Martínez", "CURP456", "M456")
    alumno3 = Alumno("Luis", "Ramírez", "Torres", "CURP789", "M789")

    alumno4 = Alumno("Carlos", "Díaz", "Hernández", "CURP321", "M321")
    alumno5 = Alumno("María", "González", "Sánchez", "CURP654", "M654")
    alumno6 = Alumno("Sofía", "Martínez", "Fernández", "CURP987", "M987")

    grupo1 = Grupo("A", 1)
    grupo1.agregar_alumno(alumno1)
    grupo1.agregar_alumno(alumno2)
    grupo1.agregar_alumno(alumno3)

    grupo2 = Grupo()  
    grupo2.agregar_alumno(alumno4)
    grupo2.agregar_alumno(alumno5)
    grupo2.agregar_alumno(alumno6)

    carrera1 = Carrera("Ingeniería en Sistemas", "IS123")
    carrera1.agregar_grupo(grupo1)

    carrera2 = Carrera()  
    carrera2.agregar_grupo(grupo2)

    print("Datos de la Carrera 1:")
    carrera1.mostrar_grupos()

    print("\nDatos de la Carrera 2:")
    carrera2.mostrar_grupos()