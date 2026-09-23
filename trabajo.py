
# SISTEMA DE SOPORTE ACADEMICO

TIPOS_CONSULTA = [
    "matricula",
    "pagos",
    "constancia",
    "plataforma",
    "otro"
]


# FUNCION SIN RETORNO
def mostrar_menu():
    print("\n===== SOPORTE ACADEMICO =====")
    print("1. Registrar solicitud")
    print("2. Ver solicitudes registradas")
    print("3. Salir")


# FUNCION CON RETORNO
def validar_texto(texto):
    return len(texto.strip()) > 0


# FUNCION CON RETORNO
def validar_codigo(codigo):
    return len(codigo.strip()) >= 4


# FUNCION CON RETORNO
def validar_tipo(tipo, tipos_validos):
    return tipo.lower().strip() in tipos_validos


# FUNCION CON RETORNO
def asignar_prioridad(tipo):
    tipo = tipo.lower().strip()

    if tipo == "plataforma" or tipo == "pagos":
        return "Alta"
    elif tipo == "matricula":
        return "Media"
    else:
        return "Baja"


# FUNCION CON RETORNO
def registrar_solicitud():
    print("\n--- REGISTRO DE SOLICITUD ---")

    codigo = input("Codigo de estudiante: ")

    if not validar_codigo(codigo):
        print("Error: el codigo debe tener minimo 4 caracteres.")
        return None

    nombre = input("Nombre del estudiante: ")

    if not validar_texto(nombre):
        print("Error: el nombre no puede estar vacio.")
        return None

    tipo = input(
        "Tipo (matricula, pagos, constancia, plataforma, otro): "
    ).lower().strip()

    if not validar_tipo(tipo, TIPOS_CONSULTA):
        print("Error: tipo de consulta incorrecto.")
        return None

    descripcion = input("Descripcion breve: ")

    if not validar_texto(descripcion):
        print("Error: la descripcion no puede estar vacia.")
        return None

    prioridad = asignar_prioridad(tipo)

    solicitud = {
        "codigo": codigo.strip(),
        "nombre": nombre.strip(),
        "tipo": tipo,
        "descripcion": descripcion.strip(),
        "prioridad": prioridad
    }

    return solicitud


# FUNCION SIN RETORNO
def mostrar_resumen(solicitud):
    print("\n===== RESUMEN DE SOLICITUD =====")
    print("Codigo:", solicitud["codigo"])
    print("Nombre:", solicitud["nombre"])
    print("Tipo:", solicitud["tipo"])
    print("Descripcion:", solicitud["descripcion"])
    print("Prioridad:", solicitud["prioridad"])

def ver_solicitudes(solicitudes):
    if not solicitudes:
        print("\nNo hay solicitudes registradas todavia.")
        return
    print(f"\n===== TOTAL: {len(solicitudes)} solicitudes =====")
    for s in solicitudes:
        mostrar_resumen(s)

# PROGRAMA PRINCIPAL
def main():
    solicitudes = []

    while len(solicitudes) < 3:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            solicitud = registrar_solicitud()

            if solicitud is not None:
                solicitudes.append(solicitud)
                print("\nSolicitud registrada correctamente.")
                mostrar_resumen(solicitud)

        elif opcion == "2":
            ver_solicitudes(solicitudes)
            
        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opcion incorrecta.")

    if len(solicitudes) >= 3:
        print("\nSe registraron las 3 solicitudes minimas.")

    print("\nTotal de solicitudes:", len(solicitudes))


if __name__ == "__main__":
    main()