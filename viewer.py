#!/usr/bin/env python3
import os
from common.window import Window
import numpy as np
from tqdm import tqdm
from PIL import Image


def gray_to_color(image):
  def get_colormap():
    f32 = lambda x: (x % 256, x/256 % 256, x/(256*256) % 256)
    key = [16777215, 12895458, 2105408, 255, 65484, 6749952, 16737792, 16711884]
    return {i: f32(key[i]) for i in range(len(key))}
  W,H = image.shape[0:2]
  colormap = get_colormap()
  c = image.ravel()
  output = np.asarray([colormap[i] for i in c]) 
  output = output.reshape((W, H, 3)).astype(np.uint8)
  return output

if __name__ == "__main__":
  win = Window(1164, 874)
  for x in tqdm(sorted(os.listdir("imgs/"))):
    ii = np.array(Image.open("imgs/"+x))
    if os.path.isfile("segz/"+x+".npz"):
      out = np.load("segz/"+x+".npz")['arr_0']
      segi = gray_to_color(out)

      # blend
      ii = ii*0.8 + segi*0.2
    win.draw(ii)
    win.getkey()
    
