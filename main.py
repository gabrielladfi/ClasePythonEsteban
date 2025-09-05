def sumar(numero1, numero2):
    resultado = numero1 + numero2
    lista_elementos = ["peras", "manzanas", "tomates"]
    for elementos in lista_elementos:
        print(elementos)
    return resultado
    


#Diccionarios
diccionario_contextual = {
    "nombre_escuela": "Contextual",
    "anos": 20,
    "recomendado_para_TDAH": True
}

diccionario_conductual = {
    "nombre_escuela": "Conductista",
    "anos": 50,
    "recomendado_para_TDAH": False
}


resultado_final = sumar(2,2)
print(resultado_final)