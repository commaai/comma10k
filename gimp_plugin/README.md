## Comma10k GIMP plugin and labelling tips
 - A simple GIMP plugin for facilitating labelling comma10k images.
 - Some tips for how to label the images and fine-tune the mask file using the awesome GIMP tool.

## Plugin Installation
Copy [gimp_comma10k_helpers.py](https://github.com/nanamiwang/comma10k/blob/gimp_plugin/gimp_plugin/gimp_comma10k_helpers.py) to the GIMP plugins folder

 - For window, find the plugin folder in GIMP installation folder. For example: <pre>C:\Users\nanami\AppData\Local\Programs\GIMP 2\lib\gimp\2.0\plug-ins</pre>
 - For Ubuntu, the private plugin folder is in user folder, For example: 
     <pre>/home/nanami/.gimp_-2.8/plug-ins/pre>

For Ubuntu, Also check the execution permission of the plugin python file and run "chmod +x" if necessary.

Restart GIMP to load the plugin.

The comma10k menu items should show up after successful installation.
![](https://photos.app.goo.gl/Mxsw92gyQEqrTmqP6)

## Plugin Usage & Labelling Tips
### Load the image & mask
- Open the image in GIMP from the comma10k git repo folder.

- Load the existing mask file by clicking the "Load Mask File" menu item. This will locate the mask file in the repo automatically. A layer named "mask" will be created for the mask file, and the opacity will be set to 30.0.
![](https://i.ibb.co/NKLnXP6/image.png)
![](https://i.ibb.co/F6qq0n2/image.png)

### Label selected area as specific category
Select some regions using any of the GIMP selection tools(Free Select Tool is a good choice), then click menu "Label Selected Pixels as" and choose a category. This will fill the selected area on the mask layer using the category color. You can operate on any layer for this work.
![](https://i.ibb.co/Dp2hX1Y/image.png)

### Update the Mask File
Clicking the plugin "Save Mask File" menu item. This will export the mask layer to PNG file, overwrite the existing mask file in the git repo and reload it in GIMP.
![](https://i.ibb.co/MB6zV2h/image.png)

### Fine-tuning the the labels
Click the subitems of plugin "Set Foreground Color to" menu. This will set the foreground color to the category color, then you can paint on the mask layer using any of the paint tools. This is useful for fine-tuning some pixels.
![](https://i.ibb.co/2MRP55V/image.png)
![](https://i.ibb.co/KrqBBx9/image.png)


### A tip for reviewing labels for specific category
Choose the "Select by Color" tool, click a category on the mask layer, the boundary of the category will show up.

