from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Cardapio(BoxLayout):
    pass

class Interface(App):
    def build(self):
        return Cardapio()

Interface().run()
