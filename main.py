import os
import cv2
import numpy as np
from src.fusion_images import fusion_images
from src.build_page import build_page

path_data = './data'
path_out = './out'
output_card_dimension = (936, 672) #lines/columns
output_page_layout = (3,3)
cards_per_page = output_page_layout[0]*output_page_layout[1]

if not os.path.exists(path_out):
    os.mkdir(path_out)

cwd = os.getcwd()
dir_path  = os.path.join(cwd, path_data)

cards = []

i = 0

def sharpen(img):
    kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
    sharpen_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
    return sharpen_img

for root, dirs, files in os.walk(dir_path):
    for dirname in dirs:
        for root, dirs, files in os.walk(os.path.join(dir_path, dirname)):
            print(files)
            im1 = cv2.imread(os.path.join(root, files[0]))
            im2 = cv2.imread(os.path.join(root, files[1]))
            im1 = cv2.resize(im1, (output_card_dimension[1], output_card_dimension[0]))
            im2 = cv2.resize(im2, (output_card_dimension[1], output_card_dimension[0]))
            final_card = fusion_images(im1,im2)
            final_card = sharpen(final_card)
            cards.append(final_card)
            print(im1.shape, final_card.shape)	
            # cv2.imwrite(os.path.join(cwd, path_out, str(i) + ".jpg"), final_card)
            i+=1

print(cards_per_page)
for i in range(0,len(cards), cards_per_page):
    page = build_page(output_page_layout, cards[i:i+cards_per_page], output_card_dimension)
    cv2.imwrite(os.path.join(cwd, path_out, "page" + str(i) + ".jpg"), page)