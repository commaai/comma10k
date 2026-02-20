#!/usr/bin/env python3
import os, subprocess
from PIL import Image
from collections import defaultdict

def remap_sa_path(x):
  if b"/sa" in x:
    b,e = x.split(b'/sa')
    ret = b"%s/%04d%s" % (b,int(e[0:5])+5000, e[5:])
    return ret
  return x

MASK_DIRS = [b"masks/", b"masks2/", b"masksd/"]
IMG_DIRS  = {b"masks/": b"imgs/", b"masks2/": b"imgs2/", b"masksd/": b"imgsd/"}
MIN_COMMITS = {b"masks/": 1, b"masks2/": 1, b"masksd/": 0}

# count commits per file by path
raw = subprocess.check_output("git log --all --name-only --format='' | grep . | sort | uniq -c", shell=True).strip().split(b"\n")

num_commits_map = {}
al_sets = defaultdict(set)
num_commits_hists = defaultdict(lambda: defaultdict(int))

for j in raw:
  jj = j.strip().split(b" ", 1)
  if len(jj) != 2:
    continue
  num_commits, mask_path = jj
  mask_path = remap_sa_path(mask_path)
  num_commits = int(num_commits)
  mask_dir = next((d for d in MASK_DIRS if mask_path.startswith(d)), None)
  if mask_dir is None or not os.path.isfile(mask_path):
    continue
  if Image.open(mask_path).mode not in ('RGB', 'RGBA'):
    print(f"skipping {mask_path} (mode {Image.open(mask_path).mode})")
    continue
  al_sets[mask_dir].add(mask_path)
  num_commits_hists[mask_dir][num_commits] += 1
  if mask_path not in num_commits_map:
    num_commits_map[mask_path] = num_commits

img_totals = {mask_dir: len(os.listdir(IMG_DIRS[mask_dir])) for mask_dir in MASK_DIRS}
total_all = sum(img_totals.values())
trainable = sorted(mask_path for mask_path, num_commits in num_commits_map.items()
                   if num_commits > MIN_COMMITS[next(d for d in MASK_DIRS if mask_path.startswith(d))])
for mask_dir in MASK_DIRS:
  total = img_totals[mask_dir]
  labeled = sum(1 for mask_path in al_sets[mask_dir] if num_commits_map.get(mask_path, 0) > MIN_COMMITS[mask_dir])
  print(f"{mask_dir.decode()}: {labeled}/{total} labeled ({labeled/total*100.:.2f}%)")
  hist = num_commits_hists[mask_dir]
  for num_commits in sorted(hist):
    print(f"  num_commits={num_commits:2d}: {hist[num_commits]} files")

with open("files_trainable", "wb") as f:
  f.write(b'\n'.join(trainable))
pct = len(trainable)/total_all*100. if total_all else 0.
print(f"\nfiles_trainable total: {len(trainable)}/{total_all} ({pct:.2f}%)")
