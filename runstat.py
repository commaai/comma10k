#!/usr/bin/env python3
import os
import subprocess
# https://stackoverflow.com/questions/5669621/git-find-out-which-files-have-had-the-most-commits
out = subprocess.check_output("git rev-list --objects --all | awk '$2' | sort -k2 | uniq -cf1 | sort -rn", shell=True).strip().split(b"\n")
fnn = []
al = 0
al_set = set()
for j in out:
  jj = j.strip().split(b" ")
  if len(jj) != 3:
    continue
  cnt, _, fn = jj
  cnt = int(cnt)
  if os.path.isfile(fn) and fn.startswith(b"masks/"):
    if cnt > 1:
      fnn.append(fn)
    al += 1
    al_set.add(fn)
out = sorted(fnn)

missing_count = al - len(out)
if missing_count < 20:
  print(f"last {missing_count} mask(s) missing:")
  print(al_set.difference(set(out)))

with open("files_trainable", "wb") as f:
  f.write(b'\n'.join(out))
print("number labelled %d/%d, percent done: %.2f%%" % (len(out), al, len(out)/al*100.))


