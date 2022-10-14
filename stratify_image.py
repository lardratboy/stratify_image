import PIL.Image

def stratify_image(image):
  
  w,h = image.size
  bands = image.split()
  o = PIL.Image.new(mode='L',size=(w*len(bands),h))
  x = 0

  for b in bands:
    o.paste(b,(x,0))
    x += w

  return o
  