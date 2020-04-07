from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class AskPresidentsLayout(BoxLayout):
        def choice(self, guess):
            output = guess
            if self.ids.result.text == "":  # if the result box is empty, then print the result. If there is already a result, do nothing.
                self.ids.result.text = output

        def clear(self):
            self.ids.result.text = ""  # erases the results so user can guess again

class AskPresidents(App):
    def build(self):
        return AskPresidentsLayout()

if __name__== "__main__":
    AskPresidents().run()