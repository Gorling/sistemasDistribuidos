import threading
import time

# Variável global compartilhada
memoria_compartilhada = 0

# Criando um lock
lock = threading.Lock()

# Função 1: adiciona 100
def adiciona():
    global memoria_compartilhada
    for _ in range(10):
        with lock:  # Bloqueia a memória compartilhada
            temp = memoria_compartilhada
            time.sleep(0.01)  # Simula processamento
            memoria_compartilhada = temp + 100

# Função 2: multiplica por 2
def multiplica():
    global memoria_compartilhada
    for _ in range(10):
        with lock:  # Bloqueia a memória compartilhada
            temp = memoria_compartilhada
            time.sleep(0.01)  # Simula processamento
            memoria_compartilhada = temp * 2

# Criando threads
t1 = threading.Thread(target=adiciona)
t2 = threading.Thread(target=multiplica)

# Iniciando threads
t1.start()
t2.start()

# Esperando threads terminarem
t1.join()
t2.join()

print(f"Valor final da memória compartilhada: {memoria_compartilhada}")
