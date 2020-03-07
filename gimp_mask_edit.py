#!/usr/bin/env python2
from gimpfu import *
import os

mask_colors = {
  'road': (0x40, 0x20, 0x20),
  'lane_markings': (0xff, 0x00, 0x00),
  'undrivable': (0x80, 0x80, 0x60),
  'movable': (0x00, 0xff, 0x66),
  'my_car': (0xcc, 0x00, 0xff),
}


def load_mask_file(image, drawable):
    fn = pdb.gimp_image_get_filename(image)
    mask_fn = os.path.join(os.path.dirname(os.path.dirname(fn)), 'masks', os.path.basename(fn))
    mask_layer = pdb.gimp_file_load_layer(image, mask_fn)
    mask_layer.opacity = 30.0
    mask_layer.name = 'mask'
    pdb.gimp_image_insert_layer(image, mask_layer, None, -1)


def save_mask_file(image, drawable):
    layers = image.layers
    mask_loaded = False
    for layer in layers:
        if layer.name == 'mask':
            mask_loaded = True
            break
    if not mask_loaded:
        pdb.gimp_message("Mask file not loaded yet")
        return

    for layer in layers:
        if layer.name == 'mask':
            mask_loaded = True
            if not pdb.gimp_item_get_visible(layer):
                layer.visible = True
        else:
            if pdb.gimp_item_get_visible(layer):
                layer.visible = False

register(
    "comma10k_load_mask_file",
    "Load Mask File",
    "Load Mask File",
    "https://github.com/nanamiwang",
    "https://github.com/nanamiwang",
    "2020",
    "<Image>/Comma10K/Load Mask File",
    "RGB*, GRAY*",
    [],
    [],
    load_mask_file
)

register(
    "comma10k_save_mask_file",
    "Save Mask File",
    "Save Mask File",
    "https://github.com/nanamiwang",
    "https://github.com/nanamiwang",
    "2020",
    "<Image>/Comma10K/Save Mask File",
    "RGB*, GRAY*",
    [],
    [],
    save_mask_file
)


for cls_name in mask_colors.keys():
    register(
        "comma10k_set_foreground_color_%s" % cls_name,
        "Set FColor to %s" % cls_name,
        "Set FColor to %s" % cls_name,
        "https://github.com/nanamiwang",
        "https://github.com/nanamiwang",
        "2020",
        "<Image>/Comma10K/Set FColor to %s" % cls_name,
        "RGB*, GRAY*",
        [],
        [],
        lambda img, l, cls_name=cls_name: pdb.gimp_context_set_foreground(mask_colors[cls_name])
    )


main()