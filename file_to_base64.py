# importy
import os
import base64
import math

# podaj ścieżkę do konwertowanego pliku, najlepiej żeby plik był w tym samym folderze co skrypt
filename = 'file_to_base64'

# odczytanie rozszerzenia
extension_original = ( filename[ filename.rfind("."): ] )

# kodowanie na b64
with open(filename, 'rb') as f:
    base64_file = base64.urlsafe_b64encode( f.read() ).decode('ascii')

# dzielenie b64 na 200-charowe stringi
content = [ base64_file[ i : i+200 ] for i in range( 0, len(base64_file), 200 ) ]

# n = ilość folderów na danym poziomie
n = math.isqrt( math.isqrt( len( content ) ) ) + 1

# tworzenie katalogu w którym będą foldery
path = os.getcwd()
root = os.path.join( path, f"generated_{filename[:filename.rfind('.')]}" )
os.mkdir( root )
ln = len(str(n))
width = len(str(len(content)))
no = 0

# generowanie folderów właściwych
for b in range( -(-len(content) // n) ):
    i, j, k = b // n**2, (b // n) % n, b % n
    dir3 = os.path.join( root, str(i).zfill(ln), str(j).zfill(ln), str(k).zfill(ln) )
    os.makedirs( dir3 )

    for l in range(n):
        if no < len(content):
            os.mkdir( os.path.join( dir3, f"{[str(no).zfill(width)]}{content[no]}" ) )
            no += 1
        else:
            break

os.mkdir( os.path.join( root, extension_original ) )
