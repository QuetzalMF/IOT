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
        """Exporta los datos del alumno como un diccionario"""
        return {
            'nombre': self.nombre,
            'apaterno': self.apaterno,
            'amaterno': self.amaterno,
            'curp': self.curp,
            'matricula': self.matricula
        }

class ListaAlumnos:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        """Agrega un objeto Alumno al arreglo de alumnos"""
        self.alumnos.append(alumno)

    def mostrar_alumnos(self):
        """Muestra la lista completa de alumnos"""
        for alumno in self.alumnos:
            print(alumno)

    def exportar_todos(self):
        """Exporta los datos de todos los alumnos como una lista de diccionarios"""
        return [alumno.exportar() for alumno in self.alumnos]


if __name__ == "__main__":
    # Crear algunos objetos Alumno
    alumno1 = Alumno("Juan", "Pérez", "García", "CURP123", "M123")
    alumno2 = Alumno("Ana", "López", "Martínez", "CURP456", "M456")

    lista_alumnos = ListaAlumnos()

    # Agregar alumnos a la lista
    lista_alumnos.agregar_alumno(alumno1)
    lista_alumnos.agregar_alumno(alumno2)

    # Mostrar alumnos
    print("Lista de alumnos:")
    lista_alumnos.mostrar_alumnos()

    # Exportar los datos de todos los alumnos
    print("\nDatos exportados de todos los alumnos:")
    datos_exportados = lista_alumnos.exportar_todos()
    print(datos_exportados)


#hacer que el editar sea mediante el arreglo 
# agregar el arreglo en el primer def y solo mandar llamar el objeto en otro def nuevo, no se que mas ayuda