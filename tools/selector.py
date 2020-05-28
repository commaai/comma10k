#!/usr/bin/env python3
import os
import sys
import glob
from window import Window
import numpy as np
sys.path.append(os.getcwd())
from viewer import fix
from tqdm import tqdm
from PIL import Image

# to generate:
# grep -vIr "\x00" -- */*/ent.txt > /tmp/ents
# cat /tmp/ents | sort -t ":" -k2 -n -r > /tmp/entssort

BASEDIR = sys.argv[1]

win = Window(1164, 874)
cc = 0

while len(glob.glob("imgs/h%03d*" % cc)) > 0:
  cc += 1
print("starting with %d" % cc)

seen = set([x[len('imgs/h113_'):] for x in glob.glob("imgs/h*")])

# permanent camera occulusions
EXCLUDE_USERS = ["807f77aac0daa4b6", "84e6a31bffe59bee"]

dat = open(sys.argv[2]).read().strip().split("\n")
for d in tqdm(dat):
  fn = os.path.join(BASEDIR, d.split(":")[0].replace("/ent.txt", ""))
  dd = sorted(os.listdir(fn))
  if dd[1][5:] in seen:
    continue
  if dd[1].split("_")[1] in EXCLUDE_USERS:
    continue
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



