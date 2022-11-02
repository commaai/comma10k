#!/usr/bin/env python3
import os
import sys
sys.path.append(os.getcwd())
import numpy as np
from viewer import fix, get_colormap
from tqdm import tqdm
from multiprocessing import Pool
from PIL import Image
import requests
import re

colormap = get_colormap()
base_dir = "masks/" # default to old set
size_dict = {
  "masks/": (874, 1164, 3),
  "masks2/": (1208, 1928, 3),
  "masksd/": (1208, 1928, 3)
}

onlycheck = os.getenv("ONLYCHECK") is not None
pr_num = os.getenv("PRNUM")
if pr_num is not None:
  api_url = "https://api.github.com/repos/commaai/comma10k/pulls/"+pr_num+"/files?per_page=100"

def get_base_dir(filename, pattern="^masks\w*/"):
  match = re.search(pattern, filename)
  if match is not None:
    return match.group(0)

  return None

def get_pr(pattern="^masks\w*/"):
  response = requests.get(api_url)
  file_list = []

  # Credit to @pjlao307 for the below
  # Use first file in the PR to determine what dir to use then use this value anywhere the correct folder is needed
  # This assumes all files in the PR are in the same folder so this will break if that's not the case
  global base_dir, colormap
  base_dir = get_base_dir(response.json()[0]['filename'], pattern=pattern)
  colormap = get_colormap(True, base_dir)

  for item in response.json():
    if base_dir is not None:
      file_list.append(item["filename"].replace(base_dir,""))

  return file_list

def canon_mask(x):
  segi = fix(Image.open(base_dir + x))

  if segi.shape != size_dict[base_dir]:
    print(x+" HAS BAD SHAPE", segi.shape)
    return True

  #print(x, segi.shape, segi.dtype)
  check = segi.reshape(-1, 3)

  ok = np.zeros(check.shape[0], dtype=bool)
  for v in colormap.values():
    okk = check == np.array(v)
    okk = np.all(okk, axis=1)
    ok |= okk

  bad = False

  if not np.all(ok):
    print(x+" HAS %d pixels with BAD COLORS" % sum(np.logical_not(ok)))
    print(check[np.logical_not(ok)])
    bad = True
    """
    cva = np.array(list(colormap.values()))
    maxb = 0
    for i in np.argwhere(np.logical_not(ok)):
      vv = np.mean((check[i] - cva)**2, axis=1)
      col = np.argmin(vv)
      maxb = max(vv[col], maxb)
      if maxb >= 20:
        break
      #print(i, check[i], col, vv[col])
      check[i] = cva[col]
    if maxb < 20:
      print("FIXED", maxb)
      segi = check.reshape(segi.shape)
    else:
      print("COULDN'T FIX", maxb)
    """

  if not onlycheck:
    im = Image.fromarray(segi)
    im.save(base_dir+x)

  return bad

if __name__ == "__main__":
  lst = sorted(os.listdir(base_dir))
  if len(sys.argv) > 1:
    canon_mask(lst[int(sys.argv[1])])
    exit(0)

  bads = []

  if onlycheck:
    # Only process changed files, do this by pulling from the PR files list from GitHub API
    if pr_num:
      lst = get_pr()

    for bad in tqdm(map(canon_mask, lst), total=len(lst)):
      bads.append(bad)
  else:
    p = Pool(16)
    for bad in tqdm(p.imap_unordered(canon_mask, lst), total=len(lst)):
      if bad:
        print("GOT BAD")
      bads.append(bad)

  if any(bads):
    print("THERE ARE %d BAD IMAGES IN THE DATASET" % sum(bads), list(np.where(bads)[0]))
    ALLOWED_BAD = 0
    if sum(bads) > ALLOWED_BAD:
      exit(-1)
    else:
      # TODO: as you fix the bad images, lower ALLOWED_BAD
      exit(0)
  else:
    exit(0)
