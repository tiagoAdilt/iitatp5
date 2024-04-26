class Escuela:
    def __init__(self):
        self.datos = {"Alumnos": []}

    def mostrar_datos_alumnos(self):
        print("Datos de los alumnos:")
        for i, alumno in enumerate(self.datos["Alumnos"], 1):
            print(f"\nAlumno {i}:")
            for clave, valor in alumno.items():
                print(f"{clave}: {valor}")

    def modificar_datos_alumno(self, indice):
        alumno = self.datos["Alumnos"][indice]
        print(f"Modificando datos del alumno {indice + 1}:")
        for clave, valor in alumno.items():
            nuevo_valor = input(f"Ingrese el nuevo valor para {clave} (actual: {valor}): ")
            if nuevo_valor:
                alumno[clave] = nuevo_valor

    def agregar_alumno(self, nombre, apellido, dni, fecha_nacimiento, tutor, notas=[], faltas=0, amonestaciones=0):
        nuevo_alumno = {
            "Nombre": nombre,
            "Apellido": apellido,
            "DNI": dni,
            "Fecha de nacimiento": fecha_nacimiento,
            "Tutor": tutor,
            "Notas": notas,
            "Faltas": faltas,
            "amonestaciones": amonestaciones
        }
        self.datos["Alumnos"].append(nuevo_alumno)


# Función principal para el menú
def menu():
    escuela = Escuela()
    
    # Agregar algunos alumnos de ejemplo
    escuela.agregar_alumno("Juan", "Pérez", "12345678", "01/01/2005", "María García")
    escuela.agregar_alumno("Ana", "López", "87654321", "15/05/2006", "Pedro Rodríguez", notas=[9, 8, 7], faltas=2, amonestaciones=1)
    escuela.agregar_alumno("Carlos", "González", "45678901", "10/10/2004", "Laura Martínez")

    while True:
        print("\nMenú:")
        print("a) Mostrar datos de todos los alumnos")
        print("b) Modificar datos de un alumno")
        print("c) Agregar un nuevo alumno")
        print("d) Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "a":
            escuela.mostrar_datos_alumnos()
        elif opcion == "b":
            indice = int(input("Ingrese el índice del alumno que desea modificar: ")) - 1
            escuela.modificar_datos_alumno(indice)
        elif opcion == "c":
            nombre = input("Nombre del nuevo alumno: ")
            apellido = input("Apellido del nuevo alumno: ")
            dni = input("DNI del nuevo alumno: ")
            fecha_nacimiento = input("Fecha de nacimiento del nuevo alumno (formato dd/mm/aaaa): ")
            tutor = input("Nombre y apellido del tutor del nuevo alumno: ")
            escuela.agregar_alumno(nombre, apellido, dni, fecha_nacimiento, tutor)
        elif opcion == "d":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    menu()

