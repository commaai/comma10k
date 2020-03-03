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
  -d labels="my car (hood, wipers, phone mount, etc...)" \
  -d labels="road" \
  -d labels="lane marking" \
	-d labels="stop line" \
	-d labels="crosswalk" \
  -d labels="other non lane / non stop line / non crosswalk road marking" \
  -d labels="sidewalk" \
  -d labels="building" \
  -d labels="wall" \
  -d labels="fence" \
  -d labels="pole" \
  -d labels="traffic light" \
  -d labels="traffic sign" \
  -d labels="vegetation" \
  -d labels="terrain" \
  -d labels="sky" \
  -d labels="person" \
  -d labels="rider" \
  -d labels="car" \
  -d labels="truck" \
  -d labels="bus" \
  -d labels="train" \
  -d labels="motorcycle" \
  -d labels="bicycle" \
  -d allow_unlabeled=false

