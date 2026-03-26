import os
from sorter import sort_files

def scan_files(folder_path):
    files = []
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            files.append(file)
    return files

if __name__ == "__main__":
    folder = "./test_folder"
    sort_files(folder)