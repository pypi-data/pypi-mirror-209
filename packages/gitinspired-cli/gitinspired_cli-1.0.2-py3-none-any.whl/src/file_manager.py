import os
import shutil

marked_files = []

def mark_files(file_paths):
    global marked_files
    marked_files.extend(file_paths)
    print("Files marked for capture.")

def push_files(server_url):
    global marked_files
    if not marked_files:
        print("No files marked for capture.")
        return

    try:
        for file_path in marked_files:
            file_name = os.path.basename(file_path)
            destination = os.path.join(server_url, file_name)
            shutil.copy(file_path, destination)

        print(f"Files pushed to server at: {server_url}")
    except Exception as e:
        print(f"Error pushing files to server: {e}")
    finally:
        marked_files = []  # Clear the marked files list after pushing

def move_to_directory(directory_path):
    os.chdir(directory_path)
    print(f"Moved to directory: {os.getcwd()}")
