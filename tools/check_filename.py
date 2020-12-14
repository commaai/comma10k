#!/usr/bin/env python3

import os
import sys
import numpy as np
from tqdm import tqdm
import subprocess

sys.path.append(os.getcwd())
filenames = []

def check_file(x):
  bad = 1
  if x.encode() in filenames:
    bad = 0
  else:
    print("Bad filename: %s" % x)

  return bad

if __name__ == "__main__":
  filenames = subprocess.check_output("git ls-files imgs | awk '{sub(/imgs\//,\"\"); print }'", shell=True).strip().split(b"\n")
#  exit(0)
  lst = sorted(os.listdir("masks/"))
  bads = []
  
  for bad in tqdm(map(check_file, lst), total=len(lst)):
    bads.append(bad)
	
  if any(bads):
    print("THERE ARE %d FILE(S) WITH WRONG NAMES" % sum(bads))
    exit(-1)
  else:
    exit(0)
	
