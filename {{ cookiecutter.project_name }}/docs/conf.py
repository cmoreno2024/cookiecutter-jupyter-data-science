# pylint: disable=invalid-name
# flake8: noqa: E501

import os
import sys
sys.path.insert(0, os.path.abspath('../notebooks'))  # Ajusta esta ruta según la estructura de tu proyecto

# -- Project information -----------------------------------------------------
project = '{{ cookiecutter.project_name }}'
author = '{{ cookiecutter.author_name }}'
release = '{{ cookiecutter.version }}'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',      # Autodocumentación a partir de docstrings
    'sphinx.ext.napoleon',     # Soporte para docstrings estilo Google/NumPy
    'sphinx.ext.viewcode',     # Muestra el código fuente con enlaces
    'sphinx.ext.autosummary',  # Generación automática de resúmenes de módulos
    'nbsphinx',                # Soporte para Jupyter Notebooks
    'sphinx.ext.mathjax',      # Soporte para ecuaciones matemáticas
]

autosummary_generate = True  # Generación automática de archivos .rst
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'special-members': '__init__',
    'inherited-members': True,
    'show-inheritance': True,
}

# -- Configuración para nbsphinx (Jupyter Notebooks) ---------------------------
nbsphinx_allow_errors = True  # Permite mostrar notebooks aunque contengan errores
nbsphinx_execute = 'never'    # No ejecutar los notebooks al construir la documentación

# -- Napoleon settings for Google style docstrings ---------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_use_param = True
napoleon_use_rtype = True

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Tema Read the Docs
html_static_path = ['_static']   # Archivos estáticos como CSS personalizados

# -- Paths for static files (like custom CSS) --------------------------------
html_static_path = ['_static']
