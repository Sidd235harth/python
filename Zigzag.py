print(" Siddarth TR \n USN:1AY24AI106 \n sec:o")
lines = 9
max_spaces = lines 
for i in range(lines):
    if i <= max_spaces:
        spaces = i
    else:
        spaces = lines - i - 1
    print(" " * spaces + "*" * 8)
