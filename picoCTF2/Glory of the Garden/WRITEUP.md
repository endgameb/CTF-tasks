┌──(kali㉿kali)-[~/Рабочий стол/CTF/picoCTF]
└─$ binwalk garden.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
382           0x17E           Copyright string: "Copyright (c) 1998 Hewlett-Packard Company"

┌──(kali㉿kali)-[~/Рабочий стол/CTF/picoCTF]
└─$ strings garden.jpg
picoCTF{more_than_m33ts_the_3y33dd2eEF5}
