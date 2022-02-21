import random
import time
from abc import ABC, abstractmethod


def call_to_server():
    time.sleep(2)
    return random.randint(480, 520)


class BankAccountBuilder(ABC):

    @abstractmethod
    def create_id(self):
        pass

    @abstractmethod
    def create_balance(self):
        pass

    @abstractmethod
    def create_rate(self):
        pass


class BankAccount:
    def __init__(self):
        self.id = None
        self.balance = None
        self.rate = None

    def __str__(self):
        account_string = ''
        if self.id is not None:
            account_string += f'ID: {self.id} \n'
        if self.balance is not None:
            account_string += f'Balance: {self.balance} \n'
        if self.rate is not None:
            account_string += f'Rate: {self.rate} \n'
        return account_string


class ConcreteBankAccountBuilder(BankAccountBuilder):
    def __init__(self):
        self.__bank_account = None
        self.__reset()

    def __reset(self):
        self.__bank_account = BankAccount()

    def create_id(self):
        self.__bank_account.id = random.randint(1000, 9999)

    def create_balance(self, balance=0):
        self.__bank_account.balance = balance

    def create_rate(self):
        rate = call_to_server()
        self.__bank_account.rate = rate

    @property
    def bank_account(self):
        bank_account = self.__bank_account
        self.__reset()
        return bank_account


def __main__():
    builder = ConcreteBankAccountBuilder()
    # builder.create_id()
    builder.create_rate()
    builder.create_balance()
    print(builder.bank_account)

if __name__ == '__main__':
    __main__()