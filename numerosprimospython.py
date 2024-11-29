def es_primo(numero):
    """Función para verificar si un número es primo."""
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def obtener_divisores(numero):
    """Función para obtener los divisores de un número."""
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores


def main():
    """Función principal que ejecuta el programa."""
    print("¡Bienvenido a la calculadora de números primos!")
    
    try:
        numero = int(input("Por favor, introduce un número entero positivo: "))
        
        if numero <= 0:
            print("Error: El número debe ser entero y positivo.")
        else:
            if es_primo(numero):
                print(f"El número {numero} es primo.")
            else:
                print(f"El número {numero} no es primo.")
                divisores = obtener_divisores(numero)
                print(f"Sus divisores son: {', '.join(map(str, divisores))}")
    
    except ValueError:
        print("Error: Por favor, introduce un número válido.")
 
        
if __name__ == "__main__":
    main()
