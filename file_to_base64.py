# importy
import os
import base64
import numpy as np

# upewnij się, że jesteś w dobrym folderze
os.getcwd()

# podaj ścieżkę do konwertowanego pliku, najlepiej żeby plik był w tym samym folderze co skrypt
filename = 'file_to_base64'

# odczytanie rozszerzenia
extension_original = ( filename[ filename.rfind("."): ] )

# kodowanie na b64
base64_file = repr( base64.urlsafe_b64encode( open(filename, 'rb').read() ) )[2:-1]

# dzielenie b64 na 200-charowe stringi
content = []
i=0
while i <= len(base64_file):
    content.append( base64_file[ i : i+200 ] )
    i += 200
content = [ x for x in content if x ]

# n = ilość folderów na danym poziomie
n = int( np.sqrt( np.sqrt( len( content ) ) ) ) + 1

# tworzenie katalogu w którym będą foldery
path = os.getcwd()
os.mkdir( os.getcwd() + f"\generated_{filename[:filename.rfind('.')]}" )
os.chdir( os.getcwd() + f"\generated_{filename[:filename.rfind('.')]}" )        # zmieniamy cwd
no = 0                                                                          # liczba już wygenerowanych folderów
ln = len(str(n))
is_job_done = False

# generowanie folderów właściwych
path1 = os.getcwd()
for i in range(0, n):
    os.mkdir( os.getcwd() + f"\{str(i).zfill(ln)}" )
    os.chdir( os.getcwd() + f"\{str(i).zfill(ln)}" )
    path2 = os.getcwd()

    for j in range(0, n):
        os.mkdir( os.getcwd() + f"\{str(j).zfill(ln)}" )
        os.chdir( os.getcwd() + f"\{str(j).zfill(ln)}" )
        path3 = os.getcwd()

        for k in range(0, n):       
            os.mkdir( os.getcwd() + f"\{str(k).zfill(ln)}" )
            os.chdir( os.getcwd() + f"\{str(k).zfill(ln)}" ) 

            for l in range(0, n):
                if no < len(content):
                    os.mkdir( f"{[str(no).zfill(len(str(len(content))))]}" + f"{content[no]}" )
                    no += 1
                else: 
                    is_job_done = True
                    os.chdir( path3 )
                    break
                if l == n-1:
                    os.chdir( path3 )

            if is_job_done:
                break
            if k == n-1:
                os.chdir( path2 )

        if is_job_done:
                break
        if j == n-1:
                os.chdir( path1 )
                
    if is_job_done:
                break
    if i == n-1:
        os.chdir( path )

os.chdir( path1 )
os.mkdir(extension_original)
os.chdir( path )
