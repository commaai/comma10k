#!/usr/bin/env python3
import os
import requests
import json
import scaleapi

client = scaleapi.ScaleClient(os.getenv("SCALE"))
tl = client.tasks()

for t in tl:
  fil = t.params['attachment']

  if 'comma10k' in fil:
    rfil = fil.split("/")[-1]
    if t.status == "completed":
      url = t.response["annotations"]["combined"]["image"]
      mapping = t.response['labelMapping']
      r = requests.get(url)
      with open("response/%s" % rfil, "wb") as f:
        f.write(r.content)
      with open("response/%s" % rfil.replace(".png", ".json"), "w") as f:
        f.write(json.dumps(mapping))
    elif t.status == "pending":
      # touch pending files
      fn = "response/%s" % rfil
      if not os.path.isfile(fn):
        with open(fn, "wb") as f:
          f.close()


