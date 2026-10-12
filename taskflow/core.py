"""Lógica de dominio para un gestor de tareas en memoria."""

import os

from dataclasses import dataclass


@dataclass
class Tarea:
    """Una tarea identificada de forma única dentro del gestor."""

    id: int
    titulo: str
    completada: bool = False


class GestorTareas:
    """Administra tareas sin reutilizar identificadores eliminados."""

    def __init__(self):
        self._tareas: list[Tarea] = []
        self._siguiente_id = 1

    def agregar(self, titulo: str) -> Tarea:
        """Crea, guarda y devuelve una tarea pendiente."""
        tarea = Tarea(id=self._siguiente_id, titulo=titulo)
        self._tareas.append(tarea)
        self._siguiente_id += 1
        return tarea

    def listar(self) -> list[Tarea]:
        """Devuelve una copia de las tareas registradas."""
        return list(self._tareas)

    def buscar(self, tarea_id: int) -> Tarea:
        """Busca una tarea por identificador o lanza ``KeyError``."""
        for tarea in self._tareas:
            if tarea.id == tarea_id:
                return tarea
        raise KeyError(f"No existe la tarea con id {tarea_id}")

    def eliminar(self, tarea_id: int) -> Tarea:
        """Elimina y devuelve la tarea indicada por su identificador."""
        tarea = self.buscar(tarea_id)
        self._tareas.remove(tarea)
        return tarea
