#!/usr/bin/env python
import os
import sys
from tools.lib.framereader import FrameReader
from PIL import Image

cc = 'd'
frn = 600
n = len(os.listdir("imgsd/"))

if __name__ == "__main__":
  print("this is image %d" % n)
  x = sys.argv[1]
  if os.path.isfile(x):
    path = x
  else:
    path = "cd:/"+x.replace("|", "/")+"/"+cc+"camera.hevc"
  fr = FrameReader(path)
  rframe = fr.get(frn, pix_fmt="rgb24")[0]
  fn = "%05d.png" % n
  ii = Image.fromarray(rframe)
  ii.save("imgsd/"+fn)

