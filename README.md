# Proyecto PEC4

Este proyecto es una solución a los ejercicios de la PEC4 de Programación para la Ciencia de Datos. Consiste en analizar los datos de participantes de la carrera ciclista Orbea Monegros 2024, y generar diferentes estadísticas y reportes mediante módulos separados.

## Estructura del Proyecto

- **`main.py`**: Archivo principal del programa.
- **`src/`**: Carpeta que contiene los módulos de los ejercicios.
  - **`ejer1.py`**: Importa el dataset, se reutiliza. Procesa los datos para listar los clubes únicos.
  - **`ejer2.py`**: Calcula el tiempo promedio por club.
  - **`ejer3.py`**: Identifica al ciclista con el menor tiempo registrado.
  - **`ejer4.py`**: Cuenta el número total de ciclistas por club.
  - **`ejer5.py`**: Genera un resumen del tiempo total acumulado por club.

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
```Mac/Linux:
source pec4/bin/activate
```  
```Windows:
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

### Tests
Cada módulo incluye una función de tests que valida su funcionalidad.  
Los tests se pueden ejecutar automáticamente al finalizar un ejercicio o manualmente desde el menú.


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