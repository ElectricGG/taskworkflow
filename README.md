# Taskflow

[![CI](https://github.com/ElectricGG/taskworkflow/actions/workflows/ci.yml/badge.svg)](https://github.com/ElectricGG/taskworkflow/actions/workflows/ci.yml)

Gestor de tareas mínimo para practicar un flujo DevOps con pull requests, pruebas continuas y GitHub Pages.

## Avance

- [x] PR #1: plantilla para pull requests.
- [x] PR #2: CI que ejecuta pruebas en cada PR.
- [x] PR #3: función `eliminar()` y tres pruebas.
- [x] PR #4: sitio estático y despliegue en GitHub Pages después de las pruebas.

## Uso

```python
from taskflow.core import agregar, eliminar

tareas = []
agregar(tareas, "Preparar demo")
eliminada = eliminar(tareas, 0)
```

## Pruebas

```bash
python -m pytest
```
