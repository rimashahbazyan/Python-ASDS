from abc import ABC, abstractmethod


class BankAccount(ABC):
    @classmethod
    def class_alias(cls):
        return cls.__name__

    @abstractmethod
    def create_account(self):
        pass


class PersonalAccount(BankAccount):
    @classmethod
    def class_alias(cls):
        return 'Personal'

    def create_account(self):
        print("Personal account created")


class BusinessAccount(BankAccount):
    @classmethod
    def class_alias(cls):
        return 'Business'

    def create_account(self):
        print("Business account created")


class BankAccountFactory:
    def __init__(self):
        self.all_accounts = {cls.class_alias(): cls for cls in BankAccount.__subclasses__()}


    def validate_account_name(self, account_name):
        if account_name not in self.all_accounts:
            raise ValueError(f'Account type "{account_name}" does not exist!')

    def get_account(self, account_name) -> BankAccount:
        self.validate_account_name(account_name)
        account_class = self.all_accounts[account_name]
        return account_class()


class Client:
    def create_account(self):
        account_name = input("What type of account do you want to open? ").capitalize()
        account_factory = BankAccountFactory()
        account = account_factory.get_account(account_name)
        account.create_account()


if __name__ == "__main__":
    client = Client()
    client.create_account()
