from kivy.app import App
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from .screen import MainWindow

class MainApp(App):
    colors = QueryDict()
    colors.primary = rgba('#8ee3fa')
    colors.secondary = rgba('#1B0B42')
    colors.warning = rgba('#F4D73C')
    colors.danger = rgba('#E86767')
    colors.success = rgba('#88D7CF')
    colors.white = rgba('#FFFFFF')
    colors.dgrey = rgba('#36454F')
    colors.grey = rgba('#C4C4C4')
    colors.black = rgba('#000000')

    fonts = QueryDict()
    fonts.heading = 'assets/fonts/Nunito-Bold.ttf'
    fonts.subheading = 'assets/fonts/Nunito-SemiBold.ttf'
    fonts.body = 'assets/fonts/Nunito-Regular.ttf'
    fonts.size = QueryDict()
    fonts.size.h1 = sp(24)
    fonts.size.h2 = sp(22)
    fonts.size.h3 = sp(18)
    fonts.size.h4 = sp(16)
    fonts.size.h5 = sp(14)
    fonts.size.h6 = sp(12)

    def build(self):
        return MainWindow()