#!/usr/bin/env python3
import os
import subprocess

def tx(x):
  if b"/sa" in x:
    b,e = x.split(b'/sa')
    ret = b"%s/%04d%s" % (b,int(e[0:5])+5000, e[5:])
    return ret
  return x


# https://stackoverflow.com/questions/5669621/git-find-out-which-files-have-had-the-most-commits
out = subprocess.check_output("git rev-list --objects --all | awk '$2' | sort -k2 | uniq -cf1 | sort -rn", shell=True).strip().split(b"\n")
fnn = []
al_set = set()
for j in out:
  jj = j.strip().split(b" ")
  if len(jj) != 3:
    continue
  cnt, _, fn = jj
  fn = tx(fn)
  cnt = int(cnt)
  if os.path.isfile(fn) and (fn.startswith(b"masks/") or fn.startswith(b"masks2/")):
    if cnt > 1:
      fnn.append(fn)
    al_set.add(fn)
out = sorted(list(set(fnn)))

missing_count = len(al_set) - len(out)
if missing_count < 20:
  print(f"last {missing_count} mask(s) missing:")
  print(al_set.difference(set(out)))

with open("files_trainable", "wb") as f:
  f.write(b'\n'.join(out))
print("number labelled %d/%d, percent done: %.2f%%" % (len(out), len(al_set), len(out)/len(al_set)*100.))


