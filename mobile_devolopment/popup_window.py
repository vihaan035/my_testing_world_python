from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

class Widgets(Widget):
    pass

class MyApp(App):
    def build(self):
        return Widgets()

if __name__ == '__main__':
    MyApp().run()