"""
Archivo principal de ejecución del programa de la PEC4
Su función principal es preguntar al usuario cómo quiere realizar los ejercicios
a través de un menú, y llamar a las funciones ejecutoras .run() de cada módulo
de ejercicio.
"""
from src import ejer1, ejer2, ejer3, ejer4, ejer5

def run_all():
    """Ejecuta todos los ejercicios en orden"""
    print("Ejecutando todos los ejercicios...")
    ejer1.run()
    ejer2.run()
    ejer3.run()
    ejer4.run()
    ejer5.run()

def run_ejer(num):
    """Ejecuta un ejercicio específico"""
    ejers = {
        1: ejer1.run,
        2: ejer2.run,
        3: ejer3.run,
        4: ejer4.run,
        5: ejer5.run
    }
    if num in ejers:
        ejers[num]()
    else:
        print(f"No existe el ejercicio {num}")

def main():
    print("Análisis de datos Orbea Monegros 2024")
    print("1. Ejecutar todos los ejercicios")
    print("2. Ejecutar ejercicios uno a uno")
    print("0. Salir del programa")

    option = input("Seleccione una opción (1-2): ")

    if option == "1":
        run_all()
    elif option == "2":
        while True:
            print("\nEjercicios disponibles:")
            print("1. Importación y EDA")
            print("2. Anonimización y limpieza")
            print("3. Agrupamiento e histograma")
            print("4. Análisis de clubs")
            print("5. Análisis UCSC")
            print("0. Salir")

            ejer = input("\nSeleccione ejercicio (0-5): ")
            if ejer == "0":
                break
            try:
                run_ejer(int(ejer))
            except ValueError:
                print("Opción no válida")
    elif option == "0":
        break
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
