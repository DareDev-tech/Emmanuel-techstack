#!/usr/bin/env python3

import os
from PIL import Image

# Set the correct input and output paths based on your local setup
old_path = '/home/linux/Emmanuel-techstack/image-processing-automation/images'
new_path = '/home/linux/Emmanuel-techstack/image-processing-automation/processed_images'

# Create output directory if it doesn't exist
os.makedirs(new_path, exist_ok=True)

# Process each image in the input directory
for image in os.listdir(old_path):
    # Skip hidden files and make sure it's a file, not a folder
    if not image.startswith('.') and os.path.isfile(os.path.join(old_path, image)):
        # Open the image
        with Image.open(os.path.join(old_path, image)) as img:
            # Process and save as .jpeg
            processed = img.rotate(-90).resize((128, 128)).convert("RGB")
            output_filename = os.path.splitext(image)[0] + '.jpeg'
            processed.save(os.path.join(new_path, output_filename), 'JPEG')
