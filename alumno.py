from lista import Lista  

class Alumno(Lista):
    def _init_(self, nombre=None, ap_materno=None, ap_paterno=None, curp=None, matricula=None):
        self.nombre = nombre
        self.ap_materno = ap_materno
        self.ap_paterno = ap_paterno
        self.curp = curp
        self.matricula = matricula

    def _repr_(self):
        return f"{self.nombre} {self.ap_materno} {self.ap_paterno} {self.matricula}"


if __name__ == "__main__":
    alumno1 = Alumno("Miguel", "Castro", "Mesta", "0001", "A0001")
    alumno2 = Alumno("Gabriela", "Zamora", "Hernandez", "0002", "A0002")

    lista_alumnos = Alumno()  
    lista_alumnos.add(alumno1)
    lista_alumnos.add(alumno2)

    print(lista_alumnos)