┌──(kali㉿kali)-[~/Рабочий стол/CTF/picoCTF]
└─$ exiftool ukn_reality.jpg
ExifTool Version Number         : 13.00
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2024:03:11 20:05:57-04:00
File Access Date/Time           : 2025:02:20 15:24:29-05:00
File Inode Change Date/Time     : 2025:02:20 15:24:29-05:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4

┌──(kali㉿kali)-[~/Рабочий стол/CTF/picoCTF]
└─$ base64 -d <<< "cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg=="
picoCTF{ME74D47A_HIDD3N_d8c381fd}




