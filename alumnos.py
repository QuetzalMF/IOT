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
            return f"Tienes (len({self.lista})) Alumnos"
        else:
            return f"{self.nombre}{self.matricula}"
        
     #metodo donde me lo regrese como diccionario si es una lista ...
    def getDic(self):
        if not self.isLista:
            return {
                "matricula": self.matricula,
                "nombre": self.nombre
            }
        else:
            # Return a list of dictionaries if it's a list of Alumno objects
            return [a.getDic() for a in self.lista]


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