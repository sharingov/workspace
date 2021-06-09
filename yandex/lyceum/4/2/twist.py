from PIL import Image


def twist_image(input_file_name, output_file_name):
    im = Image.open(input_file_name)
    x, y = im.size
    im1 = im.crop((0, 0, x // 2, y))
    im2 = im.crop((x // 2, 0, x, y))
    im.paste(im2)
    im.paste(im1, (x // 2, 0))
    im.save(output_file_name)
