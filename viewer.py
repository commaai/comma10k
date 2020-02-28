#!/usr/bin/env python3
import os
from common.window import Window
import numpy as np
from tqdm import tqdm
from PIL import Image

if __name__ == "__main__":
  win = Window(1164, 874)
  for x in tqdm(sorted(os.listdir("imgs/"))):
    ii = np.array(Image.open("imgs/"+x))
    win.draw(ii)
    win.getkey()
    
