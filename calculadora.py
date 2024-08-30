def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero"
    
def calculadora():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    # Obtener la elección del usuario
    eleccion = input("Ingrese el número de la operación (1/2/3/4): ")

    # Verificar si la elección es válida
    if eleccion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if eleccion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")
        elif eleccion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")
        elif eleccion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif eleccion == '4':
            resultado = dividir(num1, num2)
            print(f"{num1} / {num2} = {resultado}")
    else:
        print("Elección inválida")

# Llamar a la función de la calculadora
calculadora()