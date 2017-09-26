#Gary Li
#9/26/17
#name.py

from ggame import *

name = input('Enter your name: ')
color = input('Enter an RGB color code: ')

textColor = Color(0xcolor, 1)

text = TextAsset(name, fill=textcolor,style='bold 30pt Times')

Sprite(text, (300,300))
App().run()