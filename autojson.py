# import os
# import json

# # Paths
# script_dir = os.path.dirname(os.path.abspath(__file__))  # C:\Users\cassi\Documents\blog\blog
# images_dir = os.path.join(script_dir, "images")          # C:\Users\cassi\Documents\blog\blog\images
# data_dir = os.path.join(script_dir, "data")              # C:\Users\cassi\Documents\blog\blog\data
# json_path = os.path.join(data_dir, "photo.json")

# # Ensure data folder exists
# os.makedirs(data_dir, exist_ok=True)

# # Allowed image extensions
# image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

# # Get list of images
# images = [
#     {"filename": file}
#     for file in os.listdir(images_dir)
#     if os.path.splitext(file)[1].lower() in image_extensions
# ]

# # Save to JSON
# with open(json_path, "w", encoding="utf-8") as f:
#     json.dump(images, f, indent=4)

# print(f"{json_path} updated with {len(images)} entr{'y' if len(images) == 1 else 'ies'}.")

import os
import json
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

# Paths
images_folder = r"C:\Users\cassi\Documents\blog\blog\images\archive"
json_file = r"C:\Users\cassi\Documents\blog\blog\data\photo.json"

def get_image_date(image_path):
    """Get the date from EXIF metadata if available, else fallback to last modified date."""
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag)
                    if tag_name == "DateTimeOriginal":
                        return datetime.strptime(value, "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d")
    except Exception:
        pass  # If EXIF fails, we'll use last modified date
    
    # Fallback: file's last modified date
    mod_time = os.path.getmtime(image_path)
    return datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")

def generate_json():
    data = []
    for filename in os.listdir(images_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
            file_path = os.path.join(images_folder, filename)
            date_taken = get_image_date(file_path)
            data.append({
                "src": f"images/archive/{filename}",
                "date": date_taken
            })

    # Sort newest first
    data.sort(key=lambda x: x["date"], reverse=True)

    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Updated {json_file} with {len(data)} images.")

if __name__ == "__main__":
    generate_json()
