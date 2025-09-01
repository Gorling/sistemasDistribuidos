import threading
import time
import random

# Número de threads
num_threads = 4

# Criando uma barreira para sincronizar as threads
barreira = threading.Barrier(num_threads)

def tarefa(thread_id):
    # Etapa 1
    print(f"Thread {thread_id} iniciando a Etapa 1")
    time.sleep(random.uniform(0.1, 0.5))  # Simula trabalho
    print(f"Thread {thread_id} terminou a Etapa 1")

    # Espera todas as threads terminarem a Etapa 1
    barreira.wait()

    # Etapa 2
    print(f"Thread {thread_id} iniciando a Etapa 2")
    time.sleep(random.uniform(0.1, 0.5))  # Simula trabalho
    print(f"Thread {thread_id} terminou a Etapa 2")

# Criando threads
threads = []
for i in range(num_threads):
    t = threading.Thread(target=tarefa, args=(i+1,))
    threads.append(t)
    t.start()

# Esperando todas terminarem
for t in threads:
    t.join()

print("Todas as threads concluíram suas tarefas!")
