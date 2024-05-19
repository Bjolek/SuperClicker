import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

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


    def click(self):
        self.ids.ball.size_hint = (0.5 , 0.5)

        read_data()
        player["score"] += player["power"]
        self.ids.score_lbl.text = "рахунок:" + str(player["score"])
        save_data()
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
