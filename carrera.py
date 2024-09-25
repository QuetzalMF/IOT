from grupo import Grupo
from alumno import Alumno

class Carrera:
    def __init__(self, nombre=None, clave=None):
        self.nombre = nombre  # Nombre de la carrera
        self.clave = clave  # Clave de la carrera
        self.grupos = []

    def agregar(self, grupo: Grupo):
        """Agrega un grupo a la carrera"""
        self.grupos.append(grupo)

    def listar(self):
        """Lista los grupos y alumnos de la carrera"""
        nombre_str = self.nombre if self.nombre else "Nombre no asignado"
        clave_str = self.clave if self.clave else "Clave no asignada"

        print(f'Carrera: {nombre_str} - Clave: {clave_str}')
        for grupo in self.grupos:
            grupo.listar()

    def exportar(self):
        """Exporta los datos de todos los grupos y alumnos de la carrera"""
        return [grupo.exportar() for grupo in self.grupos]

            
    


if __name__ == "__main__":
    alumno1 = Alumno("Juan", "Pérez", "García", "CURP123", "M123")
    alumno2 = Alumno("Ana", "López", "Martínez", "CURP456", "M456")
    alumno3 = Alumno("Luis", "Ramírez", "Torres", "CURP789", "M789")

    alumno4 = Alumno("Carlos", "Díaz", "Hernández", "CURP321", "M321")
    alumno5 = Alumno("María", "González", "Sánchez", "CURP654", "M654")
    alumno6 = Alumno("Sofía", "Martínez", "Fernández", "CURP987", "M987")

    grupo1 = Grupo("A", 1)
    grupo1.agregar(alumno1)
    grupo1.agregar(alumno2)
    grupo1.agregar(alumno3)

    grupo2 = Grupo()  
    grupo2.agregar(alumno4)
    grupo2.agregar(alumno5)
    grupo2.agregar(alumno6)

    carrera1 = Carrera("Ingeniería en Sistemas", "IS123")
    carrera1.agregar(grupo1)

    carrera2 = Carrera()  
    carrera2.agregar(grupo2)

    print("Datos de la Carrera 1:")
    carrera1.listar()

    print("\nDatos de la Carrera 2:")
    carrera2.listar()