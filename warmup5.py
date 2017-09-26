#Gary Li
#9/26/17
#warmup5.py

from ggame import *

yellow = Color(0xFFFF00, 1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color

yellowDiamond = PolygonAsset([(0,0), (120,180), (60,300), (0,180)], blackOutline, yellow) #list of endpoints
text = TextAsset('Gary', fill=blue,style='bold 30pt Times')

Sprite(yellowDiamond, (200,400))
Sprite(text, (300,300))
App().run()