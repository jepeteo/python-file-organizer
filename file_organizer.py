import os
import shutil
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def organize_files():
    # Get the target directory from .env file
    directory = os.getenv('TARGET_DIRECTORY')

    # Category mappings
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf'],
        'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
        'Video': ['.mp4', '.avi', '.mkv', '.mov'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Others': []
    }

    # Create category folders
    for category in categories:
        os.makedirs(os.path.join(directory, category), exist_ok=True)

    # Iterate through files in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Skip if it's a directory
        if os.path.isdir(item_path):
            continue

        # Get file extension
        file_ext = Path(item).suffix.lower()

        # Find the category for the file
        target_category = 'Others'
        for category, extensions in categories.items():
            if file_ext in extensions:
                target_category = category
                break

        # Move the file to the appropriate category folder
        target_path = os.path.join(directory, target_category, item)
        shutil.move(item_path, target_path)
        print(f"Moved {item} to {target_category}")

if __name__ == "__main__":
    organize_files()