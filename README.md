# Folderify your files and use 0B of cloud storage
## Why?
The idea behind this project is that many cloud storage providers consider directories to be 0B objects, regardless of their name. We can exploit it by creating a structure of directories with a file encoded in only the names of the directories.


## How?
We can encode any file into [base64](https://pl.wikipedia.org/wiki/Base64) format, thus making it a sequence of characters. Some of them are not allowed in directory names, so we can substitute them for other ones that are not used in the base64 format and are name-safe. 

Then we create a bunch of folders with a format like this: [number] [content].
Number helps in putting the file back together in the right order. Content, however, stores a piece of file in b64 format. There is also a folder that stores the original extension of the encoded file.


## Coming back from directories.
The process of coming back is analogous to the one of encoding a file. The program reads all names of directories, sorts them by the number tag, and appends the content to a string. This string then gets modified and the original b64 characters that we substituted are brought back. The content of file gets decoded back into its original form and the extension is added.


## Efficiency
It is not really efficient way of storing/moving files, since creation of directories is *really* slow. Uploading those is also a pain. Another issue is that the entire file must be loaded into memory and then processed. This will be a problem on a bigger scale. Nonetheless, I was able to store several movies on a cloud-storage service without using up any space :wink: