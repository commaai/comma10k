#!/usr/bin/env python3
import os
from tqdm import tqdm
from PIL import Image
from multiprocessing import Pool

def to_jpeg(fn):
  fn = "imgs/"+fn

  img = Image.open(fn)
  img.save(fn.replace(".png", ".jpg"), quality=80)

if __name__ == "__main__":
  lst = sorted(filter(lambda x: x.endswith(".png"), os.listdir("imgs/")))

  p = Pool(16)
  for _ in tqdm(p.imap_unordered(to_jpeg, lst), total=len(lst)):
    pass
