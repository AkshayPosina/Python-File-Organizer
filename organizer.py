import os
import shutil

# --- CONFIGURATION ---
# Set the path to the folder you want to organize.
SOURCE_FOLDER = 'C:/Users/Harsh/Downloads' 

# This dictionary maps file extensions to folder names.
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    # Added .pptx to the Documents list
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.ppt', '.pptx'], 
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.m3u8'], # Added .m3u8
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    # Created a new category for programs
    'Programs': ['.exe', '.msi'],
    # Created a new category for developer files
    'Code': ['.ipynb', '.excalidraw', '.vsix']
}
# ---------------------


def organize_folder(folder_path):
    """
    Organizes files in the specified folder into subdirectories by file type.
    """
    print(f"Scanning folder: {folder_path}...")

    # Get a list of all files in the source folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("No files to organize.")
        return

    for file in files:
        file_extension = os.path.splitext(file)[1].lower() # Get the file extension (e.g., '.jpg')
        moved = False

        for folder_name, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                # Create the destination folder if it doesn't exist
                dest_folder_path = os.path.join(folder_path, folder_name)
                if not os.path.exists(dest_folder_path):
                    os.makedirs(dest_folder_path)
                    print(f"Created folder: {dest_folder_path}")

                # Move the file
                shutil.move(os.path.join(folder_path, file), dest_folder_path)
                print(f"Moved '{file}' to '{folder_name}' folder.")
                moved = True
                break
        
        if not moved:
            print(f"Could not categorize '{file}'. Leaving it in place.")

    print("\nOrganization complete! ✨")


if __name__ == "__main__":
    # Make sure to change SOURCE_FOLDER at the top of the script!
    if not os.path.isdir(SOURCE_FOLDER) or SOURCE_FOLDER == '/path/to/your/messy/folder':
        print("Error: Please set the 'SOURCE_FOLDER' variable to a valid directory.")
    else:
        organize_folder(SOURCE_FOLDER)