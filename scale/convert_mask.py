#!/usr/bin/env python3
import os
import sys
import glob
import json
import numpy as np
from PIL import Image, ImageColor

basedir = "response" # set to where the JSON/PNGs are located
comma_colormap = {"road":"#402020","unmovable":"#808060","lane_marking":"#ff0000","movable":"#00ff66","my_car":"#cc00ff"}

# list of scaleai labels and what they map to in comma's color space
scaleai_map = {
  "road": [
    "other road marking (crosswalk, stop line, etc...)",
    "other road marking (crosswalk, stop line, etc\.\.\.)",
    "road (all parts, including shoulders)"
  ],
  "my_car": [
    "my car (and anything inside it)"
  ],
  "lane_marking": [
    "lane marking"
  ],
  "unmovable": [
    "undrivable unmovable (grass, buildings, curbs, poles, trees, sidewalks, etc...)",
    "undrivable unmovable (grass, buildings, curbs, poles, trees, sidewalks, etc\.\.\.)",
    "sky",
    "other street signs (speed limit, parking, yield, etc\.\.\. just the sign part)",
    "other street signs (speed limit, parking, yield, etc... just the sign part)",
    "curb",
    "cones and temporary road work signs",
    "traffic light",
    "stop signs (just the sign part)",
  ],
  "movable": [
    "other movable things (people, bikes, animals, etc\.\.\.)",
    "other movable things (people, bikes, animals, etc...)",
    "vehicles (cars, buses, trucks, motorcycles, etc\.\.\.)",
    "vehicles (cars, buses, trucks, motorcycles, etc...)"
  ]
}

def convert_mask(x):
  basename = os.path.splitext(os.path.basename(x))[0]
  jsonFile = basedir+"/"+basename+".json"
  pngFile = basedir+"/"+basename+".png"

  print("Converting file: %s" % pngFile)

  # Read the ScaleAI colormap
  img = Image.open(pngFile)
  img.convert('RGBA')
  scaleai_img = np.array(img)
  red, green, blue, alpha = scaleai_img.T

  with open(jsonFile) as f:
    data = json.load(f)

  for obj in data:
      # Map the ScaleAI label/color to the Comma label/color
      for label in comma_colormap:
          if obj in scaleai_map[label]:
              #print("%s: %s" % (label,obj))

              segment = data[obj]
              if segment:
                  if isinstance(segment, list):
                      # This segment has multiple objects (with diff colors) so replace each one
                      for el in segment:
                          thiscolor = ImageColor.getrgb(el["color"])
                          thiscolorsegment = (red == thiscolor[0]) & (blue == thiscolor[2]) & (green == thiscolor[1])
                          # Replace the color
                          scaleai_img[..., :-1][thiscolorsegment.T] = ImageColor.getrgb(comma_colormap[label])
                  else:
                    thiscolor = ImageColor.getrgb(segment["color"])
                    thiscolorsegment = (red == thiscolor[0]) & (blue == thiscolor[2]) & (green == thiscolor[1])
                    # Replace the color
                    scaleai_img[..., :-1][thiscolorsegment.T] = ImageColor.getrgb(comma_colormap[label])

  img2 = Image.fromarray(scaleai_img)
  img2.save(pngFile)

if __name__ == "__main__":
  lst = sorted(glob.glob(basedir+'/*.png'))
  map(convert_mask, lst)
