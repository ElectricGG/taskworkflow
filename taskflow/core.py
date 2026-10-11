"""Operaciones básicas para una lista de tareas en memoria."""


def agregar(tareas, titulo):
    """Añade una tarea pendiente y devuelve la lista modificada."""
    tareas.append({"titulo": titulo, "completada": False})
    return tareas


def completar(tareas, indice):
    """Marca como completada la tarea situada en *indice*."""
    tareas[indice]["completada"] = True
    return tareas


def eliminar(tareas, indice):
    """Elimina y devuelve la tarea situada en *indice*.

    Python genera ``IndexError`` cuando el índice no existe, lo que permite al
    consumidor tratar explícitamente una selección inválida.
    """
    return tareas.pop(indice)
