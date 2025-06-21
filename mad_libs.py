import re
#mad_libs.py
#📄 Description:
#Replaces placeholders like NOUN, VERB, etc., in a text file with user input to create a fun Mad Libs story.

print("name : Siddarth TR \n usn : 1AY24AI106 \n section : O ")
def mad_libs(filename, output_filename):
    with open(filename, 'r') as file:
        content = file.read()

    def prompt_word(match):
        word_type = match.group(0)
        user_input = input(f"Enter a {word_type.lower()}: ")
        return user_input

    result = re.sub(r'ADJECTIVE|NOUN|VERB|ADVERB', prompt_word, content)
    print("\nModified Text:\n", result)

    with open(output_filename, 'w') as file:
        file.write(result)

# Example usage:
mad_libs("Text.txt", "output.txt")
