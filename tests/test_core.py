import pytest

from taskflow.core import agregar, eliminar


def test_eliminar_quita_la_tarea_indicada():
    tareas = [{"titulo": "Documentar", "completada": False}, {"titulo": "Probar", "completada": False}]

    eliminada = eliminar(tareas, 0)

    assert eliminada["titulo"] == "Documentar"
    assert tareas == [{"titulo": "Probar", "completada": False}]


def test_eliminar_devuelve_la_tarea_eliminada():
    tareas = []
    agregar(tareas, "Desplegar")

    assert eliminar(tareas, 0) == {"titulo": "Desplegar", "completada": False}


def test_eliminar_con_indice_invalido_lanza_error():
    with pytest.raises(IndexError):
        eliminar([], 0)
