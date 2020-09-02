#!/usr/bin/env python3

import os
import sys
import numpy as np
from tqdm import tqdm

sys.path.append(os.getcwd())

# This script checks to see if files are in the wrong folder (should be in /masks folder)

# Only these files should exist in the repo
static_list = ['.git', '.github', '.gitignore', 'LICENSE', 'README.md', 'files_trainable', 'imgs', 'masks', 'pencil', 'requirements.txt', 'sample.gif', 'sample.jpg', 'scale', 'runstat.py', 'tools', 'viewer.py', 'make_sa_dataset.sh']

def check_file(x):
  bad = 1
  if x in static_list:
    bad = 0
  else:
    print("Bad file: %s" % x)

  return bad

if __name__ == "__main__":
  lst = sorted(os.listdir("./"))
  
  bads = []
  
  for bad in tqdm(map(check_file, lst), total=len(lst)):
    bads.append(bad)
  
  if any(bads):
    print("THERE ARE %d FILE(S) IN THE WRONG FOLDER" % sum(bads))
    exit(-1)
  else:
    exit(0)
	
