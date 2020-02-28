#!/usr/bin/env python3
import os
import numpy as np
from tqdm import tqdm
from multiprocessing import Pool

def make_segz(x):
  outp = np.load("segs/"+x)['arr_0'] / 256.0 + 1e-6
  out = outp.argmax(axis=2)
  np.savez_compressed("segz/"+x, out)

if __name__ == "__main__":
  os.makedirs("segz/", exist_ok=True)
  p = Pool(16)
  lst = sorted(os.listdir("segs/"))
  for _ in tqdm(p.imap_unordered(make_segz, lst), total=len(lst)):
    pass

