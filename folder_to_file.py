# importy
import os
import base64

# załaduj katalog z folderami
files = 'generated_file_to_base64'
p = os.path.join( os.getcwd(), files )
extraction = []
extension = ''
first = True

for dirpath, dirnames, filenames in os.walk(p):     # wczytywanie całej struktury folderów
    if first:
        for name in dirnames:
            if '.' in name:
                extension = name
        first = False
    else:
        found_leaf = False
        for j in dirnames:
            if j.startswith("['"):
                extraction.append(j)
                found_leaf = True
        if found_leaf:
            dirnames.clear()

extraction.sort()
index_of_content = extraction[0].rfind("]")+1

# zmiana z url-safe b64 na zwykły b64 (tłumaczenie znaków) i odkodowanie bezpośrednio do pliku
urlsafe_to_b64 = str.maketrans('-_', '+/')

# zapis do pliku oryginalnego
with open(f"{files[10:]}{extension}", "wb") as f:
    for name in extraction:
        f.write( base64.b64decode( name[index_of_content:].translate(urlsafe_to_b64) ) )
