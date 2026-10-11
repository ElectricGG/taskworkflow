import pytest

from taskflow.core import agregar, eliminar


def test_eliminar_quita_la_tarea():
    gestor = GestorTareas()
    gestor.agregar("A")
    gestor.agregar("B")
    gestor.eliminar(1)
    assert [t.id for t in gestor.listar()] == [2]


def test_eliminar_no_reutiliza_ids():
    gestor = GestorTareas()
    gestor.agregar("A")
    gestor.eliminar(1)
    assert gestor.agregar("B").id == 2


def test_eliminar_inexistente_lanza_error():
    with pytest.raises(KeyError):
        GestorTareas().eliminar(42)