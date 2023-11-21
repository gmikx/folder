# importy
import os
import base64
import numpy as np

# upewnij się, że jesteś w dobrym folderze
os.getcwd()

# załaduj katalog z folderami
files = 'generated_file_to_base64'
p = os.getcwd() + f"\{files}"
extraction = []
extension = ''
i = 0

for dirpath, dirnames, filenames in os.walk(p):     # wczytywanie całej struktury folderów
    directory_level = dirpath.replace(p, "")
    if i==0:
        extension = dirnames[0]
    else:
        if (len(dirnames) != 0):
            for j in dirnames:
                if j[0:2]=="['":
                    extraction.append(j)
    i = 1

extraction.sort()
index_of_content = extraction[0].rfind("]")+1

b64 = ''
for i in extraction:
    b64 += (i[index_of_content:])

# zmiana z url-safe b64 na zwykły b64
import re
b64 = re.sub('-', '+', b64)
b64 = re.sub('_', '/', b64)

# zapis do pliku oryginalnego
bytes = base64.b64decode(b64)
f = open(f"{files[10:]}{extension}", "wb")
f.write(bytes)
f.close()
os.chdir(p)
os.chdir("..")
