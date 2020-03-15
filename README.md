# comma10k

![Completion Progress Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fcomma-pencil-completion-badge.cc.workers.dev%2Fbadge.json)

We are releasing the first 1,000 images of our internal comma10k dataset. After we clean up these labels, we'll release more. Learn more from [the Medium post](https://medium.com/@comma_ai/crowdsourced-segnet-you-can-help-2e683244a039), or on the [comma.ai discord](http://discord.comma.ai) in the #comma-pencil channel.

![Alt](sample.jpg "First image from the dataset")

It's 1,000 pngs of real driving captured from the comma fleet. It's MIT license, no academic only restrictions or anything. It also includes our internal segnet's guess at category.

Run <pre>./viewer.py</pre> to see them with segnet overlay.

## Directories

<pre>
 imgs/  -- The png image files
 masks/ -- PNG segmentation masks (update these!)
 segs/  -- The outputs in probablity from our internal segnet (unreleased, too big)
</pre>

## Categories of internal segnet

<pre>
 0 - #ffffff - empty
 1 -         - sky (deprecated, now undrivable)
 2 - #402020 - road (all parts, including shoulders, don't include private driveways but include public)
 3 - #ff0000 - lane markings (don't include non lane markings like turn arrows and crosswalks)
 4 - #808060 - undrivable
 5 - #00ff66 - movable (split into vehicles and people/animals?, actually don't)
 6 -         - signs and traffic lights (deprecated, now undrivable)
 7 - #cc00ff - my car (and anything inside it, including wires, mounts, etc...)
</pre>

## How can I help?

Start labelling!

Useful label tools:
 - The included comma pencil tool
 - An external image manipulation tool such as [GIMP](https://www.gimp.org/downloads/) (Free) or [Adobe Photoshop](https://www.adobe.com/products/photoshop.html) (Paid)
If you choose to use an external tool please ensure your color mode is set to 8-bit, and that antialiasing doesn't change the colors on the edges of your mask.

1. Create an Issue on this repository to indicate which images you intend to label. This is to ensure we don't have two people working on one at the same time, which would be a waste of time.
2. Fork this repository to your account using the "Fork" button in the top right
3. Clone your fork, and use your labelling tool of choice to label some images
4. Open a pull request to the official repository to submit your changes!

### Using the comma pencil tool (only works with MacOS/Linux)

See the `pencil` folder. 

```
cd pencil
pip install -r requirements.txt
python server.py
```

Then open a browser window to http://localhost:5000/

## The Goal

![Alt](sample.gif "Animated GIF showing mask")
