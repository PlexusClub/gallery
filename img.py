import os
import json

# Path to the folder containing the images
image_folder = "./assets/codemarathon"

# Base URL for accessing the images (change this to your actual server URL)
base_url = "./assets/codemarathon/"

# Initialize the list to store JSON data
events = []

# Iterate through the files in the folder
for file_name in os.listdir(image_folder):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):  # Check for valid image extensions
        event = {
            "url": f"{base_url}{file_name}",
            "eventName": "Code Marathon",
            "description": ""
        }
        events.append(event)

# Save the data to a JSON file
output_file = "codemarathon_events.json"
with open(output_file, "w") as json_file:
    json.dump(events, json_file, indent=2)

print(f"JSON file '{output_file}' created with {len(events)} entries.")
