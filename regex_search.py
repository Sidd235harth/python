import os, re
#regex_search.py
#📄 Description:
#Searches all .txt files in a folder for lines that match a user-supplied regex pattern and prints them.
print("name : Siddarth TR \n usn : 1AY24AI106 \n section : O ")
def regex_search(folder, pattern):
    regex = re.compile(pattern)
    for filename in os.listdir(folder):
        if filename.endswith('.txt'):
            with open(os.path.join(folder, filename), 'r') as f:
                for line in f:
                    if regex.search(line):
                        print(f"{filename}: {line.strip()}")

# Example usage:
regex_search(r"G:\My Drive\ExpPYproj", r"\d{3}-\d{3}-\d{4}")
