"""
Use adapter pattern and classes of your choice. Create a structure where you have 1-2 adaptees that have a method that
returns some text in spanish. Have an adapter which will have a method that translates the text to english. Have
examples of the usage of your class structure.
"""

import random
from abc import ABC, abstractmethod

MESSAGES_DICT = {
    "Spanish": {
        "perro" : "dog",
        "gato"  : "cat",
        "caimán": "alligator",
    },
    "French" : {
        "chien"    : "dog",
        "chat"     : "cat",
        "alligator": "alligator",
    },
}


class MessageReceiver(ABC):

    @abstractmethod
    def get_english_message(self):
        pass


class FrenchMessageReceiver(MessageReceiver):
    def __init__(self):
        self._language = 'French'
        self.__dict = MESSAGES_DICT[self._language]

    def get_message(self):
        return random.choice(list(self.__dict.keys()))

    def get_english_message(self):
        fr_message = self.get_message()
        eng_message = self.__dict[fr_message]
        print(f"[*] Got {self._language} message: {fr_message}, translated to: {eng_message}")
        return eng_message


class SpanishMessageReceiver:
    def __init__(self):
        self._language = 'Spanish'

    def get_spanish_message(self):
        return random.choice(list(MESSAGES_DICT[self._language].keys()))


class SpanishReceiverAdapter(MessageReceiver, SpanishMessageReceiver):
    def get_english_message(self):
        spanish_message = self.get_spanish_message()
        return self.__translate(spanish_message)

    def __translate(self, message):
        eng_message = MESSAGES_DICT[self._language][message]
        print(f"[*] Got {self._language} message: {message}, translated to: {eng_message}")
        return eng_message


class MessagePrinter:
    def print_english_message(self, message_receiver: MessageReceiver):
        print(f"Final message: {message_receiver.get_english_message()}\n")


if __name__ == '__main__':
    sp_receiver = SpanishReceiverAdapter()
    fr_receiver = FrenchMessageReceiver()

    printer = MessagePrinter()

    printer.print_english_message(sp_receiver)
    printer.print_english_message(fr_receiver)
