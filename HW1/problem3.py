from abc import ABC, abstractmethod
import random

class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def uncheck(self):
        pass


class GUIFactory:
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WinButton(Button):
    def click(self):
        print("Windows style button clicked")


class MacButton(Button):
    def click(self):
        print("Apple style button clicked")


class WinCheckbox(Checkbox):
    def check(self):
        print("Windows style Checkbox checked")

    def uncheck(self):
        print("Windows style Checkbox unchecked")


class MacCheckbox(Checkbox):
    def check(self):
        print("Apple style Checkbox checked")

    def uncheck(self):
        print("Apple style Checkbox unchecked")


class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class Application:
    def __init__(self, gui_factory: GUIFactory):
        self.gui_factory = gui_factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.gui_factory.create_button()
        self.checkbox = self.gui_factory.create_checkbox()

    def paint(self):
        is_clicked = input("This is a button, do you want to click it? ").lower()
        if is_clicked in ["yes", "y"]:
            self.button.click()


if __name__ == "__main__":
    all_oses = {"Windows": WinFactory, "MacOS": MacFactory}
    user_os, factory = random.choice(list(all_oses.items()))
    print(f"User's Operating System is {user_os}")
    app = Application(factory())
    app.create_ui()
    app.paint()
