#!/usr/bin/env python3
import os
import sys
import numpy as np
from tqdm import tqdm
from PIL import Image

NOSEGS = os.getenv("NOSEGS") is not None

def get_colormap():
  f32 = lambda x: (x % 256, x//256 % 256, x//(256*256) % 256)
  #key = [16777215, 12895458, 2105408, 255, 65484, 6749952, 16737792, 16711884]
  key = [16777215, 0xc4c4e2, 2105408, 255, 0x608080, 6749952, 16737792, 16711884]
  return {i: f32(key[i]) for i in range(len(key))}

def gray_to_color(image):
  W,H = image.shape[0:2]
  colormap = get_colormap()
  c = image.ravel()
  output = np.asarray([colormap[i] for i in c]) 
  output = output.reshape((W, H, 3)).astype(np.uint8)
  return output

def fix(im):
  dat = np.array(im)
  if im.mode == "P":
    # palette image
    pp = np.array(im.getpalette()).reshape((-1, 3)).astype(np.uint8)
    sh = dat.shape
    dat = pp[dat.flatten()].reshape(list(sh)+[3])

  if dat.shape[2] != 3:
    # remove alpha
    dat = dat[:, :, 0:3]
  return dat


if __name__ == "__main__":
  from tools.window import Window
  import pygame
  win = Window(1164, 874)
  lst = sorted(os.listdir("imgs/"))
  if len(sys.argv) > 1:
    #lst = list(filter(lambda x: x.startswith(("%04d" % int(sys.argv[1]))), lst))
    lst = lst[int(sys.argv[1]):]

  if os.getenv("ENTSORT") is not None:
    szz = []
    for x in lst:
      sz = os.stat("segs/"+x+".npz").st_size
      szz.append((sz, x))
    lst = [x[1] for x in sorted(szz, reverse=True)]

  print("")
  print("KEYBOARD COMMANDS:")
  print("right arrow = step forward")
  print("left arrow  = step back")
  print("up arrow    = raise mask opacity")
  print("down arrow  = lower mask opacity")
  print("m           = show/hide mask")
  print("q or escape = quit")
  print("")
  i = 0
  o = 2
  m = True
  p = tqdm(total=len(lst))
  while True:
    x = lst[i]
    p.set_description(x)
    p.n = (i % len(lst)) + 1
    p.refresh()
    while True:
      ii = np.array(Image.open("imgs/"+x))
      if not NOSEGS and os.path.isfile("masks/"+x) and m:
        segi = fix(Image.open("masks/"+x))
        # blend
        ii = ii*((10-o)/10) + segi*(o/10)
      win.draw(ii)
      kk = win.getkey()
      if kk == ord("s"):
        if not os.path.isfile("scale/response/%s" % x):
          print("submitting to scaleapi")
          os.system("scale/submit.sh "+x)
        else:
          print("ALREADY SUBMITTED!")
      elif kk == ord('m'):
        m = not m
      elif kk == pygame.locals.K_UP:
        o = min(10, o+1)
      elif kk == pygame.locals.K_DOWN:
        o = max(0, o-1)
      elif kk in [pygame.locals.K_RIGHT, ord(' '), ord('\n'), ord('\r')]:
        i += 1
        break
      elif kk == pygame.locals.K_LEFT:
        i += -1
        break

