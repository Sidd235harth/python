import os, re
#fill_gaps.py
#📄 Description:
#Detects gaps in numbered file names (like spam001.txt, spam003.txt) and renames them to fill the sequence.
print("name : Siddarth TR \n usn : 1AY24AI106 \n section : O ")
def fill_gaps(folder, prefix):
    files = sorted(f for f in os.listdir(folder) if re.match(rf"{prefix}\d+\.txt", f))
    for index, filename in enumerate(files, start=1):
        expected_name = f"{prefix}{str(index).zfill(3)}.txt"
        if filename != expected_name:
            os.rename(os.path.join(folder, filename), os.path.join(folder, expected_name))
            print(f"Renamed {filename} → {expected_name}")

# Example usage:
# fill_gaps("folder_path", "spam")
