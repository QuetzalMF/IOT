from alumnos import Alumno

# guardar todo en una clase, no debe heredar de nadie
# cargar el archivo json desde el momento de correr el archivo, asi mismo guardarlos en el archivo

# hacer lo mismo para grupo y carrera
# deberiamos cargar en Grupo.py mandar llamar los metodos, metodos para Grupos
class interfaz():
    def view_alumnos(lista_alumnos):
        if len(lista_alumnos.lista) > 0:
            for i, alumno in enumerate(lista_alumnos.lista):
                print(f"{i + 1}. {alumno}")
        else:
            print("No hay alumnos en la lista.")

    def add_alumno(lista_alumnos):
        nombre = input("Nombre: ")
        ap_materno = input("Apellido Materno: ")
        ap_paterno = input("Apellido Paterno: ")
        curp = input("CURP: ")
        matricula = input("Matrícula: ")
        nuevo_alumno = Alumno(nombre, ap_materno, ap_paterno, curp, matricula)
        lista_alumnos.add(nuevo_alumno)
        print(f"Alumno {nombre} agregado correctamente.")

    def edit_alumno(lista_alumnos):
        indice = int(input("Número del alumno a editar: ")) - 1
        if 0 <= indice < len(lista_alumnos.lista):
            nombre = input("Nuevo Nombre: ")
            ap_materno = input("Nuevo Apellido Materno: ")
            ap_paterno = input("Nuevo Apellido Paterno: ")
            curp = input("Nuevo CURP: ")
            matricula = input("Nueva Matrícula: ")
            lista_alumnos.edit(indice, Alumno(nombre, ap_materno, ap_paterno, curp, matricula))
            print("Alumno editado correctamente.")
        else:
            print("Índice fuera de rango.")

    def remove_alumno(lista_alumnos):
        indice = int(input("Número del alumno a eliminar: ")) - 1
        if 0 <= indice < len(lista_alumnos.lista):
            lista_alumnos.remove(lista_alumnos.lista[indice])
            print("Alumno eliminado correctamente.")
        else:
            print("Índice fuera de rango.")

    def save_alumnos(lista_alumnos):
        filename = input("Nombre del archivo (incluye .json): ")
        lista_alumnos.save_to_json(filename)
        print(f"Lista guardada en {filename}.")

# podemos cargar el arreglo desde el principio
    def load_alumnos(lista_alumnos):
        filename = input("Nombre del archivo (incluye .json): ")
        data = lista_alumnos.read_json(filename)
        lista_alumnos.load_from_data(data)
        print("Lista cargada correctamente.")

def menu():
    lista_alumnos = Alumno()
    while True:
        print("\n--- Menu ---")
        print("1. Ver lista de alumnos")
        print("2. Agregar alumno")
        print("3. Editar alumno")
        print("4. Eliminar alumno")
        print("5. Guardar lista en archivo JSON")
        print("6. Cargar lista desde archivo JSON")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            interfaz.view_alumnos(lista_alumnos)
        elif opcion == "2":
            interfaz.add_alumno(lista_alumnos)
        elif opcion == "3":
            interfaz.edit_alumno(lista_alumnos)
        elif opcion == "4":
            interfaz.remove_alumno(lista_alumnos)
        elif opcion == "5":
            interfaz.save_alumnos(lista_alumnos)
        elif opcion == "6":
            interfaz.load_alumnos(lista_alumnos)
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()