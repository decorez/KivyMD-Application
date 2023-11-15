from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.clock import Clock
from kivy.utils import rgba, QueryDict
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import SwapTransition
from kivy.properties import StringProperty, NumericProperty, ColorProperty, ListProperty

Builder.load_file('screens/home/home.kv')
class Home(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        colors = App.get_running_app().colors
        products = [
            {
                'name': 'Evolene',
                'source': 'assets/images/evolene.png',
                'avatar': 'assets/images/evolene.png',
                'price': 25,
                'color': colors.success,
                'categories': ['popular', 'discounts']
            },
            {
                'name': 'Nutricost',
                'source': 'assets/images/nutricost.jpg',
                'avatar': 'assets/images/nutricost.jpg',
                'price': 32,
                'color': colors.primary,
                'categories': ['popular', 'isolate powder']
            },
            {
                'name': 'Optimum Nutrition',
                'source': 'assets/images/optimumnutrition.png',
                'avatar': 'assets/images/optimumnutrition.png',
                'price': 25,
                'color': colors.danger,
                'categories': ['popular', 'gold standard']
            },
            {
                'name': 'Kaged',
                'source': 'assets/images/kaged.jpg',
                'avatar': 'assets/images/kaged.jpg',
                'price': 28.45,
                'color': colors.success,
                'categories': ['popular', 'discounts']
            },
            {
                'name': 'Levels Grass Fed',
                'source': 'assets/images/levels.jpg',
                'avatar': 'assets/images/levels.jpg',
                'price': 28.45,
                'color': colors.success,
                'categories': ['popular']
            },
        ]

        specials = [{
                'name': 'Optimum Nutrition',
                'source': 'assets/images/optimumnutrition.png',
                'avatar': 'assets/images/optimumnutrition.png',
                'price': 28.45,
                'color': colors.success,
                'categories': ['popular']
            },
            {
                'name': 'Kaged',
                'source': 'assets/images/kaged.jpg',
                'avatar': 'assets/images/kaged.jpg',
                'price': 31.25,
                'color': colors.danger,
                'categories': ['popular', 'discount']
            },
            {
                'name': 'Nutricost',
                'source': 'assets/images/nutricost.jpg',
                'avatar': 'assets/images/nutricost.jpg',
                'price': 32.5,
                'color': colors.warning,
                'categories': ['popular', 'discount']
            },
            ]

        prods = self.ids.products
        prods.clear_widgets()
        for product in products:
            p = Product()
            p.name = product['name']
            p.price = product['price']
            p.bcolor = product['color']
            p.source = product['avatar']
            p.back = product['source']
            p.bind(on_release=self.view_product)

            prods.add_widget(p)

        spec = self.ids.specials
        spec.clear_widgets()
        for product in reversed(specials):
            p = Special()
            p.name = product['name']
            p.price = product['price']
            p.bcolor = product['color']
            p.source = product['avatar']
            p.back = product['source']
            p.bind(on_release=self.view_product)

            spec.add_widget(p)

    def view_product(self, product):
        view = App.get_running_app().root.ids.whey_screen
        mngr = App.get_running_app().root.ids.scrn_mngr

        view.name = product.name
        view.price = product.price
        view.source = product.back
        view.bcolor = product.bcolor

        mngr.transition = SwapTransition()
        mngr.current = 'scrn_whey'

class Product(ButtonBehavior, BoxLayout):
    name = StringProperty("")
    source = StringProperty("")
    back = StringProperty("")
    bcolor = ColorProperty([1,1,1,1])
    price = NumericProperty(0.0)
    radius = NumericProperty(dp(18))
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class Special(ButtonBehavior, BoxLayout):
    name = StringProperty("")
    source = StringProperty("")
    bcolor = ColorProperty([1,1,1,1])
    price = NumericProperty(0.0)
    extras = ListProperty([])
    radius = NumericProperty(dp(18))
    def __init__(self, **kw) -> None:
        super().__init__(**kw)