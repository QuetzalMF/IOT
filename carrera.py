import json
from alumnos import Alumno
from grupo import Grupo
from lista import Lista

class Carrera(Lista):
    def __init__(self, nombre=None, clave=None):
        if nombre is None and clave is None:
            super().__init__()
            self.isLista = True
        else:
            self.nombre = nombre
            self.clave = clave
            self.grupos = Grupo() 
            self.isLista = False

    def add_grupo(self, grupo):
            self.grupos.add(grupo)

    def get_grupos(self):
            return self.grupos.lista 

    def __repr__(self):
        if self.isLista:
            return f"Tienes {len(self.lista)} carreras"
        else:
            return f"{self.nombre}, {self.clave}"

    def getDic(self):
        if not self.isLista:
            return {
                "nombre": self.nombre,
                "clave": self.clave,
                "grupos": [grupo.getDic() for grupo in self.grupos.lista]
            }
        else:
            return [carrera.getDic() for carrera in self.lista]    
        
    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.getDic(), f, indent=4)
            
    # crear lista (Alumno)
    # creo alumnos 
    # Agrego alumno a lista
    # convertir lista a diccionario
    # Guardar Archivo
    
    # Leer Archivo 
    # Convertir el diccionario a una lista(Alumno) --- Guardar en el objeto de Alumno.lista
     # Crear objeto tipo alumno-lista // deberia estar guardando alumnos, arreglo de diccionarios
     # Recorrer lista de diccionarios
     # Convertir Diccionario en objeto alumno
     # Agregar Alumno a Alumno.Lista
     
     
if __name__ == "__main__":
    alumno1 = Alumno("Diego", "Mercado", "Franco", "01", "701")
    alumno2 = Alumno("Diego", "Franco", "Mercado", "02", "702")

    grupo1 = Grupo("1", "A")
    grupo2 = Grupo("2", "B")
    grupo1.addAlumno(alumno1)
    grupo2.addAlumno(alumno2)

    carrera1 = Carrera("Ingenieria Sistemas", "TICS")
    carrera2 = Carrera("Ingenieria Quimica", "IG")

    carrera1.add_grupo(grupo1)
    carrera2.add_grupo(grupo2)

    lista_carreras = Carrera()  
    lista_carreras.add(carrera1)  
    lista_carreras.add(carrera2)

    print(carrera1.getDic()) 
    print(carrera2.getDic()) 
    #print(lista_carreras.getDic())  
    print(lista_carreras)
    lista_carreras.save_to_json("lista_carreras.json")