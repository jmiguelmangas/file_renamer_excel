Español:

Renombrar Archivos desde Excel
Este script de Python está diseñado para renombrar archivos en una carpeta basándose en los nombres proporcionados en un archivo de Excel.

Funcionalidades:
Lee un archivo de Excel que contiene los nombres nuevos para los archivos.
Verifica que el número de archivos en la carpeta coincida con el número de nombres en el archivo de Excel.
Renombra los archivos en la carpeta según los nombres especificados en el archivo de Excel.

Cómo Usar:
Coloca el archivo de Excel en el mismo directorio que el script renombrar_archivos.py.
Ejecuta el script proporcionando la ruta del archivo de Excel y la carpeta de archivos a renombrar.
El script verificará si el número de archivos coincide con el número de nombres en el archivo de Excel.
Si la verificación es exitosa, los archivos se renombrarán automáticamente.

Requisitos:
Python 3.x
Biblioteca openpyxl

Crear archivos de ejemplo:

Ejecuta creator.py para crear una carpeta con archivos
Ejemplo de uso:

python creator.py 50 carpetaEjemplo  -> 50 es el numero de archivos a crear

Ejemplo de Uso:

python renombrar_archivos.py archivo_excel.xlsx carpeta_ejemplo

English:

Rename Files from Excel

This Python script is designed to rename files in a folder based on the names provided in an Excel file.

Features:
Reads an Excel file containing the new names for the files.
Verifies that the number of files in the folder matches the number of names in the Excel file.
Renames the files in the folder according to the names specified in the Excel file.

How to Use:
Place the Excel file in the same directory as the rename_files.py script.
Run the script by providing the path to the Excel file and the folder of files to rename.
The script will verify if the number of files matches the number of names in the Excel file.
If the verification is successful, the files will be renamed automatically.

Requirements:
Python 3.x
openpyxl library

Creating Sample Folder:
Run creator.py for creating a folder with sample files to be renamed:

python creator.py 50 sample folder -> 50 is the number of files

Usage Example:

python rename_files.py excel_file.xlsx example_folder
