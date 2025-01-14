# Proyecto PEC4

Este proyecto es una solución a los ejercicios de la PEC4 de Programación para la Ciencia de Datos. Consiste en analizar los datos de participantes de la carrera ciclista Orbea Monegros 2024, y generar diferentes estadísticas y reportes mediante módulos separados.

## Estructura del Proyecto

- **`main.py`**: Archivo principal del menú de los ejercicios.
- **`run_tests.py`**: Archivo principal del menú de tests.
- **`LICENSE`**: Licencia de uso y distribución.
- **`requirements.txt`**: Instalación automática de las librerías necesarias.
- **`README.md`**: Este archivo de proyecto que estás leyendo, en formato [MarkDown](https://markdown.es).
- **`src/`**: Carpeta que contiene los módulos de los ejercicios.
- **`tests/`**: Carpeta con los módulos de tests.
- **`data/`**: Carpeta con el dataset original.
- **`dataframes/`**: Carpeta para el guardado de los dataframes manipulados.
- **`img/`**: Carpeta para guardar el histograma.

Además, todo el proyecto está escrito en Python, por lo que debes asegurarte de tener instalado el framework: [Página oficial](https://www.python.org/downloads/).  
También tienes unos potentes [recursos de Python](https://es.python.org/aprende-python/). 

## Uso

### 1. Descargar y configurar el Proyecto
Ejecuta  en tu terminal lo siguiente para clonar el repositorio:  
```
git clone https://github.com/david-jimenez-vicente/Data_Science_Programming-PEC4.git
```  
Y con esto vamos a la carpeta del repositorio clonado:  
```
cd ./Data_Science_Programming-PEC4
```  

Se aconseja crear un entorno virtual para este proyecto:  
```
python3 -m venv pec4
```  
Mac/Linux:  
```
source pec4/bin/activate
```  
Windows:  
```
pec4\Scripts\activate
```  

Para eliminar el entorno, símplemente desactiva el entorno...:  
```
deactivate
```  
... y borrar la carpeta que se ha creado del entorno en el directorio del proyecto.

### 2. Ejecutar el Proyecto  

Una vez en el directorio local del proyecto, hay 2 maneras de usar el programa: Apertura manual (sin instalación), o instalación en el sistema.  

- Opción 1. Ejecutarlo sin instalar:  
    - a) Este proyecto utiliza Python y varias librerías. Para instalarla ejecuta:  
        ```
        pip install -r requirements.txt
        ```  
    - b) Luego ejecuta el programa principal:  
      ```
      python3 main.py
      ```   
      
- Opción 2. Instalarlo en el sistema:  
  De esta manera conseguirás ejecutarlo con un simple comando del terminal desde cualquier lugar, sin tener que acudir a la carpeta donde está el proyecto. Se puede desinstalar después:
  - Estando en el directorio del repositorio clonado, ejecuta:  
  ```
  pip install .
  ```
  - Después puedes ejecutarlo desde el terminal estés en la carpeta que estés con esto:  
  ```
  pec4
  ```  
  - Para **desinstalarlo** usa esto:  
  ```
  pip uninstall pec4
  ```  

## Cómo Funciona
### Menú
Al abrir el programa, verás el menú de ejecución. Permite ejecutar todos los ejercicios o seleccionarlos individualmente.    

   - Opción `1`: Ejecuta todos los ejercicios secuencialmente con sus tests.
   - Opción `2`: Menú para ejecutar los ejercicios uno a uno.
   - Opción `0`: Salir del programa.

## Tests de ejecución
En la carpeta `tests/` se incluye un módulo de test para cada módulo de ejercicio.  
Para los test se ha usado la librería `pytest`, y se ha añadido el plugin de pytest `pytest-cov`, que revisa la cobertura de las pruebas al ejecutar cada test. La cobertura de un test es el % de líneas de código que se han ejecutado en la prueba del script testeado.  
Al ejecutarse, `pytest` realiza una batería de pruebas predefinidas con condiciones que deben cumplirse. Cuantas más situaciones posibles preveas para las pruebas, mayor cobertura tendrá el test.  
El resultado será un listado con el progreso del test. En verde aparecerá todo lo correcto, y si hay errores en la ejecución de las pruebas, se verán en rojo, para poder localizar el código a corregir más fácilmente.  
  
Cada módulo de ejercicios tiene su nmódulo de tests.  
  
Hay dos formas de ejecutar los tests:

1. Ejecutar el sistema de tests interactivo con el menú:  
```
python3 run_tests.py
```  
Este script permite:
  - Ejecutar todos los tests de una sola vez y ver la cobertura total.
  - Ejecutar tests ejercicio por ejercicio y ver la cobertura individual.  
  - Obtener los prompts de terminal para correr los tests individualmente a mano sin pasar por el menú.

2. Por si no deseas ejecutar el programa de los tests, aquí tienes los comandos de tests individuales para terminal:  
```
pytest tests/test1.py -v --cov=src.ejer1 --cov-report=term-missing
```
```
pytest tests/test2.py -v --cov=src.ejer2 --cov-report=term-missing
```
```
pytest tests/test3.py -v --cov=src.ejer3 --cov-report=term-missing
```
```
pytest tests/test4.py -v --cov=src.ejer4 --cov-report=term-missing
```
```
pytest tests/test5.py -v --cov=src.ejer5 --cov-report=term-missing
```  
  
## Test de estilo con linter
Un linter es una guía interactiva de estilo para adaptar el código a una de las normas PEP, en este caso PEP20.  
El linter usado es `pylint`.  
La ejecución de los evaluadores devolverá una puntuación sobre 10 de todo lo que ha evaluado como un conjunto. Sólo muestra los posibles inconvenientes de estilo encontrados y dónde localizarlos, y la nota final. Cuanto más corto el resultado del test, mejor ;). Todo archivo al que no haga referencia la salida, es que no tiene avisos.  
Para ejecutarlo, se sigue el formato de comando:  

```
pylint <archivo a testear>.<extensión>
```

Para correr el evaluador pylint en todos los archivos .py de la carpeta actual, usa lo siguiente (siempre estando en la carpeta donde has descargado el proyecto): 
  
```
pylint *.py
```  
Si quieres hacer el test sobre toda la carpeta de `src/` escribe:  

```
pylint ./src/*.py
```  
Si quieres hacer el test sobre toda la carpeta de `tests/` escribe:  

```
pylint ./tests/*.py
```  

## Notas Adicionales

* Si encuentras algún error en los datos o el código, verifica que el archivo `dataset.csv` esté correctamente ubicado en la arpeta "data" y que las dependencias estén instaladas en la carpeta "src". 
* Para soporte adicional, contacta al administrador del proyecto.  
* Se distribuye bajo licencia MIT. Puedes comprobarlo en el archivo `LICENSE`

## Información sobre librerías usadas

* faker: [https://faker.readthedocs.io/en/master/](https://faker.readthedocs.io/en/master/)
* pandas: [https://pandas.pydata.org/docs/user_guide/index.html](https://pandas.pydata.org/docs/user_guide/index.html)
* numpy: [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
* matplotlib: [https://matplotlib.org](https://matplotlib.org)
* pytest: [https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)
* pytest-cov: [https://pypi.org/project/pytest-cov/](https://pypi.org/project/pytest-cov/)
* pylint: [https://pypi.org/project/pylint/](https://pypi.org/project/pylint/)
* setuptools: [https://pypi.org/project/setuptools/](https://pypi.org/project/setuptools/)