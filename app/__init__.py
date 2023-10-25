from kivy.app import App
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from .screen import MainWindow

class MainApp(App):
    colors = QueryDict()
    colors.primary = rgba('#9E8')
    def build(self):
        return MainWindow()