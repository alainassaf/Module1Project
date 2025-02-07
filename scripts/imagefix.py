#!/usr/bin/env python3

import os
from PIL import Image

image_dir = '/workspaces/Module1Project/images/'
new_dir = '/opt/icons/'

# Iterate through all files in the directory
for image in os.listdir(image_dir):
    
    if '.' not in image[0]:
        # Open the image file
        img = Image.open(image_dir + image)
        
        # Rotate the image 90 degrees, resize to 128x128, convert to RGB
        img = img.rotate(-90).resize((128, 128)).convert("RGB")

        # Construct the new file name
        new_filename = os.path.join(new_dir, os.path.splitext(image)[0])

        # Save the image with the new file name
        img.save(new_filename, 'jpeg')
        
        # Close image
        img.close()