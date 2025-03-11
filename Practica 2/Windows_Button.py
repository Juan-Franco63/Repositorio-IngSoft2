from Button import Button 

class Windows_Button(Button):

    def render(self):
        print("Render Windows Button")

    def on_click(self):
        print("Click Windows Button")