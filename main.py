import sys
import json

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def calcula_factorial(data):
    result = {}
    for key, value in data.items():
        # Intentamos convertir el valor a un número entero
        try:
            num = int(value)
            # Calculamos el factorial del número
            result[key] = factorial(num)
        except ValueError:
            # Si el valor no es numerico, lo dejamos sin modificar
            result[key] = value
    return result

def main():
    # argumentos de la línea de comandos (excepto el primer argumento, que es el nombre del script)
    args = sys.argv[1:]

    # Verifica si se proporcionaron argumentos
    if not args:
        print("Proporciona un JSON como argumento.")
        return

    # El primer argumento es tratado como el JSON
    json_string = args[0]

    try:
        # analizar el JSON
        data = json.loads(json_string)

        result = calcula_factorial(data)

        # Mostrar el resultado por consola en formato JSON
        print(json.dumps({"resultado": result}))
    
    except json.JSONDecodeError:
        print("Error: Los argumentos no están en formato JSON válido.")

main()
