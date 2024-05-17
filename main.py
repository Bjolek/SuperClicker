from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def click(self):
        self.ids.ball.size_hint = (0.5 , 0.5)

    def unclick(self):
        self.ids.ball.size_hint = (0.3 , 0.3)


class MenuScreen(Screen):
    pass


class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(MainScreen(name="main"))
        return sm

    def switch_to_main_screen(self):
        self.root.current = "main"


if __name__ == "__main__":
    app = ClickerApp()
    app.run()
