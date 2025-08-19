import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"
os.environ["KIVY_NO_ARGS"] = "1"
os.environ["KIVY_WINDOW"] = "sdl2"
os.environ["KIVY_METRICS_DENSITY"] = "1"
os.environ["KIVY_INPUT_PROVIDERS"] = "mouse"

from kivy.clock import Clock
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics.texture import Texture
from pyzbar.pyzbar import decode
import cv2
import qrcode

class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.cam = cv2.VideoCapture(0)

        self.img = Image()
        self.add_widget(self.img)

        self.txt = TextInput(hint_text='Type text for QR', size_hint_y=0.1)
        self.add_widget(self.txt)

        self.btn = Button(text='Make QR', size_hint_y=0.1)
        self.btn.bind(on_press=self.make_qr)
        self.add_widget(self.btn)

        Clock.schedule_once(lambda dt: self.read_qr(), 0)

    def read_qr(self, *args):
        ok, frame = self.cam.read()
        if ok:
            data = decode(frame)
            for item in data:
                print("Found:", item.data.decode())

            buf = cv2.flip(frame, 0).tobytes()
            tex = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            tex.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.img.texture = tex

        self.img.canvas.ask_update()
        App.get_running_app().root_window.canvas.ask_update()
        Clock.schedule_interval(self.read_qr, 1.0 / 30)

    def make_qr(self, instance):
        text = self.txt.text
        if text:
            pic = qrcode.make(text)
            pic.save("my_qr.png")
            print("QR saved as my_qr.png")

class MyApp(App):
    def build(self):
        return MyBox()

MyApp().run()