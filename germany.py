#Gary Li
#9/26/17
#germany.py

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)

blackOutline = LineStyle(1,black) #pixels, color

redRectangle = RectangleAsset(200,100,blackOutline,red) #width, heright, outline, fill

Sprite(redRectangle)
App().run()
