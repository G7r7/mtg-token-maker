import numpy as np

def reduce_image(im, top=True):
    if top:
        im_part1 = im[0:22,:]
        im_part2 = im[35:,:]
    else:
        im_part1 = im[0:-35,:]
        im_part2 = im[-23:-1,:]

    im_reduced = np.append(im_part1,im_part2, axis=0)
    return im_reduced