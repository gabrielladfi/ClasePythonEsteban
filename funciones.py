def imprimir_informacion(informacion_paciente: dict):
    informacion_paciente["verificado"] = True
    print(informacion_paciente)



def base_clinica_pacientes(informacion_paciente:dict, funcion_imprimir):
    if "nombre" not in informacion_paciente.keys():
        print("La información del paciente está incompleta")
    elif "email" not in informacion_paciente.keys():
        print("No se encuentra el correo del paciente")
    else:
        print("La información del paciente está completa")
        funcion_imprimir(informacion_paciente)


paciente_gabriel = {
    "nombre": "Gabriel Galindo",
    "email": "gerencia@deltainnovalabs.com",
    "terapia": "DBT"
}

base_clinica_pacientes(paciente_gabriel, imprimir_informacion)