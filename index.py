import os
from shutil import copy2
from PIL import Image
import json

# Ensure the base image is present
base_image_path = '/Users/ordlibrary/ASSETS/image.png'
output_directory = '/Users/ordlibrary/ASSETS/output'

# Create directories
os.makedirs(os.path.join(output_directory, 'Images'), exist_ok=True)
os.makedirs(os.path.join(output_directory, 'Json'), exist_ok=True)

# Check if base image exists
if not os.path.exists(base_image_path):
    print("Base image does not exist. Please check the path.")
    exit()

# Load the base image to confirm it's valid
try:
    with Image.open(base_image_path) as img:
        img.verify()  # Verify that it's a valid image
except (IOError, SyntaxError) as e:
    print("Base image is not valid:", e)
    exit()

# Duplicate the image and create JSON files
for i in range(10001):  # From 0 to 10000
    new_image_path = os.path.join(output_directory, 'Images', f'{i}.png')
    json_path = os.path.join(output_directory, 'Json', f'{i}.json')

    # Copy image
    copy2(base_image_path, new_image_path)

    # Create JSON data
    json_data = {
        "name": f"Stone #{i}",
        "description": "The Solana Stone Powered by the $RUNES token. Derived from its forefather the Bitcoin Runestone, etching its place in blockchain history as the first ever multi chain vessel, that is building the foundation to the bridge that shall bridge the future from Solana To Bitcoin and beyond. Will you join us on this journey anon, and etch your place in history? The Ticker Is $RUNES",
        "image": f"{i}.png",
        "external_url": "thetickerisrunes.com",
        "attributes": [
            {"trait_type": "Blockchain", "value": "Bitcoin"},
            {"trait_type": "Blockchain", "value": "Solana"}
        ],
        "properties": {
            "files": [{"uri": f"{i}.png", "type": "image/png"}],
            "category": "image"
        }
    }

    # Write JSON file
    with open(json_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

print("Images and JSON files have been successfully created.")
