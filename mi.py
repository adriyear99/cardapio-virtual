from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class cardapio(BoxLayout):
    pass


class interface(App):
    def build(self):
        return cardapio()


interface().run()

