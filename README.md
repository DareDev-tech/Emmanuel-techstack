# Emmanuel-techstack
A curated collection of my IT Automation works.

# Python project 1: Image Processing Automation

## 📌 Overview
This project solves a real-world image processing challenge using **Python** and the **Pillow** library.

The scenario:  
A company preparing for a website relaunch received a batch of icon graphics from a design contractor. Unfortunately:  
- The images were in the wrong format  
- They were rotated 90°  
- They were too large for web use  

With the contractor unavailable and a tight deadline looming, a quick automated solution was needed.

This script automates the entire process—turning hours of manual work into a matter of seconds.

---

## Features
- **Batch Processing:** Iterates through all images in the input folder
- **Rotation Fix:** Rotates each image to the correct orientation
- **Resizing:** Scales images to the required web dimensions
- **Format Conversion:** Converts files (e.g., `.tiff` → `.jpeg`)
- **Organized Output:** Saves processed images in a separate directory

---

## 🛠 Tech Stack
- **Language:** Python 3.x  
- **Library:** [Pillow (PIL Fork)](https://pillow.readthedocs.io/)  

---

## 📂 Project Structure
    Emmanuel-techstack/
    ├── image-processing-automation/
    │   ├── image_process_script.py
    │   ├── image_process.py
    │   ├── images/
    │   │   ├── .DS_Store
    │   │   ├── ic_add_location_black_48dp
    │   │   ├── ic_add_location_white_48dp
    │   │   ├── ic_beenhere_black_48dp
    │   │   ├── ic_beenhere_white_48dp
    │   │   ├── ic_directions_bike_black_48dp
    │   │   ├── ic_directions_bike_white_48dp
    │   │   ├── ic_directions_black_48dp
    │   │   ├── ic_directions_boat_black_48dp
    │   │   ├── ic_directions_boat_white_48dp
    │   │   ├── ic_directions_bus_black_48dp
    │   │   ├── ic_directions_bus_white_48dp
    │   │   ├── ... (all other original images)
    │   │   └── ic_near_me_black_48dp
    │   ├── images.zip
    │   ├── problem_statement.md
    │   └── processed_images/
    │       ├── ic_add_location_black_48dp.jpeg
    │       ├── ic_add_location_white_48dp.jpeg
    │       ├── ic_beenhere_black_48dp.jpeg
    │       ├── ic_beenhere_white_48dp.jpeg
    │       ├── ic_directions_bike_black_48dp.jpeg
    │       ├── ic_directions_bike_white_48dp.jpeg
    │       ├── ... (all other processed images)
    │       └── ic_near_me_black_48dp.jpeg
    ├── README.md
    └── sales_summary_automation/
        ├── car_data.py
        ├── combine_email_report.py
        ├── email.py
        ├── Problem_statement.md
        └── report.py


## 🔄 How It Works
1. **Scan Input Folder** – The script reads all image files inside `images/`.  
2. **Rotate** – Corrects orientation by rotating each image to its proper position.  
3. **Resize** – Adjusts images to the required dimensions for web optimization.  
4. **Convert Format** – Changes image format (e.g., `.tiff` → `.jpeg`) for compatibility.  
5. **Save Output** – Stores processed images into `processed_images/` with the correct naming and format.  


## 💡 Use Cases
- Preparing images for websites or mobile apps  
- Automating repetitive image formatting tasks in forensics, image editing devopsamong others.  
- Bulk image correction for digital marketing or CMS uploads. 


