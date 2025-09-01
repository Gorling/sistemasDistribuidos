import threading

# Função que calcula a soma da lista
def soma_lista(numeros, resultado, index):
    total = sum(numeros)
    resultado[index] = total  # Armazena o resultado na posição da lista

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lista para guardar o resultado
resultado = [0]

# Criando a thread
thread = threading.Thread(target=soma_lista, args=(numeros, resultado, 0))

# Iniciando a thread
thread.start()

# Esperando a thread terminar
thread.join()

print(f"A soma da lista é: {resultado[0]}")
