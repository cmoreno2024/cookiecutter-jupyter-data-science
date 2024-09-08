# hooks/pre_gen_project.py
from datetime import datetime
import os


# Función principal del pre-hook
def pre_gen_project():
    # Obtener el año actual
    current_year = datetime.now().year

    # Obtener el archivo cookiecutter.json en el contexto actual
    cookiecutter_context_file = os.path.join(os.getcwd(), 'cookiecutter.json')

    # Reemplazar las variables en el archivo cookiecutter.json si es necesario
    with open(cookiecutter_context_file, 'r+', encoding='utf-8') as f:
        # Leer el contenido original del archivo
        content = f.read()

        # Reemplazar la clave del año por el valor actual
        content = content.replace(
            '"current_year": "YEAR"', f'"current_year": "{current_year}"')

        # Volver a escribir el archivo con la nueva variable reemplazada
        f.seek(0)
        f.write(content)
        f.truncate()
