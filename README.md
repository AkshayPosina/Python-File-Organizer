# Automated File Organizer 📂

A simple but powerful Python script to automatically organize files in a directory by moving them into categorized subfolders based on their file extension.

## Features
-   Scans a specified source folder for files.
-   Sorts files into categories like 'Images', 'Documents', 'Videos', and more.
-   Automatically creates category folders if they don't exist.
-   Easily customizable to add new file types and categories.
-   Ignores files that don't match any category.

## How to Use
1.  **Clone the repository** or download the `organizer.py` script.
2.  **Configure the script:** Open `organizer.py` and change the `SOURCE_FOLDER` variable to the absolute path of the folder you want to organize.
    ```python
    SOURCE_FOLDER = 'C:/Users/YourUser/Downloads'
    ```
3.  **Run the script:** Open your terminal, navigate to the script's directory, and run the following command:
    ```bash
    python organizer.py
    ```
The script will then scan the folder and organize your files.

## Technologies Used
-   Python
-   `os` module (for interacting with the file system)
-   `shutil` module (for moving files)
