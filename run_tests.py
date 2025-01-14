"""
Script de lanzamiento de los tests. Se puede usar como medio centralizado
para los tests, o se puede ejecutar cada uno desde la carpeta tests/
"""
import os
from pathlib import Path
import pytest

def get_project_root():
    """Obtiene la ruta raíz del proyecto"""
    return str(Path(__file__).parent)

def run_single_test(test_file):
    """
    Ejecuta los tests de un solo archivo y muestra su cobertura
    Args:
        test_file (str): Nombre del archivo de test
    """
    module = test_file.replace('test', '').replace('.py', '')
    print(f"\n=== Ejecutando tests para ejercicio {module} ===")

    # Configurar argumentos para pytest
    args = [
        os.path.join('tests', test_file),
        '-v',
        f'--cov=src.ejer{module}',  # Cobertura específica del módulo
        '--cov-report=term-missing',
        '--import-mode=importlib'
    ]

    # Ejecutar tests
    pytest.main(args)

def run_all_tests():
    """Ejecuta todos los tests y muestra la cobertura total"""
    print("\n=== Ejecutando todos los tests ===")

    # Obtener la lista de archivos de test
    project_root = get_project_root()
    tests_dir = os.path.join(project_root, 'tests')
    test_files = sorted([
        os.path.join('tests', f)
        for f in os.listdir(tests_dir)
        if f.startswith('test') and f.endswith('.py') and f[4].isdigit()
    ])

    # Configurar argumentos para pytest
    args = test_files + [
        '-v',
        '--cov=src',
        '--cov-report=term-missing',
        '--import-mode=importlib'
    ]

    # Ejecutar tests
    pytest.main(args)

def main():
    '''Ejecución principal del menú'''
    project_root = get_project_root()
    tests_dir = os.path.join(project_root, 'tests')

    if not os.path.exists(tests_dir):
        print(f"Error: No se encuentra el directorio de tests en {tests_dir}")
        return

    test_files = sorted([f for f in os.listdir(tests_dir)
                        if f.startswith('test') and f.endswith('.py') and f[4].isdigit()])

    if not test_files:
        print("Error: No se encontraron archivos de test")
        return

    print("\nSistema de ejecución de tests")
    print("1. Ejecutar todos los tests")
    print("2. Ejecutar tests uno a uno")
    print("3. Ver comandos para generar informes de coverage")

    option = input("\nSeleccione una opción (1-3): ")

    if option == "1":
        run_all_tests()
    elif option == "2":
        while True:
            print("\nTests disponibles:")
            for i, test_file in enumerate(test_files, 1):
                module = test_file.replace('test', '').replace('.py', '')
                print(f"{i}. Tests ejercicio {module}")
            print("0. Salir")

            try:
                test_num = int(input("\nSeleccione ejercicio (0-5): "))
                if test_num == 0:
                    break
                if 1 <= test_num <= len(test_files):
                    run_single_test(test_files[test_num-1])
                else:
                    print("Opción no válida")
            except ValueError:
                print("Por favor, introduzca un número válido")
    elif option == "3":
        print("\nPara generar informes de coverage, use estos comandos desde el terminal:")
        print("\nTests individuales:")
        for test_file in test_files:
            module = test_file.replace('test', '').replace('.py', '')
            print(f"pytest tests/{test_file} -v --cov=src.ejer{module} --cov-report=term-missing")
        print("\nTodos los tests:")
        print("pytest tests/ -v --cov=src --cov-report=term-missing")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
