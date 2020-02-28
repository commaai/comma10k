# comma10k

In honor of the comma.ai hackathon, which starts today (2/28/2020), we are releasing the first 1,000 images of our internal comma10k dataset. After we clean up these labels, we'll release more.

![Alt](sample.jpg "First image from the dataset")

It's 1,000 pngs of real driving captured from the comma fleet. It's MIT license, no academic only restrictions or anything. It also includes our internal segnet's guess at category.

Run <pre>./viewer.py</pre> to see them with segnet overlay.

## Directories

<pre>
 imgs/ -- The png image files
 segz/ -- The outputs in argmax from our internal segnet
 segs/ -- The outputs in probablity from our internal segnet (unreleased, too big)
</pre>

## Categories of internal segnet

<pre>
 0 - empty
 1 - sky
 2 - road
 3 - road marks (drivable, split into lanes and non lane markings)
 4 - undrivable
 5 - movable (split into vehicles and people/animals?)
 6 - signs and traffic lights (add cones?, add toll booth bar?)
 7 - my car
</pre>

## The Idea

We want to add a data labeller in this repo, such that people can fix the committed labels and submit a pull request for the new ones. Fun hackathon projects abound!

