# Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable

texto = "Hola, soy una cadena de texto"
numero = 42
decimal = 3.14

resultado = texto + " y tengo un número " + str(numero) + ", y un decimal " + str(decimal)

print(resultado)


# Los enteros (int) en Python no tienen un límite fijo. En Python 3.x, los enteros se almacenan como objetos de tipo long, lo que significa que pueden ser tan grandes como la memoria disponible en la máquina. Sin embargo, ten en cuenta que a medida que los enteros se vuelven más grandes, el tiempo de cálculo necesario para realizar operaciones con ellos también aumenta.

# Los flotantes (float) en Python están limitados por la precisión de la representación de punto flotante en la máquina. En Python, los flotantes se implementan utilizando el estándar IEEE 754, que utiliza 64 bits para almacenar el valor de punto flotante. Esto significa que los flotantes en Python tienen una precisión limitada y pueden perder precisión en cálculos muy grandes o muy pequeños.

# En Python también existe un tipo de datos decimal que se puede utilizar para realizar operaciones aritméticas con una precisión arbitraria. Este tipo de datos utiliza una representación decimal exacta en lugar de una representación de punto flotante, lo que lo hace especialmente útil para aplicaciones financieras y contables.


# Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable.

n = int(input("Ingrese el valor de n: "))  # Solicitamos al usuario el valor de n

suma = n * (n + 1)

print("La suma de los primeros", n, "números pares es:", suma)