# -*- coding: utf-8 -*-

	
import requests

#from PIL import Image
import time

## Pobieranie pliku
r = requests.get('https://github.com/Flop2137/rickrolltestv2/blob/main/Rickroll.jpg', stream=True)

with open('Rickroll.jpg', 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
        if not chunk:
            break
        
        f.write(chunk)
        
        
##        
time.sleep(1.5)
##im = Image.open("C:/Users/Public/BadUSB-ChangeWallpaper/fotka.png")
##im.show()
##time.sleep(1)
