from paciente import Paciente
from medico import Medico, filtrar_medicos_por_especialidad
from cita import Cita

pacientes = []
medicos = []
citas = []
contador_citas = 0


# Buscar por código
def buscar(lista, codigo):
    for elemento in lista:
        if elemento.codigo == codigo:
            return elemento
    return None


# Cargar médicos de ejemplo
def cargar_medicos():
    datos = [
        ("M01", "Sofía Ramos", "Dermatología"),
        ("M02", "Carlos Mendoza", "Psicología"),
        ("M03", "Ana Torres", "Pediatría"),
        ("M04", "Lucía Vargas", "Ginecología"),
        ("M05", "Elena Quispe", "Obstetricia"),
        ("M06", "Pedro Salas", "Nutrición"),
        ("M07", "Luis Rojas", "Medicina General"),
        ("M08", "Marco Díaz", "Cirugía General"),
    ]
    for codigo, nombre, especialidad in datos:
        medicos.append(Medico(codigo, nombre, especialidad))


def especialidades_disponibles():
    lista = []
    for medico in medicos:
        if medico.especialidad not in lista:
            lista.append(medico.especialidad)
    return lista


def registrar_paciente():
    codigo = input("Código del paciente: ").strip()
    if buscar(pacientes, codigo):
        print("Ese código ya existe.")
        return

    nombre = input("Nombre: ").strip()
    try:
        edad = int(input("Edad: "))
        paciente = Paciente(codigo, nombre, edad)
        pacientes.append(paciente)
        print("Paciente registrado.")
    except ValueError as error:
        print("Error:", error)


def registrar_medico():
    codigo = input("Código del médico: ").strip()
    if buscar(medicos, codigo):
        print("Ese código ya existe.")
        return

    nombre = input("Nombre: ").strip()
    especialidad = input("Especialidad: ").strip()
    try:
        medico = Medico(codigo, nombre, especialidad)
        medicos.append(medico)
        print("Médico registrado.")
    except ValueError as error:
        print("Error:", error)


def programar_cita():
    global contador_citas

    codigo = input("Código del paciente: ").strip()
    paciente = buscar(pacientes, codigo)
    if paciente is None:
        print("Paciente no encontrado.")
        return

    print("\nMédicos disponibles:")
    for i, medico in enumerate(medicos, 1):
        print(i, "-", medico)

    try:
        opcion = int(input("Elige el número del médico: "))
        if opcion < 1 or opcion > len(medicos):
            print("Opción no válida.")
            return
    except ValueError:
        print("Debes escribir un número.")
        return

    medico = medicos[opcion - 1]
    fecha = input("Fecha (dd/mm/aaaa): ").strip()

    contador_citas += 1
    codigo_cita = f"C{contador_citas:03d}"
    cita = Cita(codigo_cita, paciente, medico, fecha)
    citas.append(cita)
    paciente.agregar_cita(cita)
    print("Cita programada:", cita)


def registrar_atencion():
    codigo = input("Código de la cita: ").strip()
    cita = buscar(citas, codigo)

    if cita is None:
        print("Cita no encontrada.")
        return
    if cita.estado == "cancelada":
        print("No se puede atender una cita cancelada.")
        return

    detalle = input("Descripción de la atención: ").strip()
    cita.marcar_atendida()
    texto = f"{cita.fecha} - {cita.medico.especialidad}: {detalle}"
    cita.paciente.agregar_atencion(texto)
    print("Atención registrada.")


def filtrar_medicos():
    especialidades = especialidades_disponibles()
    print("\nEspecialidades:")
    for i, especialidad in enumerate(especialidades, 1):
        print(i, "-", especialidad)

    try:
        opcion = int(input("Elige una especialidad: "))
        if opcion < 1 or opcion > len(especialidades):
            print("Opción no válida.")
            return
    except ValueError:
        print("Debes escribir un número.")
        return

    especialidad = especialidades[opcion - 1]
    resultados = filtrar_medicos_por_especialidad(medicos, especialidad)
    print("\nMédicos de", especialidad + ":")
    for medico in resultados:
        print(medico)


def cancelar_cita():
    codigo = input("Código de la cita: ").strip()
    cita = buscar(citas, codigo)

    if cita is None:
        print("Cita no encontrada.")
        return

    try:
        cita.cancelar()
        print("Cita cancelada.")
    except ValueError as error:
        print("Error:", error)


def ver_historial():
    codigo = input("Código del paciente: ").strip()
    paciente = buscar(pacientes, codigo)

    if paciente is None:
        print("Paciente no encontrado.")
        return

    print(paciente)
    print("Citas:", [str(cita) for cita in paciente.citas] or "Sin citas")
    print("Historial:", paciente.historial or "Sin atenciones")


def menu():
    while True:
        print("\n===== SISTEMA KAWSAY =====")
        print("1. Registrar paciente")
        print("2. Registrar médico")
        print("3. Programar cita")
        print("4. Registrar atención")
        print("5. Buscar médicos por especialidad")
        print("6. Cancelar cita")
        print("7. Ver historial")
        print("8. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            registrar_medico()
        elif opcion == "3":
            programar_cita()
        elif opcion == "4":
            registrar_atencion()
        elif opcion == "5":
            filtrar_medicos()
        elif opcion == "6":
            cancelar_cita()
        elif opcion == "7":
            ver_historial()
        elif opcion == "8":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


# Inicio del programa
if __name__ == "__main__":
    cargar_medicos()

    # Pacientes de ejemplo
    ejemplos = [
        ("P01", "María Flores", 34, [
            ("M07", "10/08/2026", "Control general, presión arterial normal."),
            ("M01", "02/09/2026", "Tratamiento para dermatitis leve."),
        ]),
        ("P02", "Jorge Castillo", 8, [
            ("M03", "15/07/2026", "Control de crecimiento, vacunas al día."),
            ("M03", "20/09/2026", "Cuadro gripal, reposo e hidratación."),
        ]),
    ]

    for codigo, nombre, edad, atenciones in ejemplos:
        paciente = Paciente(codigo, nombre, edad)
        pacientes.append(paciente)

        for codigo_medico, fecha, detalle in atenciones:
            medico = buscar(medicos, codigo_medico)
            contador_citas += 1
            cita = Cita(f"C{contador_citas:03d}", paciente, medico, fecha)
            citas.append(cita)
            paciente.agregar_cita(cita)
            cita.marcar_atendida()
            paciente.agregar_atencion(
                f"{fecha} - {medico.especialidad}: {detalle}"
            )

    menu()