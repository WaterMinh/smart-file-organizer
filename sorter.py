import os
import shutil

def sort_files(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            ext = file.split(".")[-1]

            target_folder = os.path.join(folder_path, ext)

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            shutil.move(full_path, os.path.join(target_folder, file))