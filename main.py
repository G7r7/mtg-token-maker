import os
import cv2
from src.fusion_images import fusion_images
from src.build_page import build_page

path_data = './data'
path_out = './out'
output_card_dimension = (936, 672) #lines/columns

if not os.path.exists(path_out):
    os.mkdir(path_out)

cwd = os.getcwd()
dir_path  = os.path.join(cwd, path_data)

cards = []

i = 0

for root, dirs, files in os.walk(dir_path):
    for dirname in dirs:
        for root, dirs, files in os.walk(os.path.join(dir_path, dirname)):
            print(files)
            im1 = cv2.imread(os.path.join(root, files[0]))
            im2 = cv2.imread(os.path.join(root, files[1]))
            im1 = cv2.resize(im1, (output_card_dimension[1], output_card_dimension[0]))
            im2 = cv2.resize(im2, (output_card_dimension[1], output_card_dimension[0]))
            final_card = fusion_images(im1,im2)
            cards.append(final_card)
            print(im1.shape, final_card.shape)	
            # cv2.imwrite(os.path.join(cwd, path_out, str(i) + ".jpg"), final_card)
            i+=1

page = build_page((3,3), cards, output_card_dimension)
cv2.imwrite(os.path.join(cwd, path_out, "page" + str(i) + ".jpg"), page)