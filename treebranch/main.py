from kivy.app import App
from kivy.uix.widget import Widget


class PongGame(Widget):
    pass


class TreebranchApp(App):
    def build(self):
        return PongGame()


if __name__ == "__main__":
    TreebranchApp().run()
