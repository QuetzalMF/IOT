from alumnos import Alumno
from grupo import Grupo
from lista import Lista

class Carrera(Lista):
    def __init__(self, nombre=None, clave=None):
        self.nombre = nombre
        self.clave = clave

    def add_grupo(self, grupo):
        self.add(grupo)

    def edit_grupo(self, idx, grupo):
        self.edit(idx, grupo)

    def get_grupos(self):
        return self.get_all()

    def __repr__(self):
        return f'{self.nombre}, {self.clave}'

if __name__ == "__main__":
    lista_carreras = Lista()

    carrera1 = Carrera("Sistemas", "222")
    grupo1 = Grupo("7/", "A")
    grupo1.add_alumno(Alumno("Diego", "Mercado", "Franco", "01", "701"))
    grupo1.add_alumno(Alumno("Diego", "Franco", "Mercado", "02", "702"))
    carrera1.add_grupo(grupo1)

    grupo2 = Grupo("7/", "B")
    grupo2.add_alumno(Alumno("Samuel", "López", "Rodriguez", "03", "703"))
    carrera1.add_grupo(grupo2)

    lista_carreras.add(carrera1)

    carrera2 = Carrera("Electronica", "223")
    grupo3 = Grupo("7/", "C")
    grupo3.add_alumno(Alumno("Cristal", "Carrillo", "Guerrero", "04", "704"))
    carrera2.add_grupo(grupo3)

    lista_carreras.add(carrera2)

    for carrera in lista_carreras.get_all():
        print(carrera)
        for grupo in carrera.get_grupos():
            print(f"  {grupo}")
            for alumno in grupo.get_alumnos():
                print(f"    {alumno}")