#!/usr/bin/env python3
import os
import sys
from window import Window
import numpy as np
sys.path.append(os.getcwd())
from viewer import fix
from tqdm import tqdm
from PIL import Image

# to generate:
# grep -vIr "\x00" -- */*/ent.txt > /tmp/ents
# cat /tmp/ents | sort -t ":" -k2 -n -r > /tmp/entssort

BASEDIR = "/raid.dell03/runner/comma10k/Comma10k"

win = Window(1164, 874)
cc = 100

dat = open(sys.argv[1]).read().strip().split("\n")
for d in tqdm(dat):
  fn = os.path.join(BASEDIR, d.split(":")[0].replace("/ent.txt", ""))
  dd = sorted(os.listdir(fn))
  print(dd)

  ii = np.array(Image.open(os.path.join(fn, dd[1])))
  segi = fix(Image.open(os.path.join(fn, dd[2])))
  o = 1
  pii = ii*((10-o)/10) + segi*(o/10)

  win.draw(pii)
  while 1:
    kk = win.getkey()
    if kk == ord("z"):
      suf = dd[1][5:]
      outn = "imgs/h%03d_%s" % (cc, suf)
      print("saving ", outn)
      im = Image.fromarray(ii)
      im.save(outn)
      im = Image.fromarray(segi)
      im.save(outn.replace("imgs/", "masks/"))
      cc += 1
      break
    elif kk == ord(" "):
      break



