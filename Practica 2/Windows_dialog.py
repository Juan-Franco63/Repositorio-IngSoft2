from dialog import Dialog
from Windows_Button import Windows_Button

class Windows_Dialog(Dialog):
    def create_button(self):
        return Windows_Button()
