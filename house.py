#Gary Li
#9/20/17
#house.py

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color

redRectangle = RectangleAsset(125,150,blackOutline,red) #width, heright, outline, fill
redTriangle = PolygonAsset([(100,150), (200,50), (300,150)],blackOutline, red) #list of endpoints
windows = RectangleAsset(35,35,blackOutline,black) #width, heright, outline, fill
door = RectangleAsset(35,50,blackOutline,black) #width, heright, outline, fill

Sprite(redRectangle, (140,150))
Sprite(redTriangle)
Sprite(windows, (150, 175))
Sprite(windows, (220, 175))
Sprite(door, (180, 250))

App().run()
