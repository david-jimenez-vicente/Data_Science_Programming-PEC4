# Proyecto PEC4

Este proyecto es una solución a los ejercicios de la PEC4 de Programación para la Ciencia de Datos. Consiste en analizar un conjunto de datos sobre ciclistas y generar diferentes estadísticas y reportes mediante módulos separados.

## Estructura del Proyecto

- **`main.py`**: Archivo principal del programa.
- **`src/`**: Carpeta que contiene los módulos de los ejercicios.
  - **`ejercicio1.py`**: Importa el dataset, se reutiliza. Procesa los datos para listar los clubes únicos.
  - **`ejercicio2.py`**: Calcula el tiempo promedio por club.
  - **`ejercicio3.py`**: Identifica al ciclista con el menor tiempo registrado.
  - **`ejercicio4.py`**: Cuenta el número total de ciclistas por club.
  - **`ejercicio5.py`**: Genera un resumen del tiempo total acumulado por club.

## Uso

### 1. Descargar y configurar el Proyecto
Se aconseja crear un entorno virtual para este proyecto.  
Ejecuta  en tu terminal lo siguiente para clonar el repositorio:  
```
git clone https://github.com/david-jimenez-vicente/Data_Science_Programming-PEC4.git
```  
Y con esto vamos a la carpeta del repositorio clonado:  
```
cd ./Data_Science_Programming-PEC4
```  

### 2. Ejecutar el Proyecto  

Una vez en el directorio local del proyecto, hay 2 maneras de usar el programa: Apertura manual (sin instalación), o instalación en el sistema.  

- Opción 1. Ejecutarlo sin instalar:  
    - a) Este proyecto utiliza Python y depende de las siguientes librerías:  
      - `pandas`
       Para instalarla ejecuta:  
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
   - Opciones `2 al 6`: Ejecuta un ejercicio específico y opcionalmente sus tests.
   - Opción `7`: Salir del programa.

### Tests
Cada módulo incluye una función de tests que valida su funcionalidad básica.  
Los tests se pueden ejecutar automáticamente al finalizar un ejercicio o manualmente desde el menú.


## Notas Adicionales

* Si encuentras algún error en los datos o el código, verifica que el archivo `dataset.csv` esté correctamente ubicado en la arpeta "data" y que las dependencias estén instaladas en la carpeta "src". 
* Para soporte adicional, contacta al administrador del proyecto.  
* Se distribuye bajo licencia MIT. Puedes comprobarlo en el archivo `LICENSE`