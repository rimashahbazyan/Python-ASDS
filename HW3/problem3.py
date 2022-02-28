"""
Use singleton pattern and classes of your choice. Create a structure where you have some resource that has states busy 
and free and 3 users that try to use the resource and change the state to busy while they are using it. The resource 
should be singleton. Implement using 2 different methods for singleton implementation that we have discussed. 
"""
from weakref import WeakValueDictionary

DB_PASS_DICT = {
    'admin': '123456',
    'user1': '111111'
}


# Borg implementation of Singleton
class DbConnectionBorg:
    __shared_state = None

    def __init__(self, username, pwd):
        if DbConnectionBorg.__shared_state is None:
            self.__pwd = pwd
            self.__username = username
            DbConnectionBorg.__shared_state = self.__dict__
        else:
            self.__dict__ = DbConnectionBorg.__shared_state

    def connect(self):
        if DB_PASS_DICT.get(self.__username) == self.__pwd:
            print(f"Connected to DB with username {self.__username}")
        else:
            print("Connection failed, wrong username or password!")


# Metaclass implementation of Singleton
class Singleton(type):
    _instances = WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if cls not in Singleton._instances:
            instance = super().__call__(*args, **kwargs)
            Singleton._instances[cls] = instance
        return Singleton._instances[cls]


class DbConnectionMeta(metaclass=Singleton):
    def __init__(self, username, pwd):
        self.__pwd = pwd
        self.__username = username

    def connect(self):
        if DB_PASS_DICT.get(self.__username) == self.__pwd:
            print(f"Connected to DB with username {self.__username}")
        else:
            print("Connection failed, wrong username or password!")


def __main__():
    print("\nBORG")
    db_connection = DbConnectionBorg(username='admin', pwd='123456')
    db_connection.connect()
    db_connection2 = DbConnectionBorg(username='user1', pwd='111111')
    db_connection2.connect()
    db_connection3 = DbConnectionBorg(username='user2', pwd='123')
    db_connection3.connect()

    print("\nMeta")
    db_connection = DbConnectionMeta(username='user2', pwd='123')
    db_connection.connect()  # wrong credentials
    del db_connection
    db_connection = DbConnectionMeta(username='admin', pwd='123456')
    db_connection.connect()  # right credentials
    db_connection2 = DbConnectionMeta(username='user1', pwd='111111')
    db_connection2.connect()  # trying to access another connection without deleting the last one
    del db_connection
    del db_connection2
    db_connection3 = DbConnectionMeta(username='user1', pwd='111111')
    db_connection3.connect()


if __name__ == '__main__':
    __main__()
