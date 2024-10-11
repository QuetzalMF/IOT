import json
from lista import Lista  

class Alumno(Lista):
    def __init__(self, nombre=None, ap_materno=None, ap_paterno=None, curp=None, matricula=None):
        if (matricula==None and nombre==None):
             #detectar mediante los datos que estemos mandando si son mas de varios (arreglo) / si es uno es (objeto)
            super().__init__()
            self.isLista = True
        else:
            self.nombre = nombre
            self.ap_materno = ap_materno
            self.ap_paterno = ap_paterno
            self.curp = curp
            self.matricula = matricula
            self.isLista = False

    def __str__(self):
        if self.isLista:
            #return f"{self.nombre} {self.ap_materno} {self.ap_paterno} {self.matricula}"
            return f"Tienes {len(self.lista)} alumnos"
        else:
            return f"{self.nombre}{self.matricula}"   
        
     #metodo donde me lo regrese como diccionario si es una lista ...
    def getDic(self):
        if not self.isLista:
            return {
                "matricula": self.matricula,
                "nombre": self.nombre,
                "ap_materno": self.ap_materno,
                "ap_paterno": self.ap_paterno,
                "curp": self.curp
            }
        else:    
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
        for alumno_data in data:
            alumno = Alumno(
                alumno_data['nombre'],
                alumno_data['ap_materno'],
                alumno_data['ap_paterno'],
                alumno_data['curp'],
                alumno_data['matricula']
            )
            self.add(alumno)  
    #..................................................                         
   


if __name__ == "__main__":
    alumno1 = Alumno("Diego", "Mercado", "Franco", "01", "701")
    alumno2 = Alumno("Diego", "Franco", "Mercado", "02", "702")
    print(alumno1)
    print(alumno2)
    
    lista_alumnos = Alumno()  
    lista_alumnos.add(alumno1)
    lista_alumnos.add(alumno2)
    print(lista_alumnos)
    
    
    #meter ident o identacion al diccionario
    print(lista_alumnos.getDic())
    lista_alumnos.save_to_json("lista_alumnos.json")
    
    #..................................................            
    #crear la instancia......
    load_lista = Alumno()

    # Leer los datos del archivo JSON
    data = load_lista.read_json("lista_alumnos.json")
    
    # Cargar los datos leídos en la lista de objetos Alumno
    load_lista.load_from_data(data)
    
    for alumno in load_lista.lista:
        print(alumno)
    #..................................................                
            
    # Leer Archivo 
    # Convertir el diccionario a una lista(Alumno) --- Guardar en el objeto de Alumno.lista
    # Crear objeto tipo alumno-lista // deberia estar guardando alumnos, arreglo de diccionarios
    # Recorrer lista de diccionarios
    # Convertir Diccionario en objeto alumno
    # Agregar Alumno a Alumno.Lista