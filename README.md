# Google Course: Automating Real-World Tasks with Python
## Module 1 Project
### by Alain Assaf

## Project Purpose:
Your company was in the process of updating its website, and they hired a design contractor to create some new icon graphics for the site. But the contractor delivered the final designs in the wrong format, rotated 90°, and too large.

Use the Python Imaging Library to do the following to a batch of images:
* Open an image
* Rotate an image
* Resize an image
* Save an image in a specific format in a separate directory 

## Original Data
Images were provided by Google for the exercise. After creating the container, I connected to it and downloaded the images.zip file from Google.  
```bash
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie
```
I unziped the resulting images.zip file into the images folder.

### Image problems
The images received are in the wrong format:
* .tiff format
* Image resolution 192x192 pixel (too large)
* Rotated 90° anti-clockwise

The images required for the launch should be in this format:
* .jpeg format
* Image resolution 128x128 pixels
* Should be straight

## Manipulated Data
Updated images were saved to \opt\icons.

# Code details

## Dockerfile
I wrote a simple Dockerfile to create a container using the latest Python version and load the PIL image library.
```Dockerfile
# Use the latest Python image from the Docker Hub
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the Pillow library
RUN pip install --no-cache-dir pillow

# Command to run when the container starts
CMD ["python"]
```

## Container Development
I used VS Code and Docker Desktop for Windows to open the container and connect VS Code to it.  Read my [Docker and Python](https://alainassaf.com/2023-12-19-Cloud-Journey-1-Docker-and-Python/) blog post for more details.

## Python
```python
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
```