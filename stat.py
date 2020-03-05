#!/usr/bin/env python3
import subprocess
out = subprocess.check_output("git diff --name-only HEAD 9b327ccde35edf7d9bd51af247e3d785a87f759e masks/*", shell=True).strip().split(b"\n")
print("percent done: %.2f%%" % (len(out)/1000.0*100))


