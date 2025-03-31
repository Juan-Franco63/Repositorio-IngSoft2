from Button import Button

class HTML_Button(Button):

    def render(self):
        print("Render HTML Button")

    def on_click(self):
        print("Click HTML Button")