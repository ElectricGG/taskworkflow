    def eliminar(self, tarea_id):
        tarea = self.buscar(tarea_id)   # lanza KeyError si no existe
        self._tareas.remove(tarea)
        return tarea