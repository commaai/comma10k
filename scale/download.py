#!/usr/bin/env python3
import os
import requests
import json
import scaleapi

client = scaleapi.ScaleClient(os.getenv("SCALE"))
tl = client.tasks()

for t in tl:
  fil = t.params['attachment']
  if 'comma10k' in fil and t.status == "completed":
    url = t.response["annotations"]["combined"]["image"]
    mapping = t.response['labelMapping']
    rfil = fil.split("/")[-1]
    r = requests.get(url)
    with open("response/%s" % rfil, "wb") as f:
      f.write(r.content)
    with open("response/%s" % rfil.replace(".png", ".json"), "w") as f:
      f.write(json.dumps(mapping))




