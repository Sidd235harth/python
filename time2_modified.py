#project10_time2_modified.py
#📄 Description:
#Modifies a Time class so that time is stored as total seconds since midnight and formats it for display.
print("name : Siddarth TR \n usn : 1AY24AI106 \n section : O ")
class Time:
    def __init__(self, seconds=0):
        self.seconds = seconds

    def __str__(self):
        h = self.seconds // 3600
        m = (self.seconds % 3600) // 60
        s = self.seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

def int_to_time(seconds):
    return Time(seconds)

# Example usage
t = Time(3661)
print(t)
