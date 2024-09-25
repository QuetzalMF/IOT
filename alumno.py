class Alumno:
    def __init__(self, entrada, apaterno=None, amaterno=None, curp=None, matricula=None):
        """Verifica si se le pasa un array de alumnos o un solo alumno."""
        if isinstance(entrada, list):
            # Modo array
            self.array_mode = True
            self.alumnos = entrada  # entrada es una lista de objetos Alumno
        else:
            # Modo objeto
            self.array_mode = False
            self.nombre = entrada
            self.apaterno = apaterno
            self.amaterno = amaterno
            self.curp = curp  
            self.matricula = matricula  

    def __str__(self):
        if self.array_mode:
            return f"Alumno en modo array con {len(self.alumnos)} alumnos"
        curp_str = self.curp if self.curp else "CURP no disponible"
        matricula_str = self.matricula if self.matricula else "Matrícula no disponible"
        return f'{self.nombre} {self.apaterno} {self.amaterno} - {curp_str} - {matricula_str}'

    def __repr__(self):
        if self.array_mode:
            return f"Alumno en modo array con {len(self.alumnos)} alumnos"
        return f"Alumno(nombre='{self.nombre}', apaterno='{self.apaterno}', amaterno='{self.amaterno}', curp='{self.curp}', matricula='{self.matricula}')"

    def agregar(self, alumno):
        """Agrega un alumno al arreglo si está en modo array"""
        if self.array_mode:
            self.alumnos.append(alumno)

    def eliminar(self, index):
        """Elimina un alumno del arreglo si está en modo array"""
        if self.array_mode and 0 <= index < len(self.alumnos):
            del self.alumnos[index]

    def editar(self, nombre=None, apaterno=None, amaterno=None, curp=None, matricula=None):
        """Edita los datos del alumno si no está en modo array"""
        if not self.array_mode:
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
        """Elimina (resetea) los datos del alumno si no está en modo array"""
        if not self.array_mode:
            self.nombre = None
            self.apaterno = None
            self.amaterno = None
            self.curp = None
            self.matricula = None

    def exportar(self):
        """Exporta los datos del alumno o de la lista de alumnos si está en modo array"""
        if self.array_mode:
            return [alumno.exportar() for alumno in self.alumnos]
        return {
            'nombre': self.nombre,
            'apaterno': self.apaterno,
            'amaterno': self.amaterno,
            'curp': self.curp,
            'matricula': self.matricula
        }

# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunos alumnos como objetos
    alumno1 = Alumno("Juan", "Pérez", "García", "CURP123", "M123")
    alumno2 = Alumno("Ana", "López", "Martínez", "CURP456", "M456")

    # Alumno en modo array
    lista_alumnos = [alumno1, alumno2]
    alumno_array = Alumno(lista_alumnos)  # Modo array
    print("\nAlumno en modo array:")
    print(alumno_array)
    print("Alumnos dentro del array:")
    print(alumno_array.exportar())
