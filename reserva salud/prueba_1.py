import numpy as np
import json
import os

# Función para cargar los datos desde un archivo JSON
def cargar_datos():
    try:
        with open('pacientes.json', 'r') as file:
            data = json.load(file)
            pacientes = np.array(data)
    except FileNotFoundError:
        # Si el archivo no existe, crea un array vacío
        pacientes = np.empty((0, 7), dtype=object)
    return pacientes

# Función para guardar los datos en un archivo JSON
def guardar_datos(pacientes):
    with open('pacientes.json', 'w') as file:
        json.dump(pacientes.tolist(), file)

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
