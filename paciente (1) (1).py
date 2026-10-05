class Paciente:
    def __init__(self, codigo, nombre, edad):
        self._codigo = codigo
        self.nombre = nombre  # Pasa por el setter
        self.edad = edad      # Pasa por el setter
        self._historial = []
        self._citas = []

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip().title()

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor <= 0 or valor >= 120:
            raise ValueError("La edad debe ser mayor a 0 y menor a 120 años.")
        self._edad = valor

    @property
    def historial(self):
        return list(self._historial)

    @property
    def citas(self):
        return list(self._citas)

    def agregar_atencion(self, descripcion):
        self._historial.append(descripcion)

    def agregar_cita(self, cita):
        self._citas.append(cita)

    def __str__(self):
        return f"[{self.codigo}] Paciente: {self.nombre} ({self.edad} años)"
