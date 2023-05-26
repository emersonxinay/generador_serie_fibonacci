def generar_serie(serie):
    if serie == 1:
        # Generar la serie de Fibonacci
        n = int(input("Ingrese la longitud de la serie de Fibonacci: "))
        serie_fibonacci = [0, 1]
        for i in range(2, n):
            serie_fibonacci.append(serie_fibonacci[i-1] + serie_fibonacci[i-2])
        return serie_fibonacci
    elif serie == 2:
        # Generar la serie de números primos
        n = int(input("Ingrese la cantidad de números primos a generar: "))
        serie_primos = []
        numero = 2
        while len(serie_primos) < n:
            es_primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo:
                serie_primos.append(numero)
            numero += 1
        return serie_primos