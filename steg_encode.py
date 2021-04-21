#!/usr/bin/env python3

import cv2
import numpy as np
import types

def steg_encode(image_path):
    image = cv2.imread(image_path)

    msg = '' #message string

    #read lines of file into msg variable to pass to steg encoding
    with open('/Users/erik/Documents/Projects/Python/securityResearch/stego_programs/text.txt', 'rt') as f:
        for line in f.readlines():
            msg += line

    #calculate max bytes to be encoded (image width*len*color)//8(for bytes)
    n_bytes = (image.shape[0]*image.shape[1]*3)//8
    if len(msg) > n_bytes:
        raise ValueError('Msg too long for image size')

    bin_msg = ''.join([format(ord(i), '08b') for i in msg])
    index = 0

    for values in image: #iterate over ea line of pic
        for pixel in values: #iterate over ea pixel in line
            r, g, b = [format(i, '08b') for i in pixel]
            #modify LSB only if there is more data to store
            if index < len(bin_msg):
                #hide data in LSB of red pixel
                pixel[0] = int(r[:-1] + bin_msg[index], 2)
                index += 1
            if index < len(bin_msg):
                #hide data in LSB of green pixel
                pixel[1] = int(g[:-1] + bin_msg[index], 2)
                index += 1
            if index < len(bin_msg):
                #hide data in LSB of blue pixel
                pixel[2] = int(b[:-1] + bin_msg[index], 2)
                index += 1
            elif index >= len(bin_msg):
                break

    cv2.imwrite(image_path, image) #writes encoded image back over the original

steg_encode('/Users/erik/Documents/Projects/Python/securityResearch/stego_programs/Ramen.png')
