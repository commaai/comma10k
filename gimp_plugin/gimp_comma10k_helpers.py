#!/usr/bin/env python2
from gimpfu import *
import os
import urllib2
import ssl

label_colors = {
  'Road': (0x40, 0x20, 0x20),
  'Lanemarkings': (0xff, 0x00, 0x00),
  'Undrivable': (0x80, 0x80, 0x60),
  'Movable': (0x00, 0xff, 0x66),
  'Mycar': (0xcc, 0x00, 0xff),
}

label_texts = {
  'Road': 'Road',
  'Lanemarkings': 'Lanemarking',
  'Undrivable': 'Undrivable Area',
  'Movable': 'Movable Object',
  'Mycar': 'My Car',
}

author = 'https://github.com/nanamiwang'
copyright = 'https://github.com/nanamiwang'
date = '2020'

def _find_mask_layer(image):
  mask_layer = None
  for layer in image.layers:
    if layer.name == 'mask':
      return layer


def _mask_file_name(image):
  fn = pdb.gimp_image_get_filename(image)
  return os.path.join(os.path.dirname(os.path.dirname(fn)), 'masks', os.path.basename(fn))


repo_url_base = 'https://github.com/commaai/comma10k/raw/master/masks/'

def _mask_file_url(image):
  fn = pdb.gimp_image_get_filename(image)
  return repo_url_base + os.path.basename(fn)


def _dowload_file(url, local_path, progress_text):
  pdb.gimp_progress_init(progress_text, None)
  try:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    u = urllib2.urlopen(url, context=ctx)
    with open(local_path, 'wb') as f:
      meta = u.info()
      file_size = int(meta.getheaders("Content-Length")[0])
      file_size_dl = 0
      block_sz = 4192
      while True:
        buffer = u.read(block_sz)
        if not buffer:
          break
        file_size_dl += len(buffer)
        f.write(buffer)
        pdb.gimp_progress_update(file_size_dl * 100. / file_size)
  finally:
    pdb.gimp_progress_end()

	
def load_mask_file(image, drawable):
  mask_layer = _find_mask_layer(image)
  if mask_layer != None:
    gimp.message("Mask layer already exists")
    return

  mask_file_path = _mask_file_name(image)
  if os.path.exists(mask_file_path):
    mask_layer = pdb.gimp_file_load_layer(image, _mask_file_name(image))
    mask_layer.opacity = 60.0
    mask_layer.name = 'mask'
  else:
    # Paint to undrivable as default
    pdb.gimp_context_set_foreground(label_colors['Undrivable'])
    mask_layer = pdb.gimp_layer_new(image, image.width, image.height, RGB_IMAGE, "mask", 60.0, LAYER_MODE_NORMAL)
    pdb.gimp_drawable_fill(mask_layer, FILL_FOREGROUND)
    # Start labelling from road
    pdb.gimp_context_set_foreground(label_colors['Road'])
  pdb.gimp_image_insert_layer(image, mask_layer, None, -1)
  image.clean_all()

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
  image.clean_all()


def load_github_mask_file(image, drawable):
  layer_name = 'github mask'
  for layer in image.layers:
    if layer.name == layer_name:
      pdb.gimp_image_remove_layer(image, layer)
      break
  url = _mask_file_url(image)
  progress_text = 'Downloading mask for {}'.format(url.split('/')[-1])
  tmp_png_fn = pdb.gimp_temp_name('png')
  _dowload_file(url, tmp_png_fn, progress_text)
  if not os.path.exists(tmp_png_fn):
    pdb.gimp_message('Downloading from github failed.')
    return
  github_mask_layer = pdb.gimp_file_load_layer(image, tmp_png_fn)
  github_mask_layer.opacity = 90.0
  github_mask_layer.name = layer_name
  pdb.gimp_image_insert_layer(image, github_mask_layer, None, -1)
  github_mask_layer.visible = True
  mask_layer = _find_mask_layer(image)
  if mask_layer != None:
    mask_layer.opacity = 90.0
    return


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
  author,
  copyright,
  date,
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
  author,
  copyright,
  date,
  "<Image>/Comma10K/Save Mask to File",
  "RGB*, GRAY*",
  [],
  [],
  save_mask_file
)

register(
  "comma10k_load_github_mask_file",
  "Load the old Mask File from github.com",
  "Load the old Mask File from github.com",
  author,
  copyright,
  date,
  "<Image>/Comma10K/Load Old Mask from github",
  "RGB*, GRAY*",
  [],
  [],
  load_github_mask_file
)

for category_name in label_colors.keys():
  register(
    "comma10k_set_foreground_color_%s" % category_name,
    "Set FColor to %s" % category_name,
    "Set FColor to %s" % category_name,
    author,
    copyright,
    date,
    "<Image>/Comma10K/Set Foreground Color to/%s" % label_texts[category_name],
    "RGB*, GRAY*",
    [],
    [],
    lambda img, l, category_name=category_name: pdb.gimp_context_set_foreground(label_colors[category_name])
  )

  register(
    "comma10k_label_selected_pixels_as_%s" % category_name,
    "Label selected pixels as %s" % category_name,
    "Label selected pixels as %s" % category_name,
    author,
    copyright,
    date,
    "<Image>/Comma10K/Label Selected Pixels as/%s" % label_texts[category_name],
    "RGB*, GRAY*",
    [],
    [],
    lambda img, l, category_name=category_name: label_selected_pixels(img, l, category_name)
  )

main()
