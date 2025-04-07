
┌──(kali㉿kali)-[~/Рабочий стол/CTF]
└─$ python3 script.py

┌──(kali㉿kali)-[~/Рабочий стол/CTF]
└─$ nc -w 2 mimas.picoctf.net 52834 < original.jpg

┌──(kali㉿kali)-[~/Рабочий стол/CTF]
└─$ nc mimas.picoctf.net 51017
MD5 of your picture:
bffe03f4e28183a440052beb8145110f  test.out

Checking tag 1/7
Looking at IFD0: ModifyDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 2/7
Looking at ExifIFD: DateTimeOriginal
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 3/7
Looking at ExifIFD: CreateDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 4/7
Looking at Composite: SubSecCreateDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 5/7
Looking at Composite: SubSecDateTimeOriginal
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 6/7
Looking at Composite: SubSecModifyDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 7/7
Timezones do not have to match, as long as it's the equivalent time.
Looking at Samsung: TimeStamp
Looking for '1970:01:01 00:00:00.001+00:00'
Found: 2023:11:20 20:46:21.420+00:00
Oops! That tag isn't right. Please try again.

┌──(kali㉿kali)-[~/Рабочий стол/CTF]
└─$ hexedit original.jpg

┌──(kali㉿kali)-[~/Рабочий стол/CTF]
└─$ nc -w 2 mimas.picoctf.net 52834 < original.jpg

┌──(kali㉿kali)-[~/Рабочий стол/CTF]
└─$ nc mimas.picoctf.net 51017
MD5 of your picture:
70593a3784c21dfa6d94cd996c58d361  test.out

Checking tag 1/7
Looking at IFD0: ModifyDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 2/7
Looking at ExifIFD: DateTimeOriginal
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 3/7
Looking at ExifIFD: CreateDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 4/7
Looking at Composite: SubSecCreateDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 5/7
Looking at Composite: SubSecDateTimeOriginal
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 6/7
Looking at Composite: SubSecModifyDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 7/7
Timezones do not have to match, as long as it's the equivalent time.
Looking at Samsung: TimeStamp
Looking for '1970:01:01 00:00:00.001+00:00'
Found: 1970:01:01 00:00:00.001+00:00
Great job, you got that one!

You did it!
picoCTF{71m3_7r4v311ng_p1c7ur3_ed953b57}

┌──(kali㉿kali)-[~/Рабочий стол/CTF]
└─$
В нижней части файла это можно увидеть:

Image_UTC_Data1700513181420

Время эпоха начинается в 1970 году, чтобы добраться до того, что это будет 0, однако, чтобы добавить одну секунду после этого и соответствовать количеству потребностей цифр для эпохи. 0000000000001 Image_UTC_Data0000000000001 и сохранение изображения изменит значение Samsung: TimeStamp.


