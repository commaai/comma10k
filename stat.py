#!/usr/bin/env python3
import subprocess
out = subprocess.check_output("git diff --name-only HEAD 9b327ccde35edf7d9bd51af247e3d785a87f759e masks/*", shell=True).strip().split(b"\n")
with open("files_trainable", "wb") as f:
  f.write(b'\n'.join(out))
print("number labelled %d, percent done: %.2f%%" % (len(out), len(out)/1000.0*100))


