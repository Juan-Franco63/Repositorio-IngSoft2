from abc import ABC, abstractmethod
from Button import Button

class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render(self):
        button = self.create_button()
        button.render()
        button.on_click()