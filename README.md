# comma10k

![Completion Progress Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fcomma-pencil-completion-badge.cc.workers.dev%2Fbadge.json)

This is the first 2,000 images of our internal comma10k dataset. After we clean up these new labels, we'll release more. Learn more from [the Medium post](https://medium.com/@comma_ai/crowdsourced-segnet-you-can-help-2e683244a039), or on the [comma.ai discord](http://discord.comma.ai) in the #comma-pencil channel.

![Alt](sample.jpg "First image from the dataset")

It's 10,000 pngs of real driving captured from the comma fleet. It's MIT license, no academic only restrictions or anything.

Run <pre>./viewer.py</pre> to see them with segnet overlay.

## Directories

<pre>
 imgs/  -- The png image files
 masks/ -- PNG segmentation masks (update these!)
 segs/  -- The outputs in probability from our internal segnet (unreleased, too big)
</pre>

## Categories of internal segnet

<pre>
 1 - #402020 - road (all parts, anywhere nobody would look at you funny for driving)
 2 - #ff0000 - lane markings (don't include non lane markings like turn arrows and crosswalks)
 3 - #808060 - undrivable
 4 - #00ff66 - movable (vehicles and people/animals)
 5 - #cc00ff - my car (and anything inside it, including wires, mounts, etc. No reflections)
</pre>

## How can I help?

1. Visit the [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1ZKqku0cAyWY0ELY5L2qsKYYYA2AMGbgAn4p53uoT3v8) (request access to edit the spreadsheet if you haven't already) and put your discord username in the "labeller" column for the mask(s) you're working on and change the status to "In Progress"
2. Start labelling! Useful label tools:
   * [img-labeler](https://erikbernheim.github.io/img-labeler/)
   * The included comma pencil tool
   * An external image manipulation tool such as [GIMP](https://www.gimp.org/downloads/)/[Krita](https://krita.org/) (Free) or [Adobe Photoshop](https://www.adobe.com/products/photoshop.html) (Paid)
If you choose to use an external tool please ensure your color mode is set to 8-bit, and that antialiasing doesn't change the colors on the edges of your mask.

3. Fork this repository to your account using the "Fork" button in the top right
4. Create a **new branch** from the **master** branch, and use your labelling tool of choice to label some images
5. Open a pull request from your new branch to the master branch in the official repository to submit your changes!
6. Visit the #comma-pencil channel on the [comma.ai Discord](http://discord.comma.ai) for the latest news and chat about the project.

### Beginner Tutorial
<a href="https://youtube.com/watch?v=RxqG15zOmCk" title="img-labeler Tutorial Video" rel="noopener noreferer"><img src="https://i.ytimg.com/vi/RxqG15zOmCk/maxresdefault.jpg" width="480px"></a>

## The Goal

![Alt](sample.gif "Animated GIF showing mask")

## Publication

comma10k is still a work in progress. For now, just cite the GitHub link. Once we reach 10k images, we'll release a paper, a train/test split, and a benchmark model. 

For now, we are validating on images ending with "9.png" and are seeing a categorical cross entropy loss of 0.051. Can you beat this?

