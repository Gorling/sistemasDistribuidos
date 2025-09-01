import threading
import time

# Dois locks compartilhados
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    print("Thread 1 tentando adquirir Lock 1...")
    with lock1:
        print("Thread 1 adquiriu Lock 1")
        time.sleep(1)  # Simula algum processamento
        print("Thread 1 tentando adquirir Lock 2...")
        with lock2:
            print("Thread 1 adquiriu Lock 2")
    print("Thread 1 terminou")

def thread2():
    print("Thread 2 tentando adquirir Lock 2...")
    with lock2:
        print("Thread 2 adquiriu Lock 2")
        time.sleep(1)  # Simula algum processamento
        print("Thread 2 tentando adquirir Lock 1...")
        with lock1:
            print("Thread 2 adquiriu Lock 1")
    print("Thread 2 terminou")

# Criando threads
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

# Iniciando threads
t1.start()
t2.start()

# Esperando threads terminarem
t1.join()
t2.join()

print("Fim do programa")
