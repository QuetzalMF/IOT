class Alumno:
    def __init__(self, nombre=None, apaterno=None, amaterno=None, curp=None, matricula=None, alumnos=None):
        self.nombre = nombre
        self.apaterno = apaterno
        self.amaterno = amaterno
        self.curp = curp
        self.matricula = matricula
        # Inicializa el arreglo de alumnos si no se pasa uno
        self.alumnos = alumnos if alumnos is not None else []

    def __str__(self):
        curp_str = self.curp if self.curp else "CURP no disponible"
        matricula_str = self.matricula if self.matricula else "Matrícula no disponible"
        return f'{self.nombre} {self.apaterno} {self.amaterno} - {curp_str} - {matricula_str}'

    def __repr__(self): #desglosamos el arreglo
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

    def agregar_alumno(self, alumno):
        """Agrega un alumno al grupo de alumnos internos"""
        if isinstance(alumno, Alumno):
            self.alumnos.append(alumno)
        else:
            print("El objeto que intentas agregar no es del tipo Alumno")

    def mostrar_grupo(self):
        """Muestra el grupo de alumnos asociados a este alumno"""
        if self.alumnos:
            print(f"Grupo de {self.nombre}:")
            for alumno in self.alumnos:
                print(alumno)
        else:
            print(f"{self.nombre} no tiene un grupo de alumnos asociado.")

    def editar_grupo(self, matricula, nombre=None, apaterno=None, amaterno=None, curp=None):
        """
        Edita los datos de un alumno dentro del grupo basado en la matrícula
        """
        for alumno in self.alumnos:
            if alumno.matricula == matricula:
                alumno.editar_datos(nombre=nombre, apaterno=apaterno, amaterno=amaterno, curp=curp)
                print(f"Datos actualizados del alumno con matrícula {matricula}:")
                print(alumno)
                return
        print(f"No se encontró un alumno con la matrícula {matricula} en el grupo.")


class ListaAlumnos:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        """Agrega un objeto Alumno al arreglo de alumnos"""
        if isinstance(alumno, Alumno):
            self.alumnos.append(alumno)
        else:
            print("El objeto que intentas agregar no es del tipo Alumno")

    def mostrar_alumnos(self):
        """Muestra la lista completa de alumnos"""
        for alumno in self.alumnos:
            print(alumno)

    def exportar_todos(self):
        """Exporta los datos de todos los alumnos como una lista de diccionarios"""
        return [alumno.exportar() for alumno in self.alumnos]

    def editar_alumno(self, matricula, nombre=None, apaterno=None, amaterno=None, curp=None):
        """
        Edita los datos de un alumno en la lista principal basado en la matrícula
        """
        for alumno in self.alumnos:
            if alumno.matricula == matricula:
                alumno.editar_datos(nombre=nombre, apaterno=apaterno, amaterno=amaterno, curp=curp)
                print(f"Datos actualizados del alumno con matrícula {matricula}:")
                print(alumno)
                return
        print(f"No se encontró un alumno con la matrícula {matricula} en la lista.")

if __name__ == "__main__":
    alumno1 = Alumno("Juan", "Pérez", "García", "CURP123", "M123")
    alumno2 = Alumno("Ana", "López", "Martínez", "CURP456", "M456")

    lista_alumnos = ListaAlumnos()

    lista_alumnos.agregar_alumno(alumno1)
    lista_alumnos.agregar_alumno(alumno2)

    #.....Crear un grupo de alumnos dentro de alumno1
    alumno1.agregar_alumno(alumno2)  
    #.....Alumno1 tiene a Alumno2 en su grupo

    
    print("Lista de alumnos:")
    lista_alumnos.mostrar_alumnos()

    
    print("\nGrupo de alumnos dentro de Alumno1:")
    alumno1.mostrar_grupo()

    # Editar datos de un alumno en la lista
    lista_alumnos.editar_alumno(matricula="M123", nombre="Juanito", apaterno="Pérez Modificado")
    # Editar datos de un alumno en el grupo interno de Alumno1
    alumno1.editar_grupo(matricula="M456", nombre="Ana María", apaterno="López Modificado")

    # Mostrar los cambios
    print("\nLista de alumnos después de editar:")
    lista_alumnos.mostrar_alumnos()

    print("\nGrupo de alumnos dentro de Alumno1 después de editar:")
    alumno1.mostrar_grupo()
