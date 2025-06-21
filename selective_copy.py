import os, shutil
#selective_copy.py
#📄 Description:
#Copies all files with specified extensions (like .pdf, .jpg) from a folder tree into a new folder.
print("name : Siddarth TR \n usn : 1AY24AI106 \n section : O ")
def selective_copy(source_folder, destination_folder, extensions):
    os.makedirs(destination_folder, exist_ok=True)
    for foldername, _, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.lower().endswith(extensions):
                shutil.copy(os.path.join(foldername, filename), destination_folder)

# Example usage:
selective_copy(r"G:\My Drive\ExpPYproj", "destination", (".pdf", ".jpg"))
