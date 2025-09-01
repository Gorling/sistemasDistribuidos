import threading
import time
import random

# Inicializando os relógios de Lamport para cada processo
lamport_p1 = 0
lamport_p2 = 0

# Locks para atualizar os relógios de forma segura
lock_p1 = threading.Lock()
lock_p2 = threading.Lock()

# Função para simular eventos e envio de mensagens do processo 1
def processo1():
    global lamport_p1, lamport_p2
    for i in range(5):
        # Evento local
        with lock_p1:
            lamport_p1 += 1
            print(f"[P1] Evento local {i+1}, timestamp = {lamport_p1}")
        time.sleep(random.uniform(0.1, 0.5))

        # Envia mensagem para P2
        with lock_p1:
            lamport_p1 += 1
            msg_timestamp = lamport_p1
            print(f"[P1] Enviando mensagem para P2, timestamp = {msg_timestamp}")

        # Recebimento simulado do lado de P2
        with lock_p2:
            lamport_p2 = max(lamport_p2, msg_timestamp) + 1
            print(f"[P2] Recebeu mensagem de P1, atualizando timestamp = {lamport_p2}")

# Função para simular eventos e envio de mensagens do processo 2
def processo2():
    global lamport_p1, lamport_p2
    for i in range(5):
        # Evento local
        with lock_p2:
            lamport_p2 += 1
            print(f"[P2] Evento local {i+1}, timestamp = {lamport_p2}")
        time.sleep(random.uniform(0.1, 0.5))

        # Envia mensagem para P1
        with lock_p2:
            lamport_p2 += 1
            msg_timestamp = lamport_p2
            print(f"[P2] Enviando mensagem para P1, timestamp = {msg_timestamp}")

        # Recebimento simulado do lado de P1
        with lock_p1:
            lamport_p1 = max(lamport_p1, msg_timestamp) + 1
            print(f"[P1] Recebeu mensagem de P2, atualizando timestamp = {lamport_p1}")

# Criando threads para os processos
t1 = threading.Thread(target=processo1)
t2 = threading.Thread(target=processo2)

# Iniciando threads
t1.start()
t2.start()

# Esperando threads terminarem
t1.join()
t2.join()

print("Fim da simulação de Lamport!")
