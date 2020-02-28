# comma10k

In honor of the comma.ai hackathon, which starts today (2/28/2020), we are releasing the first 1,000 images of our internal comma10k dataset.

It's 1,000 pngs of real driving captured from the comma fleet. It's also MIT license, no academic only restrictions or anything.

 imgs/ -- The png image files
 segz/ -- The outputs in argmax from our internal segnet
 segs/ -- The outputs in probablity from our internal segnet (unreleased, too big)

## Categories

 0 - empty
 1 - sky
 2 - road
 3 - road marks (drivable)
 4 - undrivable
 5 - movable (split into vehicles and people/animals?)
 6 - signs and traffic lights (add cones?, add toll booth bar?)
 7 - my car

