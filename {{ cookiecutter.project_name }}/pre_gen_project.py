from datetime import datetime
import os
import subprocess
import sys
import re


# Función para validar el nombre del proyecto
def validar_nombre_proyecto(name):
    if not re.match(r'^[a-zA-Z0-9_-]+$', name):
        raise ValueError(f"Nombre del proyecto no válido: {name}")
    return name


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

    # Crear el entorno virtual con Mamba
    project_name = validar_nombre_proyecto('{{ cookiecutter.project_slug }}')
    python_version = '{{ cookiecutter.python_version }}'

    # Validar versión de Python (opcional, solo números y puntos)
    if not re.match(r'^\d+(\.\d+){0,2}$', python_version):
        raise ValueError(f"Versión de Python no válida: {python_version}")

    print(f"Creando el entorno virtual '{project_name}' con Mamba...")
    create_env_cmd = ['mamba', 'create', '-n',
                      project_name, f'python={python_version}', '-y']

    try:
        # Ejecutar el comando para crear el entorno virtual sin shell=True
        subprocess.run(create_env_cmd, check=True)
        print(f"Entorno virtual '{project_name}' creado exitosamente.")

        # Instalar dependencias desde environment.yml si el archivo existe
        env_file = 'environment.yml'
        if os.path.exists(env_file):
            print(f"Instalando dependencias desde {env_file}...")
            install_deps_cmd = ['mamba', 'env',
                                'update', '-n', project_name, '-f', env_file]
            subprocess.run(install_deps_cmd, check=True)
            print("Dependencias instaladas correctamente.")

    except subprocess.CalledProcessError as error:
        print(f"Error al crear el entorno o instalar dependencias: {error}")
        sys.exit(1)

    # Mostrar instrucciones para activar el entorno
    print("Para activar el entorno, usa:")
    print(f"    conda activate {project_name}")
