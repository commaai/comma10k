#!/usr/bin/env python2
from gimpfu import *
import os

label_colors = {
  'Road': (0x40, 0x20, 0x20),
  'Lanemarkings': (0xff, 0x00, 0x00),
  'Undrivable': (0x80, 0x80, 0x60),
  'Movable': (0x00, 0xff, 0x66),
  'Mycar': (0xcc, 0x00, 0xff),
}


def _find_mask_layer(image):
  mask_layer = None
  for layer in image.layers:
    if layer.name == 'mask':
      return layer


def _mask_file_name(image):
  fn = pdb.gimp_image_get_filename(image)
  return os.path.join(os.path.dirname(os.path.dirname(fn)), 'masks', os.path.basename(fn))


def load_mask_file(image, drawable):
  mask_layer = _find_mask_layer(image)
  if mask_layer != None:
    gimp.message("Mask file already loaded")
    return

  mask_layer = pdb.gimp_file_load_layer(image, _mask_file_name(image))
  mask_layer.opacity = 30.0
  mask_layer.name = 'mask'
  pdb.gimp_image_insert_layer(image, mask_layer, None, -1)


def save_mask_file(image, drawable):
  mask_layer = _find_mask_layer(image)
  if not mask_layer:
    gimp.message("Mask file not loaded yet")
    return
  pdb.gimp_selection_none(image)
  mask_fn = _mask_file_name(image)
  pdb.file_png_save2(image, mask_layer, mask_fn, mask_fn, 0, 9, 0, 0, 0, 0, 0, 0, 0)
  pdb.gimp_image_remove_layer(mask_layer)
  load_mask_file(image, drawable)


def label_selected_pixels(image, drawable, category_name):
  mask_layer = _find_mask_layer(image)
  if not mask_layer:
    gimp.message("Mask file not loaded yet")
    return
  if pdb.gimp_selection_is_empty(image):
    pdb.gimp_message("You must first select a region.")
    return
  pdb.gimp_context_set_foreground(label_colors[category_name])
  pdb.gimp_edit_fill(mask_layer, 0)
  pdb.gimp_selection_none(image)
  mask_layer.visible = True

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


for category_name in label_colors.keys():
  register(
    "comma10k_set_foreground_color_%s" % category_name,
    "Set FColor to %s" % category_name,
    "Set FColor to %s" % category_name,
    "https://github.com/nanamiwang",
    "https://github.com/nanamiwang",
    "2020",
    "<Image>/Comma10K/Set Foreground Color to/%s" % category_name,
    "RGB*, GRAY*",
    [],
    [],
    lambda img, l, category_name=category_name: pdb.gimp_context_set_foreground(label_colors[category_name])
  )

  register(
    "comma10k_label_selected_pixels_as_%s" % category_name,
    "Label selected pixels as %s" % category_name,
    "Label selected pixels as %s" % category_name,
    "https://github.com/nanamiwang",
    "https://github.com/nanamiwang",
    "2020",
    "<Image>/Comma10K/Label Selected Pixels as/%s" % category_name,
    "RGB*, GRAY*",
    [],
    [],
    lambda img, l, category_name=category_name: label_selected_pixels(img, l, category_name)
  )

main()
