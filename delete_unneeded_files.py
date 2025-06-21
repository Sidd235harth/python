import os
#delete_unneeded_files.py
#📄 Description:
#Finds and lists files in a directory tree that are larger than 100MB to help you clean up space.
print("name : Siddarth TR \n usn : 1AY24AI106 \n section : O ")
def find_large_files(folder, size_limit=100*1024*1024):
    for foldername, _, filenames in os.walk(folder):
        for filename in filenames:
            path = os.path.join(foldername, filename)
            if os.path.getsize(path) > size_limit:
                print(f"{path} - {os.path.getsize(path)} bytes")

# Example usage:
# find_large_files("folder_path")
