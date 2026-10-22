import os
import UnityPy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from PIL import Image


class UnityPyApp(App):

  def build(self):
    layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

    self.status_label = Label(
        text='UnityPy Android Swapper Ready\nLetakkan file .unity3d di memori HP',
        halign='center',
    )
    layout.add_widget(self.status_label)

    btn_process = Button(
        text='Contoh Proses Asset',
        size_hint=(1, 0.3),
        background_color=(0.1, 0.6, 0.8, 1),
    )
    btn_process.bind(on_press=self.run_process)
    layout.add_widget(btn_process)

    return layout

  def run_process(self, instance):
    self.status_label.text = 'Tombol diklik! Menjalankan logika UnityPy...'
    # Masukkan logika UnityPy Anda di sini


if __name__ == '__main__':
  UnityPyApp().run()
