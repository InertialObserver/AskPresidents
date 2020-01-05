from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

class AskPresidentsLayout(BoxLayout):
        def choice(self, guess):
            output = guess
            if self.ids.result.text == "":
                self.ids.result.text = output

class AskPresidents(App):
    def build(self):
        return AskPresidentsLayout()

if __name__== "__main__":
    AskPresidents().run()