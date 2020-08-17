#!/usr/bin/env python
# coding: utf-8

# In[8]:


#QR Code Detector 
from pyzbar import pyzbar
import argparse 
import cv2


#parsing the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-i" , "--image" , required =True,
    help ="path to the image file")

args =vars(ap.parse_args())

image = cv2.imread(args["image"])

barcodes =pyzbar.decode(image)


for barcode in barcodes:
    
    (x,y,w,h) =barcode.rect
    cv2.rectangle(image , (x,y), (x+w , y+h),(255,0,0) ,3 )
    
    barcodeData= barcode.data.decode("utf8")
    barcodeType =barcode.type
    
    
    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image , text ,(x,y-10) ,cv2.FONT_HERSHEY_SIMPLEX,0.7, (0,255,0), 2)
    
    print("[INFO] Found {} barcode  {}:".format(barcodeData, barcodeType))
    
cv2.imshow("Image" , image)
cv2.waitKey(0)

    




















     
        







