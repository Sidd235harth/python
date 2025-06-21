#project11_kangaroo_class.py
#📄 Description:
#Implements a class representing a Kangaroo with a pouch that can hold any object, including another Kangaroo.
print("name : Siddarth TR \n usn : 1AY24AI106 \n section : O ")
class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def __str__(self):
        return f"Kangaroo pouch contains: {[str(item) for item in self.pouch_contents]}"

# Testing
kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(roo)

print(kanga)
print(roo)
