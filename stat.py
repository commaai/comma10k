#!/usr/bin/env python3
import subprocess
out = subprocess.check_output("git diff --name-only HEAD 9b327ccde35edf7d9bd51af247e3d785a87f759e masks/0*", shell=True).strip().split(b"\n")
out += subprocess.check_output("git diff --name-only HEAD 675f01fec8ebd430f2781ccdef6c17bd542ad9c5 masks/1*", shell=True).strip().split(b"\n")
out += subprocess.check_output("git diff --name-only HEAD 0c2e5ee5e4f2f72ab0c2e2521344b1035fdaddba masks/h0*", shell=True).strip().split(b"\n")
out += subprocess.check_output("git diff --name-only HEAD 329ff5f6dc6e96476ec09ed3e42d6bd52edc83fc masks/r0*", shell=True).strip().split(b"\n")
with open("files_trainable", "wb") as f:
  f.write(b'\n'.join(out))
print("number labelled %d, percent done: %.2f%%" % (len(out), len(out)/2102.0*100))


