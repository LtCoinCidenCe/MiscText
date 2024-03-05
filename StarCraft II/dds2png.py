from pathlib import Path
from PIL import Image

it = [x for x in Path('.').iterdir() if x.is_file()
      and x.name.endswith('.dds')]


commands = 0
for entry in it:
    originalName = entry.name
    newName = originalName[0:-4]+'.png'
    ddsImage = Image.open(originalName)
    ddsImage.save(newName, 'png')
    print("From:", originalName, "to:", newName)
    commands += 1

print("Total files:", commands)

oo = 0
