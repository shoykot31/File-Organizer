import os
import shutil

def organize_my_files(folder_path):
    # Dictionary mapping file extensions to their designated target folders
    extension_map = {
        # Executables & Installers
        "exe": "Installers",
        "msi": "Installers",
        "apk": "Installers",
        
        # Documents
        "pdf": "Documents",
        "pptx": "Documents",
        "epub": "Documents",        
	"doctx": "Documents",

        # Media (Images & Videos)
        "jpg": "Media/Images",
        "jpeg": "Media/Images",
        "png": "Media/Images",
        "avif": "Media/Images",
        "mp4": "Media/Videos",
        "mkv": "Media/Videos",
	"mp3": "Media/Audio",
	"webp": "Media/Audio",
	"opus": "Media/Audio",        
	"mov": "Media/Videos",

        # Torrents
        "torrent": "Torrents",
        
        # Archives/Compressed
        "zip": "Archives",
	"rar": "Archives",        

        # Code & Web
        "html": "Code",
        "py": "Code",
	"c": "Code",
	"cpp": "Code",
	"js": "Code",
	"css": "Code",
        "sublime-build": "Code",
        
        # System & Miscellaneous
        "lnk": "System_Shortcuts",
        "ini": "System_Shortcuts",
        "log": "System_Shortcuts",
        "winmd": "System_Shortcuts"
    }

    # Loop through everything inside the target folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip if it's already a folder (avoids moving existing directories)
        if os.path.isdir(file_path):
            continue
            
        # Isolate the file extension
        parts = filename.split('.')
        if len(parts) > 1:
            extension = parts[-1].lower()
            
            # Check if the extension has an assigned group folder
            if extension in extension_map:
                target_subfolder = extension_map[extension]
                target_dir = os.path.join(folder_path, target_subfolder)
                
                # Dynamically create the category folder if missing
                os.makedirs(target_dir, exist_ok=True)
                
                # Move the file inside
                shutil.move(file_path, os.path.join(target_dir, filename))
                print(f"Moved: {filename} -> {target_subfolder}/")
            else:
                # Catch-all directory for unmapped extensions (like .x64)
                other_dir = os.path.join(folder_path, "Others")
                os.makedirs(other_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(other_dir, filename))
                print(f"Moved Unmapped: {filename} -> Others/")
        else:
            print(f"Skipped (No extension found): {filename}")

# Paste your messy folder directory below to run it:
organize_my_files("/path/to/your/messy_folder")