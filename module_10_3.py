import threading
from time import sleep
from random import randint


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        counter = 100
        while counter >= 0:
            summa = randint(50, 500)
            self.lock.acquire()
            try:
                self.balance += summa
                print(f"Пополнение: {summa}. Баланс: {self.balance}\n")
            finally:
                self.lock.release()
            sleep(0.001)
            counter -= 1

    def take(self):
        counter = 100
        while counter >= 0:
            summa = randint(50, 500)
            print(f'Запрос на {summa}')
            self.lock.acquire()
            try:
                if summa <= self.balance:
                    self.balance -= summa
                    print(f'Снятие: {summa}. Баланс: {self.balance}\n')
                else:
                    print('Запрос отклонён, недостаточно средств\n')
            finally:
                self.lock.release()
            sleep(0.001)
            counter -= 1

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

