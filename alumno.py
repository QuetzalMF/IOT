from lista import Lista  

class Alumno(Lista):
    def __init__(self, nombre=None, ap_materno=None, ap_paterno=None, curp=None, matricula=None):
        self.nombre = nombre
        self.ap_materno = ap_materno
        self.ap_paterno = ap_paterno
        self.curp = curp
        self.matricula = matricula

    def __repr__(self):
        return f"{self.nombre} {self.ap_materno} {self.ap_paterno} {self.matricula}"


if __name__ == "__main__":
    alumno1 = Alumno("Diego", "Mercado", "Franco", "01", "701")
    alumno2 = Alumno("Diego", "Franco", "Mercado", "02", "702")

    lista_alumnos = Alumno()  
    lista_alumnos.add(alumno1)
    lista_alumnos.add(alumno2)

    print(lista_alumnos)
    
#........
#class Alumno:
    def __init__(self, nombre=None, ap_materno=None, ap_paterno=None, curp=None, matricula=None):
        self.nombre = nombre
        self.ap_materno = ap_materno
        self.ap_paterno = ap_paterno
        self.curp = curp
        self.matricula = matricula

    def __repr__(self):
        return f"{self.nombre} {self.ap_materno} {self.ap_paterno} {self.matricula}"


#if __name__ == "__main__":
    alumno1 = Alumno("Diego", "Mercado", "Franco", "01", "701")
    alumno2 = Alumno("Diego", "Franco", "Mercado", "02", "702")

    lista_alumnos = Lista()  # Create an instance of Lista
    lista_alumnos.add(alumno1)
    lista_alumnos.add(alumno2)

    print(lista_alumnos.get_all()) 