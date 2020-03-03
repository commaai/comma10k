#!/usr/bin/env python3
import os
import sys
sys.path.append(os.getcwd())
from viewer import fix
from tqdm import tqdm
from multiprocessing import Pool
from PIL import Image

def canon_mask(x):
  segi = fix(Image.open("masks/"+x))
  #print(x, segi.shape, segi.dtype)
  im = Image.fromarray(segi)
  im.save("masks/"+x)

if __name__ == "__main__":
  p = Pool(16)
  lst = sorted(os.listdir("masks/"))
  for _ in tqdm(p.imap_unordered(canon_mask, lst), total=len(lst)):
    pass

