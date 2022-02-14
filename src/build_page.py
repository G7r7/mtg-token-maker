import numpy as np

def build_page(dimension, card_list, card_dimension):
    page = np.ones((0, card_dimension[1]*dimension[1], 3))*255
    i = 0
    row = np.ones((card_dimension[0], 0, 3))*255
    for card in card_list:
        i+=1
        row = np.append(row, card, axis=1)
        if i != 0 and i%dimension[1] == 0:
            page = np.append(page, row, axis=0)
            row = np.ones((card_dimension[0], 0, 3))*255 

    white_card = np.ones((card_dimension[0], card_dimension[1], 3))*255
    if i%dimension[1] != 0:
        while i != 0 and i%dimension[1] != 0:
            row = np.append(row, white_card, axis=1)
            i+=1
        page = np.append(page, row, axis=0)

        
    return page