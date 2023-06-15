import os

os.system("pip install piexif")

import piexif
from tkinter import Tk
from tkinter.filedialog import askdirectory
 
# Function to remove metadata from image
def remove_metadata(image_path):
    try:
        exif_dict = piexif.load(image_path)
        if exif_dict:
            exif_dict.pop('0th')
            exif_dict.pop('Exif')
            exif_dict.pop('GPS')
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, image_path)
            print(f"{os.path.basename(image_path)} cleaned")
        else:
            print(f"{os.path.basename(image_path)} has no metadata")
    except Exception as e:
        print(f"Error cleaning {os.path.basename(image_path)} - {e}")
 
# Function to get path of folder
def get_folder_path():
    root = Tk()
    root.withdraw()
    folder_path = askdirectory(title = "Select folder with images")
    return folder_path
 
# Main function
def main():
    folder_path = get_folder_path()
    print(f"Cleaning metadata from all images in folder {folder_path}")
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.tga', '.heif', '.heic', '.ico', '.tga', '.gif', '.tiff', '.tif', '.svg', '.jfif', '.pct', '.pict', '.jp2', '.bmp')):
                remove_metadata(os.path.join(folder_path, filename))
            else:
                print(f"{filename} is not an image")
    except Exception as e:
        print(f"Error cleaning images - {e}")
    print("Metadata cleaning completed.")
 
if __name__ == "__main__":
    main()

#softy_plug