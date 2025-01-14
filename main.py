"""
Archivo principal de ejecución del programa de la PEC4
Su función principal es preguntar al usuario cómo quiere realizar los ejercicios
a través de un menú, y llamar a las funciones ejecutoras .run() de cada módulo
de ejercicio.
"""
from src import ejer1, ejer2, ejer3, ejer4, ejer5

def run_all():
    """Ejecuta todos los ejercicios en orden"""
    print("\nEjecutando todos los ejercicios...\n")
    print("\n=== Ejercicio 1: Importación del dataset y EDA ===\n")
    ejer1.run()
    print("\n=== Ejercicio 2: Anonimización y limpieza ===\n")
    ejer2.run()
    print("\n=== Ejercicio 3: Agrupamiento de minutos e histograma ===\n")
    ejer3.run()
    print("\n=== Ejercicio 4: Análisis de clubs ===\n")
    ejer4.run()
    print("\n=== Ejercicio 5: Análisis UCSC ===\n")
    ejer5.run()

def run_ejer(num):
    """\nEjecuta un ejercicio específico\n"""
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
    """Menú de ejecución del programa"""
    print("\n\n\n\n\n\n············Análisis de datos Orbea Monegros 2024··············\n")

    while True:  # Bucle principal para el menú
        # Mostrar el menú principal
        print("========================================")
        print("Menú principal:")
        print("1. Ejecutar todos los ejercicios")
        print("2. Ejecutar ejercicios uno a uno")
        print("0. Salir del programa")
        print("========================================")

        # Capturar la opción del usuario
        option = input("Seleccione una opción (0-2): ")

        if option == "0":
            print("Saliendo del programa.")
            break
        if option == "1":
            run_all()
        elif option == "2":
            while True:  # Bucle interno para los ejercicios
                print("\n\n\n\n\n\n========================================")
                print("Ejercicios disponibles:")
                print("1. Importación y EDA")
                print("2. Anonimización y limpieza")
                print("3. Agrupamiento e histograma")
                print("4. Análisis de clubs")
                print("5. Análisis UCSC")
                print("0. Salir")
                print("========================================")

                ejer = input("\nSeleccione ejercicio (0-5): ")
                if ejer == "0":
                    break
                try:
                    run_ejer(int(ejer))
                except ValueError:
                    print("Opción no válida")
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
