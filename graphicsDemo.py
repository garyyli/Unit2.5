#Gary Li
#9/20/17
#graphicsDemo.py - intro to ggame

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color

redRectangle = RectangleAsset(200,100,blackOutline,red) #width, heright, outline, fill
blueCircle = CircleAsset(100,blackOutline, blue) #radius, outline, fill
greenEllipse = EllipseAsset(100,50,blackOutline,green) #horizontalradius, verticalradius, outline, fill
blackLine = LineAsset(50, 160, blackOutline) #xEndpoint, yEndpoint, lineStyle
redTriangle = PolygonAsset([(0,0), (120,180), (60,300)],blackOutline, red) #list of endpoints
text = TextAsset('GAAAAAAAAAAAAA', fill=blue,style='bold 30pt Times')

Sprite(redRectangle)
Sprite(blueCircle, (200,200))
Sprite(greenEllipse, (200,400))
Sprite(blackLine)
Sprite(redTriangle)
Sprite(text, (300,300))
App().run()
