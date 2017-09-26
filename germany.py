#Gary Li
#9/26/17
#germany.py

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)

blackOutline = LineStyle(1,black)
redOutline = LineStyle(1,red)
yellowOutline = LineStyle(1,yellow)

blackRectangle = RectangleAsset(500,100,blackOutline,black)
redRectangle = RectangleAsset(500,100,redOutline,red)
yellowRectangle = RectangleAsset(500,100,yellowOutline,yellow)

Sprite(blackRectangle)
Sprite(redRectangle,(0,100))
Sprite(yellowRectangle,(0,200))

App().run()
