#!/usr/bin/env python3

import cv2
import numpy as np
import types

def steg_decode(image_name):
  image = cv2.imread(image_name) #load encoded image as cv2 object

  bin_data = '' #instantiate empty container to hold binary data
  #values are the rows of pixels in the image
  for values in image: #pixel and value are np.ndarrary data type
    for pixel in values: #ea pixel list of 3 values (RGB) color values
      #list comp to convert ea RGB value in the pixel to bin
      r, g, b = [format(i, '08b') for i in pixel]
      bin_data += r[-1] #get value of LSB of red pixel, add to bin_data
      bin_data += g[-1] #get value of LSB of green pixel, add to bin_data
      bin_data += b[-1] #get value of LSB of blue pixel, add to bin_data

  #split bin_data into groups of 8 (bytes) to decode
  all_bytes = [bin_data[i:i+8] for i in range(0, len(bin_data), 8)]
  #convert from bytes to chars
  decoded_data = ''
  index = 0
  for byte in all_bytes:
    #turn that byte int a char and add it to the decoded_data string
    decoded_data += chr(int(byte, 2))
    index += 1
    if index < 500: continue #limit decoding to first 500 bytes
    else: break #to prevent decoding the whold image

  print('The decoded text is:' + decoded_data)

steg_decode('/Users/erik/Documents/Projects/Python/securityResearch/stego_programs/Ramen.png')
