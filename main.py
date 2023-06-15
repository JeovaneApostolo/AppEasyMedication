from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.icon_definitions import md_icons
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.clock import Clock, mainthread

class SplashScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class DashboardScreen(Screen):
    pass

class MedScreen(Screen):
    pass

class AlarmeScreen(Screen):
    def toggle_alarm(self, alarm_num):
        alarm_status_label = self.root.ids[f'alarm{alarm_num}_status']
        current_status = alarm_status_label.text

        if 'Desativado' in current_status:
            alarm_status_label.text = f'Alarm {alarm_num}: Ativado'
        else:
            alarm_status_label.text = f'Alarm {alarm_num}: Desativado'

class ChatScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        # Criando o ScreenManager
        sm = ScreenManager()

        # Adicionando as telas ao ScreenManager
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(MedScreen(name='med'))
        sm.add_widget(AlarmeScreen(name='alarme'))
        sm.add_widget(ChatScreen(name='chat'))

        return sm
    
    def build(self):
        kv = Builder.load_file("telas.kv")
        screen = kv
        return screen


if __name__ == '__main__':
    MyApp().run()