import os
import shutil

# --- CONFIGURATION ---
# This dictionary maps file extensions to folder names.
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.m3u8'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Programs': ['.exe', '.msi'],
    'Code': ['.ipynb', '.excalidraw', '.vsix']
}
# ---------------------


def organize_folder(folder_path):
    """
    Organizes files in the specified folder into subdirectories by file type.
    """
    print(f"\n📂 Scanning folder: {folder_path}...\n")

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("No files to organize.")
        return

    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        moved = False

        for folder_name, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                dest_folder_path = os.path.join(folder_path, folder_name)
                os.makedirs(dest_folder_path, exist_ok=True)
                shutil.move(os.path.join(folder_path, file), dest_folder_path)
                print(f"✅ Moved '{file}' → '{folder_name}' folder")
                moved = True
                break
        
        if not moved:
            print(f"⚠️ Could not categorize '{file}'. Leaving it in place.")

    print("\n✨ Organization complete!")


if __name__ == "__main__":
    folder_path = input("Enter the path of the folder you want to organize: ").strip()

    if not os.path.isdir(folder_path):
        print("❌ Error: Invalid folder path.")
    else:
        organize_folder(folder_path)
