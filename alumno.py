class Alumno:
    alumnos_creados = []

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

    def crear_alumno(self, nombre, apaterno, amaterno, curp=None, matricula=None):
        """Crea un nuevo alumno y lo almacena en la lista alumnos_creados"""
        nuevo_alumno = Alumno(nombre, apaterno, amaterno, curp, matricula)
        Alumno.alumnos_creados.append(nuevo_alumno)
        print(f'Alumno {nuevo_alumno.nombre} {nuevo_alumno.apaterno} creado y almacenado.')

    @classmethod
    def editar_alumno(cls, nombre_busqueda, nombre=None, apaterno=None, amaterno=None, curp=None, matricula=None):
        """Busca un alumno por su nombre y edita los datos proporcionados"""
        for alumno in cls.alumnos_creados:
            if alumno.nombre == nombre_busqueda:
                if nombre:
                    alumno.nombre = nombre
                if apaterno:
                    alumno.apaterno = apaterno
                if amaterno:
                    alumno.amaterno = amaterno
                if curp:
                    alumno.curp = curp
                if matricula:
                    alumno.matricula = matricula
                print(f'Alumno {nombre_busqueda} ha sido editado.')
                return
        print(f'Alumno {nombre_busqueda} no encontrado.')

    @classmethod
    def mostrar_alumnos_creados(cls):
        """Muestra todos los alumnos creados y almacenados en alumnos_creados"""
        if cls.alumnos_creados:
            print("Lista de alumnos creados:")
            for alumno in cls.alumnos_creados:
                print(alumno)
        else:
            print("No hay alumnos creados.")

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
    # Crear alumnos y almacenarlos
    alumno1 = Alumno("Juan", "Pérez", "García", "CURP123", "M123")
    alumno2 = Alumno("Ana", "López", "Ramírez", "CURP456", "M456")
    
    # Crear más alumnos con el método crear_alumno
    Alumno.crear_alumno(Alumno, "Carlos", "Martínez", "Sánchez", "CURP789", "M789")
    Alumno.crear_alumno(Alumno, "Luis", "Ramírez", "Torres", "CURP321", "M321")

    # Mostrar todos los alumnos creados
    Alumno.mostrar_alumnos_creados()

    # Editar un alumno existente
    print("\nEditando datos de 'Carlos'...")
    Alumno.editar_alumno("Carlos", nombre="Carlos Alberto", curp="CURP999")

    # Mostrar todos los alumnos nuevamente para ver el cambio
    Alumno.mostrar_alumnos_creados()
