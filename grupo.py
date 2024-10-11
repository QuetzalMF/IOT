import json
from alumnos import Alumno
from lista import Lista  

class Grupo(Lista):
    def __init__(self, grado=None, seccion=None):
        if (grado==None and seccion==None):
            super().__init__()
            self.isLista = True
        else:
            self.grado = grado
            self.seccion = seccion
            self.alumnos = Alumno()
            self.isLista = False
            
    def addAlumno(self, alumno):
        self.alumnos.add(alumno)
        
    def get_alumnos(self):  # Método que necesitas
        return self.alumnos.lista  # Devuelve la lista de alumnos    

    def __str__(self):
        if self.isLista:
            return f"Tienes {len(self.lista)} Alumnos"
        else:
            return f"{self.grado} {self.seccion}"
        
         #metodo donde me lo regrese como diccionario si es una lista ...
    def getDic(self):
        if not self.isLista:
            return {
                "grado": self.grado,
                "seccion": self.seccion,
                "alumnos": [alumno.getDic() for alumno in self.alumnos.lista] 
            }
        else:
            # Return a list of dictionaries if it's a list of Alumno objects
            return [a.getDic() for a in self.lista]
        
    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.getDic(), f, indent=4)    
    
     
    #..................................................                   
    # Método para leer el archivo JSON y devolver la data
    def read_json(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)
    # Método para cargar los datos leídos y convertirlos en objetos Alumno
    def load_from_data(self, data):
        for grupo_data in data:
                grupo = Grupo(
                    grupo_data['grado'],
                    grupo_data['seccion']
                )
        for alumno_data in grupo_data['alumnos']:   
                alumno = Alumno(
                    alumno_data['matricula'],
                    alumno_data['nombre'],
                    alumno_data['ap_paterno'],
                    alumno_data['ap_materno'],
                    alumno_data['curp']
                ) 
                grupo.addAlumno(alumno)
        self.add(grupo)   
    #..................................................                     
    
            
if __name__ == "__main__":
    alumno1 = Alumno("Diego", "Mercado", "Franco", "01", "701")
    alumno2 = Alumno("Diego", "Franco", "Mercado", "02", "702")
    grupo1 = Grupo("Grupo", "A")
    grupo2 = Grupo("Grupo", "B")
    print(grupo1)
    print(grupo2)
   
    grupo1.addAlumno(alumno1)
    grupo2.addAlumno(alumno2)
    
    lista_grupos = Grupo()  
    lista_grupos.add(grupo1)
    lista_grupos.add(grupo2)
    
    print(lista_grupos)
    
    # Convert the data to dictionary/JSON format
    print(lista_grupos.getDic())
    lista_grupos.save_to_json("lista_grupo.json")
    
    
    #..................................................            
    #crear la instancia......
    load_lista = Grupo()
    # Leer los datos del archivo JSON
    data = load_lista.read_json("lista_grupo.json")
    # Cargar los datos leídos en la lista de objetos Alumno
    load_lista.load_from_data(data)
    for grupo in load_lista.lista:
        print(grupo)
    #..................................................                
    
    # 1 paso: conventir toda la salida de informacion a Json
    # Cuando regrese la cadena de datos que regrese como arreglo me lo convierta en Json o Diccionario
    # Grupo