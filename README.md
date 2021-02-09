# comma10k

![Completion Progress Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fcomma-pencil-completion-badge.cc.workers.dev%2Fbadge.json)

Learn more from [the Medium post](https://medium.com/@comma_ai/crowdsourced-segnet-you-can-help-2e683244a039), or on the [comma.ai discord](http://discord.comma.ai) in the #comma-pencil channel.

![Alt](sample.jpg "First image from the dataset")

It's 10,000 PNGs of real driving captured from the comma fleet. It's MIT license, no academic only restrictions or anything.

Run <pre>./viewer.py</pre> to see them with segnet overlay.

## Directories

<pre>
 imgs/  -- The PNG image files
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

1. Visit the [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1ZKqku0cAyWY0ELY5L2qsKYYYA2AMGbgAn4p53uoT3v8) (request access to edit the spreadsheet if you haven't already) and put your discord username in the "labeller" column for the mask(s) you're working on and change the status to "In Progress" If you're new, please start off by just doing one so we could leave you feedback. Dont want to do too many just to learn you have to redo them.
2. Spend some time studying already merged masks to see how things are labeled. Use the comma10kviewer to easily do this. 
3. Watch the Beginner Tutorial youtube video below.
4. Start labelling! Useful label tools:
   * [img-labeler](https://erikbernheim.github.io/img-labeler/) (Only compatible with Chrome and Edge. Other browsers like Brave, Firefox, and Opera, even if chromium based, don't work properly. Must also be used with browser zoom and monitor scaling disabled.)
   * The included comma pencil tool
   * An external image manipulation tool such as [GIMP](https://www.gimp.org/downloads/)/[Krita](https://krita.org/) (Free) or [Adobe Photoshop](https://www.adobe.com/products/photoshop.html) (Paid)
If you choose to use an external tool please ensure your color mode is set to 8-bit, and that antialiasing doesn't change the colors on the edges of your mask.

5. Fork this repository to your account using the "Fork" button in the top right
6. Create a **new branch** from the **master** branch, and use your labelling tool of choice to label some images
7. Open a pull request from your new branch to the master branch in the official repository to submit your changes!
8. Visit the #comma-pencil channel on the [comma.ai Discord](http://discord.comma.ai) for the latest news and chat about the project.

## Image Viewing Tools

1. [comma10kviewer](https://spektor56.github.io/comma10kviewer)
2. [comma10kreviewer](https://spektor56.github.io/comma10kreviewer)

### Beginner Tutorial
<a href="https://youtube.com/watch?v=RxqG15zOmCk" title="img-labeler Tutorial Video" rel="noopener noreferer"><img src="https://i.ytimg.com/vi/RxqG15zOmCk/maxresdefault.jpg" width="480px"></a>

## The Goal

![Alt](sample.gif "Animated GIF showing mask")

## Publication

comma10k is still a work in progress. For now, just cite the GitHub link. Once we reach 10k images, we'll release a paper, a train/test split, and a benchmark model. 

For now, we are validating on images ending with "9.png" and are seeing a categorical cross entropy loss of 0.051. Can you beat this?

And it has been beaten with a CCE loss of 0.045, <a href="https://github.com/YassineYousfi/comma10k-baseline">"comma10k-baseline" by YassineYousfi!</a>

Can you beat that?

