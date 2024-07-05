import numpy as np
from prueba_1 import cargar_datos, guardar_datos, ingresar_ficha, buscar_por_rut, buscar_medicamentos_por_rut, eliminar_ficha, listar_pacientes


# Cargar datos existentes desde el archivo JSON
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
        # Guardar los datos actualizados en el archivo JSON antes de salir
        guardar_datos(listado_pacientes)
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, ingrese una opción del 1 al 6.")
