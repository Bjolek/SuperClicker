import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.window import Window
Window.size = (390,670)


player = {
    "score": 0,
    "power": 1
}

def read_data():
    global player
    try:
        with open("play.json", "r", encoding="utf-8") as file:
            player = json.load(file)
    except:
        print("невдача(((")
def save_data():
    global player
    try:
        with open("play.json", "w", encoding="utf-8") as file:
            json.dump(player, file,indent=3, ensure_ascii=True)
    except:
        print("невдача(((")

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def on_enter(self, *args):
        read_data()
        self.ids.score_lbl.text = "рахунок:" + str(player["score"])

    def switch_to_shop_screen(self):
        self.manager.current = "Shop"

    def click(self):
        self.ids.ball.size_hint = (0.37 , 0.37)

        read_data()
        player["score"] += player["power"]
        self.ids.score_lbl.text = "рахунок:" + str(player["score"])
        save_data()
    def unclick(self):
        self.ids.ball.size_hint = (0.2 , 0.2)


class MenuScreen(Screen):
    pass


class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(ShopScreen(name="Shop"))

        return sm

    def switch_to_main_screen(self):
        self.root.current = "main"


class ShopScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def buy(self, price, power):
        read_data()
        if price <= player["score"]:
            player["score"] -= price
            player["power"] += power
            save_data()

    def go_back_to_main_screen(self):
        self.manager.current = "main"


if __name__ == "__main__":
    app = ClickerApp()
    app.run()
