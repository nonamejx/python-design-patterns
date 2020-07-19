"""
Abstract Factory Design Pattern.

Intent:Provide an interface for creating families of related or dependent objects without specifying their
concrete classes.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class MacOSButton(Button):

    def click(self) -> str:
        return "You've clicked on a MacOS button."


class WindowsButton(Button):

    def click(self) -> str:
        return "You've clicked on a Windows button."


class Checkbox(ABC):

    @abstractmethod
    def select(self):
        pass


class MacOSCheckbox(Checkbox):

    def select(self) -> str:
        return "You've selected a MacOS checkbox."


class WindowsCheckbox(Checkbox):

    def select(self) -> str:
        return "You've selected a Windows checkbox."


class GUIFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return different abstract products.
    These products are called a family and are related by a high-level theme or concept.
    """

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class MacOSGUIFactory(GUIFactory):

    def create_button(self) -> MacOSButton:
        return MacOSButton()

    def create_checkbox(self) -> MacOSCheckbox:
        return MacOSCheckbox()


class WindowsGUIFactory(GUIFactory):

    def create_button(self) -> WindowsButton:
        return WindowsButton()

    def create_checkbox(self) -> WindowsCheckbox:
        return WindowsCheckbox()


def app(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.click())
    print(checkbox.select())


if __name__ == '__main__':
    app(WindowsGUIFactory())
