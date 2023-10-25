import os
import importlib

from kivy.core.window import Window

from kaki.app import App

class WorkoutApp(App):
    KV_FILES = {
        os.path.join(os.getcwd(),
                    'screens', 
                    'rootscreen',
                    'root_screen.kv'),
        os.path.join(os.getcwd(),
                    'screens', 
                    'todayworkout',
                    'today_workout.kv'),
        os.path.join(os.getcwd(),
                    'screens', 
                    'allworkout',
                    'all_workout.kv'),
    },
    CLASSES = {
        'rootscreen' : 'root_screen',
        'todayworkout' : 'today_workout',
        'allworkout' : 'all_workout',
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive': True}),
    ]

    def build_app(self):
        import screens.rootscreen.root_screen

        Window.bind(on_keyboard=self.rebuild)
        importlib.reload(screens.rootscreen.root_screen)

        return screens.rootscreen.root_screen.RootScreen()
    
    def rebuild(self, *args):
        if args[1] == 32:
            self.rebuild()

WorkoutApp().run()