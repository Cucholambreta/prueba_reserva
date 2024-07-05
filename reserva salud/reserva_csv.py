import numpy as np
import csv
import os

# Función para cargar los datos desde un archivo CSV
def cargar_datos():
    pacientes = np.empty((0, 7), dtype=object)
    try:
        with open('pacientes.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                pacientes = np.vstack([pacientes, np.array(row)])
    except FileNotFoundError:
        print("Archivo CSV no encontrado. Se creará uno nuevo al guardar los datos.")
    return pacientes

# Función para guardar los datos en un archivo CSV
def guardar_datos(pacientes):
    with open('pacientes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for paciente in pacientes:
            writer.writerow(paciente)

# Función para ingresar la ficha de un paciente
def ingresar_ficha():
    nombre = input("Nombre del paciente: ")
    rut = input("RUT del paciente: ")
    edad = input("Edad del paciente: ")
    sexo = input("Sexo del paciente: ")
    fono = input("Teléfono del paciente: ")
    motivo = input("Motivo de la consulta: ")
    medicamentos = input("Medicamentos recetados: ")

    nueva_ficha = np.array([[nombre, rut, edad, sexo, fono, motivo, medicamentos]])
    return nueva_ficha

# Función para buscar una ficha por RUT
def buscar_por_rut(pacientes, rut):
    paciente_encontrado = None
    for paciente in pacientes:
        if paciente[1] == rut:
            paciente_encontrado = paciente
            break
    return paciente_encontrado

# Función para buscar medicamentos por RUT e imprimir motivo de consulta y medicamentos
def buscar_medicamentos_por_rut(pacientes, rut):
    encontrados = False
    for paciente in pacientes:
        if paciente[1] == rut:
            print(f"Motivo de consulta: {paciente[5]}")
            print(f"Medicamentos recetados: {paciente[6]}")
            encontrados = True
    if not encontrados:
        print("No se encontraron medicamentos para ese RUT.")

# Función para eliminar una ficha por RUT
def eliminar_ficha(pacientes, rut):
    pacientes_actualizados = [paciente for paciente in pacientes if paciente[1] != rut]
    return np.array(pacientes_actualizados)

# Función para listar todos los pacientes
def listar_pacientes(pacientes):
    for i, paciente in enumerate(pacientes, start=1):
        print(f"Paciente {i}:")
        print(f"Nombre: {paciente[0]}")
        print(f"RUT: {paciente[1]}")
        print(f"Edad: {paciente[2]}")
        print(f"Sexo: {paciente[3]}")
        print(f"Teléfono: {paciente[4]}")
        print(f"Motivo de consulta: {paciente[5]}")
        print(f"Medicamentos recetados: {paciente[6]}")
        print()

# Cargar datos existentes desde el archivo CSV
listado_pacientes = cargar_datos()

while True:
    print("Menú:")
    print("1. Ingresar ficha del paciente")
    print("2. Buscar ficha por rut")
    print("3. Buscar medicamentos por rut")
    print("4. Eliminar ficha del paciente")
    print("5. Listar pacientes atendidos")
    print("6. Salir")
    
    opcion = input("Ingrese el número de la opción deseada (1-6): ")

    if opcion == '1':
        nueva_ficha = ingresar_ficha()
        listado_pacientes = np.concatenate((listado_pacientes, nueva_ficha), axis=0)
        print("¡Ficha ingresada correctamente!")

    elif opcion == '2':
        rut = input("Ingrese el RUT a buscar: ")
        paciente_encontrado = buscar_por_rut(listado_pacientes, rut)
        if paciente_encontrado is not None:
            print("Paciente encontrado:")
            print(f"Nombre: {paciente_encontrado[0]}")
            print(f"Edad: {paciente_encontrado[2]}")
            print(f"Sexo: {paciente_encontrado[3]}")
            print(f"Teléfono: {paciente_encontrado[4]}")
            print(f"Motivo de consulta: {paciente_encontrado[5]}")
            print(f"Medicamentos recetados: {paciente_encontrado[6]}")
        else:
            print("No se encontró ningún paciente con ese RUT.")

    elif opcion == '3':
        rut = input("Ingrese el RUT para buscar medicamentos: ")
        buscar_medicamentos_por_rut(listado_pacientes, rut)

    elif opcion == '4':
        rut = input("Ingrese el RUT de la ficha a eliminar: ")
        listado_pacientes = eliminar_ficha(listado_pacientes, rut)
        print("Ficha eliminada correctamente.")

    elif opcion == '5':
        if len(listado_pacientes) > 0:
            print("Listado de pacientes atendidos:")
            listar_pacientes(listado_pacientes)
        else:
            print("No hay pacientes registrados.")

    elif opcion == '6':
        # Guardar los datos actualizados en el archivo CSV antes de salir
        guardar_datos(listado_pacientes)
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, ingrese una opción del 1 al 6.")
