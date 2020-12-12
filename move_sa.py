#!/usr/bin/env python3
import os
saimgs = sorted([x for x in os.listdir('imgs') if x.startswith("sa")])
print(len(saimgs))

for i,x in enumerate(saimgs):
  os.rename("imgs/"+x, "imgs/%4d_%s" % (5000+i,x[8:]))
  os.rename("masks/"+x, "masks/%4d_%s" % (5000+i,x[8:]))

