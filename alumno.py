from grupos import Grupo
from carreras import Carrera
class Alumno:
    def __init__(self, nombre, apaterno, amaterno, curp=None, matricula=None):
        self.nombre = nombre
        self.apaterno = apaterno
        self.amaterno = amaterno
        self.curp = curp  
        self.matricula = matricula  

    def __str__(self):
        curp_str = self.curp if self.curp else "CURP no disponible"
        matricula_str = self.matricula if self.matricula else "Matrícula no disponible"
        return f'{self.nombre} {self.apaterno} {self.amaterno} - {curp_str} - {matricula_str}'

    def __repr__(self):
        return f"Alumno(nombre='{self.nombre}', apaterno='{self.apaterno}', amaterno='{self.amaterno}', curp='{self.curp}', matricula='{self.matricula}')"

    def editar_datos(self, nombre=None, apaterno=None, amaterno=None, curp=None, matricula=None):
        """Edita los datos del alumno"""
        if nombre:
            self.nombre = nombre
        if apaterno:
            self.apaterno = apaterno
        if amaterno:
            self.amaterno = amaterno
        if curp:
            self.curp = curp
        if matricula:
            self.matricula = matricula

    def eliminar_datos(self):
        """Elimina (resetea) los datos del alumno"""
        self.nombre = None
        self.apaterno = None
        self.amaterno = None
        self.curp = None
        self.matricula = None

    def exportar(self):
        """Exporta los datos del alumno"""
        return {
            'nombre': self.nombre,
            'apaterno': self.apaterno,
            'amaterno': self.amaterno,
            'curp': self.curp,
            'matricula': self.matricula
        } 

if __name__ == "__main__":
    # Crear instancias de alumnos
    alumno1 = Alumno("Juan", "Pérez", "García", "CURP123", "M123")
    alumno2 = Alumno("Ana", "López", "Ramírez", "CURP456", "M456")
    alumno3 = Alumno("Carlos", "Martínez", "Sánchez")

    # Crear un grupo y agregar alumnos
    grupo1 = Grupo("A", "1")
    grupo1.agregar_alumno(alumno1)
    grupo1.agregar_alumno(alumno2)
    grupo1.agregar_alumno(alumno3)

    # Crear una carrera y agregar el grupo
    carrera1 = Carrera("Ingeniería", "ING123")
    carrera1.agregar_grupo(grupo1)

    # Mostrar los grupos y alumnos de la carrera
    carrera1.mostrar_grupos()

    # Exportar los datos de los alumnos en un arreglo
    print("\nDatos exportados de los alumnos:")
    arreglo_alumnos = grupo1.exportar_alumnos()
    print(arreglo_alumnos)

    # Editar los datos de un alumno
    print("\nEditando datos de Ana López...")
    alumno2.editar_datos(nombre="Ana María", curp="CURP789")

    # Mostrar nuevamente el grupo para ver los cambios
    carrera1.mostrar_grupos()

    # Mostrar el arreglo actualizado
    print("\nArreglo actualizado de los alumnos:")
    arreglo_alumnos_actualizado = grupo1.exportar_alumnos()
    print(arreglo_alumnos_actualizado)

#crear un arreglo que muestre los datos del alumno y asi mismo al crear el metodo de editar sea al arreglo mas no a las clases
#quitar el exportar
#quitar si hay matricula
