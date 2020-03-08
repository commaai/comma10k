## Comma10k GIMP plugin and labelling tips
 - A simple GIMP plugin for facilitating labelling comma10k images.
 - Some tips for how to label the images and fine-tune the mask file using the awesome GIMP tool.
## Plugin Installation
Copy [gimp_comma10k_helpers.py](https://github.com/nanamiwang/comma10k/blob/gimp_plugin/gimp_plugin/gimp_comma10k_helpers.py) to the GIMP plugins folder

 - For window, find the plugin folder in GIMP installation folder. For example: <pre>C:\Users\nanami\AppData\Local\Programs\GIMP 2\lib\gimp\2.0\plug-ins</pre>
 - For Ubuntu, the private plugin folder is in user folder, For example: 
     <pre>/home/nanami/.gimp_-2.8/plug-ins</pre>

For Ubuntu, Also check the execution permission of the plugin python file and run "chmod +x" if necessary.

Restart GIMP to load the plugin.

Tested on Ubuntu and Windows10.

The comma10k menu items should show up after successful installation.
![68747470733a2f2f692e6962622e636f2f4d566b366b736e2f696d6167652e706e67](https://user-images.githubusercontent.com/3113052/76161584-bbe78d80-616f-11ea-97d3-a5875df8b11a.png)

## Plugin Usage & Labelling Tips
### Load the image & mask
- Click "Open..." menu in GIMP, locate the comma10k git repo folder and choose a image file.

- Load the existing mask file by clicking the "Load Mask File" menu item. This will locate the mask file in the repo automatically. A layer named "mask" will be created for the mask file, and the opacity will be set to 30.0.
![Load_mask_file1](https://user-images.githubusercontent.com/3113052/76161632-2a2c5000-6170-11ea-879a-550d91bef3db.png)
![Load_mask_file2](https://user-images.githubusercontent.com/3113052/76161668-78d9ea00-6170-11ea-9212-42058c3ac6c5.png)

### Label selected area as specific category
Select some regions using any of the GIMP selection tools(Free Select Tool is a good choice), then click menu "Label Selected Pixels as" and choose a category. This will fill the selected area on the mask layer using the category color.
![label_selected_1](https://user-images.githubusercontent.com/3113052/76161727-fdc50380-6170-11ea-9060-64d66a41b926.png)
![label_selected_2](https://user-images.githubusercontent.com/3113052/76161747-3a90fa80-6171-11ea-8be2-dfd8c1a760c8.png)

### Save the Labels and Update the Mask File
Clicking the plugin "Save Mask File" menu item. This will export the mask layer to PNG file, overwrite the existing mask file in the git repo and reload it in GIMP.
![save_mask](https://user-images.githubusercontent.com/3113052/76161785-89d72b00-6171-11ea-93d4-e0b360a73e65.png)


### Fine-tuning the the labels
Click the subitems of plugin "Set Foreground Color to" menu. This will set the foreground color to the category color, then you can paint on the mask layer using any of the paint tools (PaintBrush as a example). This is useful for fine-tuning some pixels.
![fine_tuning1](https://user-images.githubusercontent.com/3113052/76161821-f3efd000-6171-11ea-97cf-452d85d6954f.png)
![fine_tuning2](https://user-images.githubusercontent.com/3113052/76161858-4a5d0e80-6172-11ea-8432-2418bb1a9145.png)


### A tip for reviewing labels for specific category
 - With the mask layer as current layer, enable the "Select by Color" tool (shortcut key: Shift+O), then click a category on the image, the boundary of the category will show up so that you can see the segmentation effect easier.

