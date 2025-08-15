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
image-processing-automation/
    ├── images/
        ├── .DS_Store
        ├── ic_add_location_black_48dp
        ├── ic_add_location_white_48dp
        ├── ic_beenhere_black_48dp
        ├── ic_beenhere_white_48dp
        ├── ic_directions_bike_black_48dp
        ├── ic_directions_bike_white_48dp
        ├── ic_directions_black_48dp
        ├── ic_directions_boat_black_48dp
        ├── ic_directions_boat_white_48dp
        ├── ic_directions_bus_black_48dp
        ├── ic_directions_bus_white_48dp
        ├── ic_directions_car_black_48dp
        ├── ic_directions_car_white_48dp
        ├── ic_directions_railway_black_48dp
        ├── ic_directions_railway_white_48dp
        ├── ic_directions_run_black_48dp
        ├── ic_directions_run_white_48dp
        ├── ic_directions_subway_black_48dp
        ├── ic_directions_subway_white_48dp
        ├── ic_directions_transit_black_48dp
        ├── ic_directions_transit_white_48dp
        ├── ic_directions_walk_black_48dp
        ├── ic_directions_walk_white_48dp
        ├── ic_directions_white_48dp
        ├── ic_edit_location_black_48dp
        ├── ic_edit_location_white_48dp
        ├── ic_ev_station_black_48dp
        ├── ic_ev_station_white_48dp
        ├── ic_flight_black_48dp
        ├── ic_flight_white_48dp
        ├── ic_hotel_black_48dp
        ├── ic_hotel_white_48dp
        ├── ic_layers_black_48dp
        ├── ic_layers_clear_black_48dp
        ├── ic_layers_clear_white_48dp
        ├── ic_layers_white_48dp
        ├── ic_local_activity_black_48dp
        ├── ic_local_activity_white_48dp
        ├── ic_local_airport_black_48dp
        ├── ic_local_airport_white_48dp
        ├── ic_local_atm_black_48dp
        ├── ic_local_atm_white_48dp
        ├── ic_local_bar_black_48dp
        ├── ic_local_bar_white_48dp
        ├── ic_local_cafe_black_48dp
        ├── ic_local_cafe_white_48dp
        ├── ic_local_car_wash_black_48dp
        ├── ic_local_car_wash_white_48dp
        ├── ic_local_convenience_store_black_48dp
        ├── ic_local_convenience_store_white_48dp
        ├── ic_local_dining_black_48dp
        ├── ic_local_dining_white_48dp
        ├── ic_local_drink_black_48dp
        ├── ic_local_drink_white_48dp
        ├── ic_local_florist_black_48dp
        ├── ic_local_florist_white_48dp
        ├── ic_local_gas_station_black_48dp
        ├── ic_local_gas_station_white_48dp
        ├── ic_local_grocery_store_black_48dp
        ├── ic_local_grocery_store_white_48dp
        ├── ic_local_hospital_black_48dp
        ├── ic_local_hospital_white_48dp
        ├── ic_local_hotel_black_48dp
        ├── ic_local_hotel_white_48dp
        ├── ic_local_laundry_service_black_48dp
        ├── ic_local_laundry_service_white_48dp
        ├── ic_local_library_black_48dp
        ├── ic_local_library_white_48dp
        ├── ic_local_mall_black_48dp
        ├── ic_local_mall_white_48dp
        ├── ic_local_movies_black_48dp
        ├── ic_local_movies_white_48dp
        ├── ic_local_offer_black_48dp
        ├── ic_local_offer_white_48dp
        ├── ic_local_parking_white_48dp
        ├── ic_local_pharmacy_black_48dp
        ├── ic_local_pharmacy_white_48dp
        ├── ic_local_phone_black_48dp
        ├── ic_local_phone_white_48dp
        ├── ic_local_pizza_black_48dp
        ├── ic_local_pizza_white_48dp
        ├── ic_local_play_black_48dp
        ├── ic_local_play_white_48dp
        ├── ic_local_post_office_black_48dp
        ├── ic_local_post_office_white_48dp
        ├── ic_local_printshop_black_48dp
        ├── ic_local_printshop_white_48dp
        ├── ic_local_see_black_48dp
        ├── ic_local_see_white_48dp
        ├── ic_local_shipping_black_48dp
        ├── ic_local_shipping_white_48dp
        ├── ic_local_taxi_black_48dp
        ├── ic_local_taxi_white_48dp
        ├── ic_map_black_48dp
        ├── ic_map_white_48dp
        ├── ic_my_location_black_48dp
        ├── ic_my_location_white_48dp
        ├── ic_navigation_black_48dp
        ├── ic_navigation_white_48dp
        └── ic_near_me_black_48dp
    ├── processed_images/
        ├── ic_add_location_black_48dp.jpeg
        ├── ic_add_location_white_48dp.jpeg
        ├── ic_beenhere_black_48dp.jpeg
        ├── ic_beenhere_white_48dp.jpeg
        ├── ic_directions_bike_black_48dp.jpeg
        ├── ic_directions_bike_white_48dp.jpeg
        ├── ic_directions_black_48dp.jpeg
        ├── ic_directions_boat_black_48dp.jpeg
        ├── ic_directions_boat_white_48dp.jpeg
        ├── ic_directions_bus_black_48dp.jpeg
        ├── ic_directions_bus_white_48dp.jpeg
        ├── ic_directions_car_black_48dp.jpeg
        ├── ic_directions_car_white_48dp.jpeg
        ├── ic_directions_railway_black_48dp.jpeg
        ├── ic_directions_railway_white_48dp.jpeg
        ├── ic_directions_run_black_48dp.jpeg
        ├── ic_directions_run_white_48dp.jpeg
        ├── ic_directions_subway_black_48dp.jpeg
        ├── ic_directions_subway_white_48dp.jpeg
        ├── ic_directions_transit_black_48dp.jpeg
        ├── ic_directions_transit_white_48dp.jpeg
        ├── ic_directions_walk_black_48dp.jpeg
        ├── ic_directions_walk_white_48dp.jpeg
        ├── ic_directions_white_48dp.jpeg
        ├── ic_edit_location_black_48dp.jpeg
        ├── ic_edit_location_white_48dp.jpeg
        ├── ic_ev_station_black_48dp.jpeg
        ├── ic_ev_station_white_48dp.jpeg
        ├── ic_flight_black_48dp.jpeg
        ├── ic_flight_white_48dp.jpeg
        ├── ic_hotel_black_48dp.jpeg
        ├── ic_hotel_white_48dp.jpeg
        ├── ic_layers_black_48dp.jpeg
        ├── ic_layers_clear_black_48dp.jpeg
        ├── ic_layers_clear_white_48dp.jpeg
        ├── ic_layers_white_48dp.jpeg
        ├── ic_local_activity_black_48dp.jpeg
        ├── ic_local_activity_white_48dp.jpeg
        ├── ic_local_airport_black_48dp.jpeg
        ├── ic_local_airport_white_48dp.jpeg
        ├── ic_local_atm_black_48dp.jpeg
        ├── ic_local_atm_white_48dp.jpeg
        ├── ic_local_bar_black_48dp.jpeg
        ├── ic_local_bar_white_48dp.jpeg
        ├── ic_local_cafe_black_48dp.jpeg
        ├── ic_local_cafe_white_48dp.jpeg
        ├── ic_local_car_wash_black_48dp.jpeg
        ├── ic_local_car_wash_white_48dp.jpeg
        ├── ic_local_convenience_store_black_48dp.jpeg
        ├── ic_local_convenience_store_white_48dp.jpeg
        ├── ic_local_dining_black_48dp.jpeg
        ├── ic_local_dining_white_48dp.jpeg
        ├── ic_local_drink_black_48dp.jpeg
        ├── ic_local_drink_white_48dp.jpeg
        ├── ic_local_florist_black_48dp.jpeg
        ├── ic_local_florist_white_48dp.jpeg
        ├── ic_local_gas_station_black_48dp.jpeg
        ├── ic_local_gas_station_white_48dp.jpeg
        ├── ic_local_grocery_store_black_48dp.jpeg
        ├── ic_local_grocery_store_white_48dp.jpeg
        ├── ic_local_hospital_black_48dp.jpeg
        ├── ic_local_hospital_white_48dp.jpeg
        ├── ic_local_hotel_black_48dp.jpeg
        ├── ic_local_hotel_white_48dp.jpeg
        ├── ic_local_laundry_service_black_48dp.jpeg
        ├── ic_local_laundry_service_white_48dp.jpeg
        ├── ic_local_library_black_48dp.jpeg
        ├── ic_local_library_white_48dp.jpeg
        ├── ic_local_mall_black_48dp.jpeg
        ├── ic_local_mall_white_48dp.jpeg
        ├── ic_local_movies_black_48dp.jpeg
        ├── ic_local_movies_white_48dp.jpeg
        ├── ic_local_offer_black_48dp.jpeg
        ├── ic_local_offer_white_48dp.jpeg
        ├── ic_local_parking_white_48dp.jpeg
        ├── ic_local_pharmacy_black_48dp.jpeg
        ├── ic_local_pharmacy_white_48dp.jpeg
        ├── ic_local_phone_black_48dp.jpeg
        ├── ic_local_phone_white_48dp.jpeg
        ├── ic_local_pizza_black_48dp.jpeg
        ├── ic_local_pizza_white_48dp.jpeg
        ├── ic_local_play_black_48dp.jpeg
        ├── ic_local_play_white_48dp.jpeg
        ├── ic_local_post_office_black_48dp.jpeg
        ├── ic_local_post_office_white_48dp.jpeg
        ├── ic_local_printshop_black_48dp.jpeg
        ├── ic_local_printshop_white_48dp.jpeg
        ├── ic_local_see_black_48dp.jpeg
        ├── ic_local_see_white_48dp.jpeg
        ├── ic_local_shipping_black_48dp.jpeg
        ├── ic_local_shipping_white_48dp.jpeg
        ├── ic_local_taxi_black_48dp.jpeg
        ├── ic_local_taxi_white_48dp.jpeg
        ├── ic_map_black_48dp.jpeg
        ├── ic_map_white_48dp.jpeg
        ├── ic_my_location_black_48dp.jpeg
        ├── ic_my_location_white_48dp.jpeg
        ├── ic_navigation_black_48dp.jpeg
        ├── ic_navigation_white_48dp.jpeg
        └── ic_near_me_black_48dp.jpeg
    ├── image_process_script.py
    ├── image_process.py
    ├── images.zip
    └── problem_statement.md
sales_summary_automation/
    ├── car_data.py
    ├── combine_email_report.py
    ├── email.py
    ├── Problem_statement.md
    └── report.py
README.md


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


