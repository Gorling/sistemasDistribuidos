import threading
import time

# Função para cada thread
def imprime_nome(nome, intervalo):
    for _ in range(3):
        print(f"{nome}")
        time.sleep(intervalo)

# Criando threads com intervalos diferentes
thread1 = threading.Thread(target=imprime_nome, args=("Thread 1", 1))
thread2 = threading.Thread(target=imprime_nome, args=("Thread 2", 2))
thread3 = threading.Thread(target=imprime_nome, args=("Thread 3", 3))

# Iniciando as threads
thread1.start()
thread2.start()
thread3.start()

# Esperando as threads terminarem
thread1.join()
thread2.join()
thread3.join()
