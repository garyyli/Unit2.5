#Gary Li
#9/26/17
#warmup5.py

from ggame import *

yellow = Color(0xFFFF00, 1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color

yellowDiamond = PolygonAsset([(250,150), (350,-100), (450,150), (350,400)], blackOutline, yellow) #list of endpoints
text = TextAsset('Gary', fill=blue,style='bold 20pt Times')

Sprite(yellowDiamond, (100,100))
Sprite(text, (100,100))
App().run()
