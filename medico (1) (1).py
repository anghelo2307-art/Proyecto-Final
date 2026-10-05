class Medico:
    # Lista simple en minúsculas y sin tildes para evitar fallos de escritura
    ESPECIALIDADES_VALIDAS = [
        "dermatologia", "psicologia", "pediatria", "ginecologia",
        "obstetricia", "nutricion", "medicina general", "cirugia general"
    ]

    def __init__(self, codigo, nombre, especialidad):
        self._codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad  # Pasa por el setter

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
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        valor_limpio = (valor or "").strip().lower()
        if valor_limpio not in Medico.ESPECIALIDADES_VALIDAS:
            raise ValueError(f"Especialidad inválida. Use una de: {Medico.ESPECIALIDADES_VALIDAS}")
        self._especialidad = valor_limpio.title()

    def __str__(self):
        return f"[{self.codigo}] Dr(a). {self.nombre} - {self.especialidad}"


def filtrar_medicos_por_especialidad(medicos, especialidad):
    esp_buscada = (especialidad or "").strip().title()
    return list(filter(lambda m: m.especialidad == esp_buscada, medicos))
