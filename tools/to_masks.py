#!/usr/bin/env python3
import os
import sys
sys.path.append(os.getcwd())
import numpy as np

from tqdm import tqdm
from multiprocessing import Pool
from viewer import gray_to_color
from PIL import Image

def make_segz(x):
  outp = np.load("segs/"+x)['arr_0'] / 256.0 + 1e-6
  out = outp.argmax(axis=2)
  im = Image.fromarray(gray_to_color(out))
  im.save("masks/"+x.replace(".npz", ""))

if __name__ == "__main__":
  os.makedirs("masks/", exist_ok=True)
  p = Pool(16)
  lst = sorted(os.listdir("segs/"))
  lst = list(filter(lambda x: not os.path.isfile("masks/"+x.replace(".npz", "")), lst))
  print("running %d" % len(lst))
  for _ in tqdm(p.imap_unordered(make_segz, lst), total=len(lst)):
    pass

