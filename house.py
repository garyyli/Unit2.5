#Gary Li
#9/20/17
#house.py

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color

redRectangle = RectangleAsset(200,100,blackOutline,red) #width, heright, outline, fill
blackLine = LineAsset(50, 160, blackOutline) #xEndpoint, yEndpoint, lineStyle
redTriangle = PolygonAsset([(100,150), (200,50), (300,150)],blackOutline, red) #list of endpoints

Sprite(redRectangle)
Sprite(blackLine)
Sprite(redTriangle)
App().run()
