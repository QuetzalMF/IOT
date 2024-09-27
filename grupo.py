from alumno import Alumno
from lista import Lista

class Grupo(Lista):
    def __init__(self, grado=None, seccion=None): 
        self.grado = grado
        self.seccion = seccion

    def add_alumno(self, alumno):
        self.add(alumno) 

    def get_alumnos(self):
        return self.get_all() 

    def __repr__(self):
        return f"Grupo: {self.grado} {self.seccion}"

if __name__ == "__main__":

    lista_grupos = Lista()

    grupo1 = Grupo("7/", "A")
    grupo1.add_alumno(Alumno("Diego", "Mercado", "Franco", "01", "701"))
    grupo1.add_alumno(Alumno("Diego", "Franco", "Mercado", "02", "702"))
    grupo1.add_alumno(grupo1)
    
    grupo2 = Grupo("7/", "B")
    grupo2.add_alumno(Alumno("Samuel", "López", "Rodriguez", "03", "703"))
    lista_grupos.add(grupo2)

    grupo3 = Grupo("7/", "C")
    grupo3.add_alumno(Alumno("Cristal", "Carrillo", "Guerrero", "04", "704"))
    lista_grupos.add(grupo3)

    for grupo in lista_grupos.get_all():
        print(grupo)
        for alumno in grupo.get_alumnos():
            print(f"{alumno}")