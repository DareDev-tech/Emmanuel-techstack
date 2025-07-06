#!/usr/bin/env python3

import os
from PIL import Image

old_path = os.path.join(os.path.expanduser('~'), 'Emmanuel-techstack', 'image-processing-automation', 'images')
new_path = os.path.join(os.path.expanduser('~'), 'processed_images')

os.makedirs(new_path, exist_ok=True)

for image in os.listdir(old_path):
    if not image.startswith('.') and os.path.isfile(os.path.join(old_path, image)):
        with Image.open(os.path.join(old_path, image)) as img:
            processed = img.rotate(-90).resize((128, 128)).convert("RGB")
            output_filename = os.path.splitext(image)[0] + '.jpeg'
            processed.save(os.path.join(new_path, output_filename), 'JPEG')

