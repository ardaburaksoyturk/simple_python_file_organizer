import os
import shutil
from datetime import datetime

def organize_downloads():
    """Organize files in the downloads folder by moving them into subfolders named after the file extension"""

    downloads_path = os.path.expanduser("~/Downloads")

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".ico"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".m4a", ".wma"],
        "Video": [".mp4", ".mov", ".wmv", ".avi", ".mkv", ".flv", ".mpeg"],
        "Compressed": [".zip", ".rar", ".tar", ".gz", ".bz2", ".7z"],
    }

    try:
        
        for folder in file_types:
            folder_path = os.path.join(downloads_path, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
    
        files_moved = 0
        for filename in os.listdir(downloads_path):
            file_path = os.path.join(downloads_path, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1].lower()
                for folder, extensions in file_types.items():
                    if file_extension in extensions:
                        new_path = os.path.join(downloads_path, folder, filename)
                        shutil.move(file_path, new_path)
                        files_moved += 1
                        break
        print(f"Organized {files_moved} files")
    except Exception as e:
        print(f"An error occurred: {e}")

organize_downloads()
