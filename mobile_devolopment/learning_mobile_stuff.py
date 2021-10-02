import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name:    "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last name:    "))
        self.Lastname = TextInput(multiline=False)
        self.inside.add_widget(self.Lastname)

        self.inside.add_widget(Label(text="Email ID:    "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        lastname = self.Lastname.text
        email = self.email.text

        print("You have submited and here is the submited information",'\n',"Name = ",name,'\n',"Last Name = ", lastname,'\n',"email = ",email)
        quit()

class MyMainApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyMainApp().run()