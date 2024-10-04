from alumnos import Alumno
from lista import Lista  

class Grupo(Lista):
    def __init__(self, grado=None, seccion=None):
        if (grado==None and seccion==None):
            super().__init__()
        else:
            self.grado = grado
            self.seccion = seccion
            self.alumnos = Alumno()
            self.isLista = False
            
    def addAlumno(self, alumno):
        self.alumnos.add(alumno)

    def __str__(self):
        if self.isLista:
            return f"Tienes (len({self.isLista})) Alumnos"
        else:
            return f"{self.grado} {self.seccion}"
    
            
if __name__ == "__main__":
    alumno1 = Alumno("Diego", "Mercado", "Franco", "01", "701")
    alumno2 = Alumno("Diego", "Franco", "Mercado", "02", "702")
    grupo1 = Alumno("hola", "01")
    grupo2 = Alumno("hola2", "02")
    print(grupo1)
    print(grupo2)

    lista_grupos = Grupo()  
    grupo1.add(alumno1)
    grupo2.add(alumno2)
    lista_grupos.add(grupo1)
    lista_grupos.add(grupo2)
    
    print(lista_grupos)
    
    # 1 paso: conventir toda la salida de informacion a Json
    # Cuando regrese la cadena de datos que regrese como arreglo me lo convierta en Json o Diccionario
    # Grupo