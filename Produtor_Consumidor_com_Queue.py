import threading
import queue
import time
import random

# Criando a fila compartilhada
fila = queue.Queue(maxsize=5)  # capacidade limitada

# Função Produtor
def produtor():
    for i in range(10):
        item = f"Item {i}"
        fila.put(item)  # adiciona item na fila (bloqueia se cheia)
        print(f"Produtor produziu: {item}")
        time.sleep(random.uniform(0.1, 0.5))  # tempo variável de produção

# Função Consumidor
def consumidor():
    for _ in range(10):
        item = fila.get()  # retira item da fila (bloqueia se vazia)
        print(f"Consumidor consumiu: {item}")
        time.sleep(random.uniform(0.2, 0.6))  # tempo variável de consumo
        fila.task_done()  # sinaliza que a tarefa foi concluída

# Criando threads
thread_produtor = threading.Thread(target=produtor)
thread_consumidor = threading.Thread(target=consumidor)

# Iniciando threads
thread_produtor.start()
thread_consumidor.start()

# Esperando threads terminarem
thread_produtor.join()
thread_consumidor.join()

print("Fim da simulação do Produtor-Consumidor!")
