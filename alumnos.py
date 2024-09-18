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

    # def editar_datos(self, nombre=None, apaterno=None, amaterno=None, curp=None, matricula=None):
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


if __name__ == "__main__":
    alumno1 = Alumno("Juan", "Pérez", "García", "CURP123", "M123")
    print("Alumno original:")
    print(alumno1)

    # Editar datos del alumno
    # alumno1.editar_datos(nombre="Juanito", curp="CURP987")
    # print("\nAlumno después de editar:")
    # print(alumno1)

    # Exportar datos del alumno
    datos_alumno1 = alumno1.exportar()
    print("\nDatos exportados del alumno:")
    print(datos_alumno1)

    # Eliminar datos del alumno
    alumno1.eliminar_datos()
    print("\nAlumno después de eliminar:")
    print(alumno1)

#crear un arreglo que muestre los datos del alumno y asi mismo al crear el metodo de editar sea al arreglo mas no a las clases
#quitar el exportar
#quitar si hay matricula
