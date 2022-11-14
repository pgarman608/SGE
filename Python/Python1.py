import pickle
import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix import label,button,floatlayout,widget,boxlayout
from kivy.config import Config
kivy.config.Config.set('graphics','resizable', False)

class caja(boxlayout.BoxLayout):
    None
class Iniciador(App):
    title = "Lista de Videojuegos|Pablo García"
    def build(self):
        return caja()
"""
videojuegos = [{"Zelda",18}]
fileWriter = open("videojuegos.txt","wb")
fileReader = open("videojuegos.txt","rb")
pickle.dump(videojuegos, fileWriter)
fileWriter.close()
videojuegos1 = pickle.load(fileReader)
fileReader.close()
print(videojuegos1)
"""
if __name__ == '__main__':
    Iniciador().run()