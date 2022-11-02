#!/usr/bin/env python3
import os
import sys
sys.path.append(os.getcwd())
import numpy as np
from tqdm import tqdm
from multiprocessing import Pool
from PIL import Image
import requests
import re
from canonicialize_masks import get_base_dir

base_dir = "imgs/" # default to old set
size_dict = {
  "imgs/": (874, 1164, 3),
  "imgs2/": (1208, 1928, 3),
  "imgsd/": (1208, 1928, 3)
}

pr_num = os.getenv("PRNUM")
if pr_num is not None:
  api_url = "https://api.github.com/repos/commaai/comma10k/pulls/"+pr_num+"/files?per_page=100"

def get_pr(pattern="^imgs\w*/"):
  response = requests.get(api_url)
  file_list = []

  # Credit to @pjlao307 for the below
  # Use first file in the PR to determine what dir to use then use this value anywhere the correct folder is needed
  # This assumes all files in the PR are in the same folder so this will break if that's not the case
  global base_dir, colormap
  base_dir = get_base_dir(response.json()[0]['filename'], pattern=pattern)

  for item in response.json():
    if base_dir is not None:
      file_list.append(item["filename"].replace(base_dir,""))

  return file_list

def check_img_size(x):
  img = np.array(Image.open(base_dir + x))

  if img.shape != size_dict[base_dir]:
    print(x+" HAS BAD SHAPE", img.shape)
    return True

  return False

if __name__ == "__main__":
  lst = sorted(os.listdir(base_dir))
  bads = []

  # Only process changed files, do this by pulling from the PR files list from GitHub API
  if pr_num:
    lst = get_pr(pattern="^imgs\w*/")
    print(lst)

  for bad in tqdm(map(check_img_size, lst), total=len(lst)):
    bads.append(bad)

  if any(bads):
    print("THERE ARE %d BAD IMAGES IN THE DATASET" % sum(bads), list(np.where(bads)[0]))
    ALLOWED_BAD = 0
    exit(-1)
