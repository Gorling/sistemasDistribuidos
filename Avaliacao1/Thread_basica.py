import threading
import time

# Função para imprimir números pares
def imprime_pares():
    for i in range(0, 21, 2):
        print(f"Par: {i}")
        time.sleep(0.1)  # Pequena pausa para visualizar a alternância

# Função para imprimir números ímpares
def imprime_impares():
    for i in range(1, 20, 2):
        print(f"Ímpar: {i}")
        time.sleep(0.1)

# Criando as threads
thread_par = threading.Thread(target=imprime_pares)
thread_impar = threading.Thread(target=imprime_impares)

# Iniciando as threads
thread_par.start()
thread_impar.start()

# Esperando as threads terminarem
thread_par.join()
thread_impar.join()

print("Fim da execução!")
