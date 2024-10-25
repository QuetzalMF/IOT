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
            return f"Tienes {len(self.lista)} alumnos"
        else:
            return f"{self.nombre} {self.ap_materno} {self.ap_paterno} {self.curp} {self.matricula}"
    
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

    def read_json(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)

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
            
