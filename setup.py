from setuptools import setup, find_packages

setup(
    name='pec4',
    version='1.0.0',
    description='Solución a los ejercicios de la PEC4 de Programación para la Ciencia de Datos',
    author='José David Jiménez Vicente',
    author_email='jdjvjdjv@gmail.com',
    url='https://github.com/david-jimenez-vicente/Data_Science_Programming-PEC4',
    packages=find_packages(),  # Cambiado esto
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'faker',
        'pytest',
        'pytest-cov',
        'pylint',
        'setuptools',
    ],
    entry_points={
        'console_scripts': [
            'pec4=src.main:main',  # Modificado esto para apuntar a src.main
        ],
    },
    data_files=[
        ('data', ['./data/dataset.csv']),
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)