from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window




class MainApp(App):
    def __init__(self):
        super().__init__()
        self.label=Label(text='моя программа\nВсе работает')
      
    def btn_pressed(self,instance):
       
        button_text = instance.text 
        
        
    def build(self):
        box=BoxLayout()
        #btn=Button(text='vvv')
        #btn.bind(on_press=self.btn_pressed)
        #main_layout = BoxLayout(orientation="vertical")
        
        #main_layout.add_widget(self.solution)


        
        #btn.bind(on_press=self.on_button_press)
        
        btn= Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        btn.bind(on_press=self.on_solution)
       
        box.add_widget(self.label)
       
        box.add_widget(btn)
     
        return box             
  
    def on_solution(self, instance):
        #text = self.solution.text
    #if text:
        #solution = str(eval(self.solution.text))
        self.label.text = 'solution'

if __name__ == '__main__':
    app = MainApp()
    app.run()
        
