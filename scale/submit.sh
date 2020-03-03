#!/bin/bash

# copied from cityscapes https://www.cityscapes-dataset.com/method-details/?submissionID=6526
# added my car, and the three lane markings

# test them on 999

curl "https://api.scale.com/v1/task/segmentannotation" \
  -u "$SCALE" \
  -d callback_url="http://www.example.com/callback" \
  -d instruction="Please segment the image using the given labels." \
  -d attachment_type=image \
  -d attachment="https://raw.githubusercontent.com/commaai/comma10k/master/imgs/0999_e8e95b54ed6116a6_2018-10-22--11-26-21_3_339.png" \
  -d labels="sky" \
  -d labels="road (all parts, including shoulders)" \
  -d labels="curb" \
  -d labels="lane marking" \
  -d labels="other road marking (crosswalk, stop line, etc...)" \
  -d instance_labels="vehicles (cars, buses, trucks, motorcycles, etc...)" \
  -d instance_labels="other movable things (people, bikes, animals, etc...)" \
  -d labels="undrivable unmovable (grass, buildings, curbs, poles, trees, sidewalks, etc...)" \
  -d instance_labels="cones and temporary road work signs" \
  -d instance_labels="stop signs (just the sign part)" \
  -d instance_labels="other street signs (speed limit, parking, yield, etc... just the sign part)" \
  -d instance_labels="traffic light" \
  -d labels="my car (and anything inside it)" \
  -d allow_unlabeled=false

