# Plantilla Cookiecutter para Proyectos Jupyter con Sphinx

Esta plantilla de Cookiecutter está diseñada para crear proyectos que incluyen Jupyter Notebooks, integración de documentación con Sphinx, y las mejores prácticas de desarrollo para Python.

![Cookicutter](https://cdn-icons-png.flaticon.com/512/5473/5473473.png)

## ¿Qué incluye esta plantilla?

- **Jupyter Notebooks** integrados en la documentación mediante **nbsphinx**.
- **Sphinx** configurado con el tema **Read the Docs**.
- Integración con **pre-commit hooks** para formateo automático con **Black** y validación con **Flake8** y **Ruff**.
- Configuración opcional de CI con **GitHub Actions**.
- Soporte para ambientes virtuales con **venv** o **Conda**.
- Pruebas automáticas con **pytest**.
- Estructura lista para **Docker** (opcional).

## Uso de la Plantilla

Para usar esta plantilla de Cookiecutter:

1. Instala Cookiecutter si aún no lo tienes:

   ```bash
   pip install cookiecutter
   ```

2. Genera tu nuevo proyecto usando la plantilla:

   ```bash
   cookiecutter https://github.com/DiegoLerma/cookiecutter-jupyter-data-science
   ```

3. Responde las preguntas de Cookiecutter para configurar tu proyecto.

## Variables Disponibles

A continuación se muestran las variables configurables a través de **cookiecutter.json**:

- `project_name`: El nombre del proyecto.
- `author_name`: Tu nombre.
- `author_email`: Tu dirección de correo electrónico.
- `github_username`: Tu nombre de usuario de GitHub.
- `python_version`: La versión de Python para el proyecto.
- `license`: La licencia para tu proyecto (por defecto, MIT).
- `use_pre_commit_hooks`: Opción para usar o no **pre-commit hooks**.

## Ejemplo

```bash
cookiecutter https://github.com/DiegoLerma/cookiecutter-jupyter-data-science
```

Este comando generará un proyecto con la estructura configurada para Jupyter Notebooks, Sphinx, pre-commits y más.

## Requisitos Previos

- **Python 3.10+**
- **Cookiecutter** instalado

## Contribuciones

Si deseas contribuir a esta plantilla, por favor abre un **issue** o envía un **pull request** a este repositorio.
