from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

Builder.load_file('screens/wheypro/wheypro.kv')
class WheyScreen(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)