from src.reduce_image import reduce_image
import numpy as np
import cv2

def fusion_images(im1,im2):    
    im1 = reduce_image(im1,True)
    im2 = reduce_image(im2,False)

    title1 = im1[0:90,:]
    body1 = im1[-410:-37,:]
    title2 = im2[28:102,:]
    body2 = im2[-400:-1,:]
    half_card1= np.append(title1,body1,axis=0)
    half_card2= np.append(title2,body2,axis=0)
    final_card= np.append(half_card1,half_card2,axis=0)
    return final_card


    # title1 = im1[0:ceil((im1.shape[0])*(0.096)),:]
    # body1 = im1[ceil((im1.shape[0])*(-0.438)):ceil((im1.shape[0])*(-0.039)),:]
    # title2 = im2[ceil((im2.shape[0])*(0.029)):ceil((im2.shape[0])*(0.108)),:]
    # body2 = im2[ceil((im2.shape[0])*(-0.427)):ceil((im2.shape[0])*(-0.001)),:]
    # half_card1= np.append(title1,body1,axis=0)
    # half_card2= np.append(title2,body2,axis=0)
    # final_card= np.append(half_card1,half_card2,axis=0)
    # print(final_card.shape)
    # return final_card