#!/usr/bin/env python3
import os
import pygame
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

if len(sys.argv) > 3:
  mask = sys.argv[3]
else:
  mask = "h%03d"

while len(glob.glob(("imgs/"+mask+"*") % cc)) > 0:
  cc += 1
print("starting with %d" % cc)

seen = set([x.split("_", 1)[1] for x in glob.glob("imgs/*")])

# permanent camera occulusions
EXCLUDE_USERS = ["807f77aac0daa4b6", "84e6a31bffe59bee"]

seek_fn = None
#seek_fn = glob.glob("imgs/"+(mask % (cc-1))+"*")[0].split("_", 1)[1]
#print(seek_fn)

o = 2
dat = open(sys.argv[2]).read().strip().split("\n")
for d in tqdm(dat):
  fn = os.path.join(BASEDIR, d.split(":")[0].replace("/ent.txt", ""))
  dd = sorted(os.listdir(fn))
  if seek_fn is not None:
    #print(dd[1], seek_fn)
    if not dd[1].endswith(seek_fn):
      continue
    seek_fn = None

  if dd[1][5:] in seen:
    continue
  if dd[1].split("_")[1] in EXCLUDE_USERS:
    continue
  print(dd)

  ii = np.array(Image.open(os.path.join(fn, dd[1])))
  segi = fix(Image.open(os.path.join(fn, dd[2])))
  while 1:
    pii = ii*((10-o)/10) + segi*(o/10)
    win.draw(pii)
    kk = win.getkey()
    if kk == ord("z"):
      suf = dd[1][5:]
      outn = ("imgs/"+mask+"_%s") % (cc, suf)
      print("saving ", outn)
      im = Image.fromarray(ii)
      im.save(outn)
      im = Image.fromarray(segi)
      im.save(outn.replace("imgs/", "masks/"))
      cc += 1
      break
    elif kk == pygame.locals.K_UP:
      o = min(10, o+1)
    elif kk == pygame.locals.K_DOWN:
      o = max(0, o-1)
    elif kk == ord(" "):
      break



