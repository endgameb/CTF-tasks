открываем файл
заходим в статистика > иерахия протоколов 
смотрим и видим что udp трафика больше всего
сохраняем весь поток udp в файл 
правой кнопкой мыши > отслеживать >  udp поток
показать как: необработанный 
сохраняем в файл udp
┌──(kali㉿kali)-[/media/sf_k/ugra ctf 2025-quals/forensic/Вещает, видимо ]
└─$ binwalk udp    

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
500           0x1F4           MPEG transport stream data
1816          0x718           MPEG transport stream data
3508          0xDB4           MPEG transport stream data
5200          0x1450          MPEG transport stream data
6892          0x1AEC          MPEG transport stream data
8208          0x2010          MPEG transport stream data
9148          0x23BC          MPEG transport stream data
10464         0x28E0          MPEG transport stream data
12156         0x2F7C          MPEG transport stream data
13472         0x34A0          MPEG transport stream data
14412         0x384C          MPEG transport stream data
16292         0x3FA4          MPEG transport stream data
17796         0x4584          MPEG transport stream data
18924         0x49EC          MPEG transport stream data
20052         0x4E54          MPEG transport stream data
20992         0x5200          MPEG transport stream data
21932         0x55AC          MPEG transport stream data
23060         0x5A14          MPEG transport stream data
24000         0x5DC0          MPEG transport stream data
25128         0x6228          MPEG transport stream data
27008         0x6980          MPEG transport stream data
28136         0x6DE8          MPEG transport stream data
29640         0x73C8          MPEG transport stream data
31708         0x7BDC          MPEG transport stream data
33024         0x8100          MPEG transport stream data
34716         0x879C          MPEG transport stream data
36032         0x8CC0          MPEG transport stream data
37160         0x9128          MPEG transport stream data
38288         0x9590          MPEG transport stream data
39792         0x9B70          MPEG transport stream data
40732         0x9F1C          MPEG transport stream data
42048         0xA440          MPEG transport stream data
43364         0xA964          MPEG transport stream data
44492         0xADCC          MPEG transport stream data
45432         0xB178          MPEG transport stream data
46372         0xB524          MPEG transport stream data
47312         0xB8D0          MPEG transport stream data
48440         0xBD38          MPEG transport stream data
49380         0xC0E4          MPEG transport stream data
50508         0xC54C          MPEG transport stream data
52388         0xCCA4          MPEG transport stream data
53516         0xD10C          MPEG transport stream data
55396         0xD864          MPEG transport stream data
57464         0xE078          MPEG transport stream data
59532         0xE88C          MPEG transport stream data
61224         0xEF28          MPEG transport stream data
62164         0xF2D4          MPEG transport stream data
63668         0xF8B4          MPEG transport stream data
65360         0xFF50          MPEG transport stream data
66676         0x10474         MPEG transport stream data
68932         0x10D44         MPEG transport stream data
70060         0x111AC         MPEG transport stream data
72316         0x11A7C         MPEG transport stream data
73632         0x11FA0         MPEG transport stream data
74760         0x12408         MPEG transport stream data
75888         0x12870         MPEG transport stream data
76828         0x12C1C         MPEG transport stream data
77956         0x13084         MPEG transport stream data
78896         0x13430         MPEG transport stream data
80024         0x13898         MPEG transport stream data
81904         0x13FF0         MPEG transport stream data
83220         0x14514         MPEG transport stream data
84912         0x14BB0         MPEG transport stream data
87920         0x15770         MPEG transport stream data
89236         0x15C94         MPEG transport stream data
90928         0x16330         MPEG transport stream data
92432         0x16910         MPEG transport stream data
93748         0x16E34         MPEG transport stream data
95064         0x17358         MPEG transport stream data
96568         0x17938         MPEG transport stream data
98072         0x17F18         MPEG transport stream data
100704        0x18960         MPEG transport stream data
102020        0x18E84         MPEG transport stream data
102960        0x19230         MPEG transport stream data
104088        0x19698         MPEG transport stream data
105216        0x19B00         MPEG transport stream data
106344        0x19F68         MPEG transport stream data
107472        0x1A3D0         MPEG transport stream data
108412        0x1A77C         MPEG transport stream data
109540        0x1ABE4         MPEG transport stream data
111232        0x1B280         MPEG transport stream data
112736        0x1B860         MPEG transport stream data
114992        0x1C130         MPEG transport stream data
117248        0x1CA00         MPEG transport stream data
119880        0x1D448         MPEG transport stream data
122136        0x1DD18         MPEG transport stream data
124016        0x1E470         MPEG transport stream data
125144        0x1E8D8         MPEG transport stream data
126836        0x1EF74         MPEG transport stream data
128904        0x1F788         MPEG transport stream data
131160        0x20058         MPEG transport stream data
133792        0x20AA0         MPEG transport stream data
135108        0x20FC4         MPEG transport stream data
136424        0x214E8         MPEG transport stream data
137928        0x21AC8         MPEG transport stream data
139056        0x21F30         MPEG transport stream data
140184        0x22398         MPEG transport stream data
141312        0x22800         MPEG transport stream data
142252        0x22BAC         MPEG transport stream data
143380        0x23014         MPEG transport stream data
145260        0x2376C         MPEG transport stream data
146764        0x23D4C         MPEG transport stream data
148644        0x244A4         MPEG transport stream data
150524        0x24BFC         MPEG transport stream data
152968        0x25588         MPEG transport stream data
154096        0x259F0         MPEG transport stream data
155600        0x25FD0         MPEG transport stream data
157104        0x265B0         MPEG transport stream data
158608        0x26B90         MPEG transport stream data
159736        0x26FF8         MPEG transport stream data
161240        0x275D8         MPEG transport stream data
162932        0x27C74         MPEG transport stream data
164624        0x28310         MPEG transport stream data
165564        0x286BC         MPEG transport stream data
166692        0x28B24         MPEG transport stream data
167820        0x28F8C         MPEG transport stream data
168760        0x29338         MPEG transport stream data
169888        0x297A0         MPEG transport stream data
170828        0x29B4C         MPEG transport stream data
171956        0x29FB4         MPEG transport stream data
174212        0x2A884         MPEG transport stream data
175716        0x2AE64         MPEG transport stream data
177972        0x2B734         MPEG transport stream data
180604        0x2C17C         MPEG transport stream data
182672        0x2C990         MPEG transport stream data
183800        0x2CDF8         MPEG transport stream data
185680        0x2D550         MPEG transport stream data
186996        0x2DA74         MPEG transport stream data
188688        0x2E110         MPEG transport stream data
190004        0x2E634         MPEG transport stream data
191508        0x2EC14         MPEG transport stream data
193388        0x2F36C         MPEG transport stream data
194892        0x2F94C         MPEG transport stream data
196020        0x2FDB4         MPEG transport stream data
196960        0x30160         MPEG transport stream data
198088        0x305C8         MPEG transport stream data
199028        0x30974         MPEG transport stream data
200156        0x30DDC         MPEG transport stream data
201096        0x31188         MPEG transport stream data
202224        0x315F0         MPEG transport stream data
204104        0x31D48         MPEG transport stream data
205420        0x3226C         MPEG transport stream data
207300        0x329C4         MPEG transport stream data
209180        0x3311C         MPEG transport stream data
211248        0x33930         MPEG transport stream data
212752        0x33F10         MPEG transport stream data
213880        0x34378         MPEG transport stream data
215196        0x3489C         MPEG transport stream data
216512        0x34DC0         MPEG transport stream data
217828        0x352E4         MPEG transport stream data
219144        0x35808         MPEG transport stream data
221024        0x35F60         MPEG transport stream data
222904        0x366B8         MPEG transport stream data
224032        0x36B20         MPEG transport stream data
224972        0x36ECC         MPEG transport stream data
225912        0x37278         MPEG transport stream data
226852        0x37624         MPEG transport stream data
227980        0x37A8C         MPEG transport stream data
228920        0x37E38         MPEG transport stream data
230048        0x382A0         MPEG transport stream data
231928        0x389F8         MPEG transport stream data
233808        0x39150         MPEG transport stream data
236252        0x39ADC         MPEG transport stream data
237944        0x3A178         MPEG transport stream data
239824        0x3A8D0         MPEG transport stream data
241328        0x3AEB0         MPEG transport stream data
242832        0x3B490         MPEG transport stream data
243772        0x3B83C         MPEG transport stream data
245088        0x3BD60         MPEG transport stream data
246216        0x3C1C8         MPEG transport stream data
247532        0x3C6EC         MPEG transport stream data
249224        0x3CD88         MPEG transport stream data
250540        0x3D2AC         MPEG transport stream data
251480        0x3D658         MPEG transport stream data
252420        0x3DA04         MPEG transport stream data
253360        0x3DDB0         MPEG transport stream data
254300        0x3E15C         MPEG transport stream data
255428        0x3E5C4         MPEG transport stream data
256368        0x3E970         MPEG transport stream data
257496        0x3EDD8         MPEG transport stream data
259188        0x3F474         MPEG transport stream data
260128        0x3F820         MPEG transport stream data
261256        0x3FC88         MPEG transport stream data
262384        0x400F0         MPEG transport stream data
263700        0x40614         MPEG transport stream data
264640        0x409C0         MPEG transport stream data
265768        0x40E28         MPEG transport stream data
266708        0x411D4         MPEG transport stream data
268024        0x416F8         MPEG transport stream data
268964        0x41AA4         MPEG transport stream data
269904        0x41E50         MPEG transport stream data
270844        0x421FC         MPEG transport stream data
271972        0x42664         MPEG transport stream data
272912        0x42A10         MPEG transport stream data
273852        0x42DBC         MPEG transport stream data
274792        0x43168         MPEG transport stream data
275732        0x43514         MPEG transport stream data
276860        0x4397C         MPEG transport stream data
277800        0x43D28         MPEG transport stream data
278928        0x44190         MPEG transport stream data
280808        0x448E8         MPEG transport stream data
282688        0x45040         MPEG transport stream data
285132        0x459CC         MPEG transport stream data
286824        0x46068         MPEG transport stream data
288704        0x467C0         MPEG transport stream data
290208        0x46DA0         MPEG transport stream data
291712        0x47380         MPEG transport stream data
292652        0x4772C         MPEG transport stream data
293968        0x47C50         MPEG transport stream data
295096        0x480B8         MPEG transport stream data
296412        0x485DC         MPEG transport stream data
298104        0x48C78         MPEG transport stream data
299420        0x4919C         MPEG transport stream data
300360        0x49548         MPEG transport stream data
301300        0x498F4         MPEG transport stream data
302240        0x49CA0         MPEG transport stream data
303180        0x4A04C         MPEG transport stream data
304308        0x4A4B4         MPEG transport stream data
305248        0x4A860         MPEG transport stream data
306376        0x4ACC8         MPEG transport stream data
308068        0x4B364         MPEG transport stream data
309384        0x4B888         MPEG transport stream data
310512        0x4BCF0         MPEG transport stream data
311828        0x4C214         MPEG transport stream data
313520        0x4C8B0         MPEG transport stream data
314460        0x4CC5C         MPEG transport stream data
315776        0x4D180         MPEG transport stream data
316904        0x4D5E8         MPEG transport stream data
318220        0x4DB0C         MPEG transport stream data
319348        0x4DF74         MPEG transport stream data
321040        0x4E610         MPEG transport stream data
322356        0x4EB34         MPEG transport stream data
323672        0x4F058         MPEG transport stream data
324800        0x4F4C0         MPEG transport stream data
325740        0x4F86C         MPEG transport stream data
326680        0x4FC18         MPEG transport stream data
327620        0x4FFC4         MPEG transport stream data
328748        0x5042C         MPEG transport stream data
329688        0x507D8         MPEG transport stream data
330816        0x50C40         MPEG transport stream data
332696        0x51398         MPEG transport stream data
334012        0x518BC         MPEG transport stream data
335892        0x52014         MPEG transport stream data
337772        0x5276C         MPEG transport stream data
339840        0x52F80         MPEG transport stream data
341344        0x53560         MPEG transport stream data
342472        0x539C8         MPEG transport stream data
343788        0x53EEC         MPEG transport stream data
345104        0x54410         MPEG transport stream data
346420        0x54934         MPEG transport stream data
347736        0x54E58         MPEG transport stream data
349616        0x555B0         MPEG transport stream data
351496        0x55D08         MPEG transport stream data
352624        0x56170         MPEG transport stream data
353564        0x5651C         MPEG transport stream data
354504        0x568C8         MPEG transport stream data
355444        0x56C74         MPEG transport stream data
356572        0x570DC         MPEG transport stream data
357512        0x57488         MPEG transport stream data
358640        0x578F0         MPEG transport stream data
360520        0x58048         MPEG transport stream data
362024        0x58628         MPEG transport stream data
363904        0x58D80         MPEG transport stream data
365784        0x594D8         MPEG transport stream data
368228        0x59E64         MPEG transport stream data
369356        0x5A2CC         MPEG transport stream data
370860        0x5A8AC         MPEG transport stream data
372364        0x5AE8C         MPEG transport stream data
373868        0x5B46C         MPEG transport stream data
374996        0x5B8D4         MPEG transport stream data
376500        0x5BEB4         MPEG transport stream data
378192        0x5C550         MPEG transport stream data
379884        0x5CBEC         MPEG transport stream data
380824        0x5CF98         MPEG transport stream data
381952        0x5D400         MPEG transport stream data
383080        0x5D868         MPEG transport stream data
384020        0x5DC14         MPEG transport stream data
385148        0x5E07C         MPEG transport stream data
386088        0x5E428         MPEG transport stream data
387216        0x5E890         MPEG transport stream data
389096        0x5EFE8         MPEG transport stream data
390412        0x5F50C         MPEG transport stream data
392668        0x5FDDC         MPEG transport stream data
394736        0x605F0         MPEG transport stream data
396804        0x60E04         MPEG transport stream data
397932        0x6126C         MPEG transport stream data
399624        0x61908         MPEG transport stream data
401128        0x61EE8         MPEG transport stream data
402444        0x6240C         MPEG transport stream data
404136        0x62AA8         MPEG transport stream data
406016        0x63200         MPEG transport stream data
407144        0x63668         MPEG transport stream data
409400        0x63F38         MPEG transport stream data
410528        0x643A0         MPEG transport stream data
411656        0x64808         MPEG transport stream data
412596        0x64BB4         MPEG transport stream data
413724        0x6501C         MPEG transport stream data
414852        0x65484         MPEG transport stream data
415792        0x65830         MPEG transport stream data
416920        0x65C98         MPEG transport stream data
418612        0x66334         MPEG transport stream data
419552        0x666E0         MPEG transport stream data
421056        0x66CC0         MPEG transport stream data
422560        0x672A0         MPEG transport stream data
424252        0x6793C         MPEG transport stream data
425756        0x67F1C         MPEG transport stream data
426696        0x682C8         MPEG transport stream data
428012        0x687EC         MPEG transport stream data
429516        0x68DCC         MPEG transport stream data
430832        0x692F0         MPEG transport stream data
431772        0x6969C         MPEG transport stream data
433652        0x69DF4         MPEG transport stream data
435344        0x6A490         MPEG transport stream data
436472        0x6A8F8         MPEG transport stream data
437412        0x6ACA4         MPEG transport stream data
438352        0x6B050         MPEG transport stream data
439292        0x6B3FC         MPEG transport stream data
440420        0x6B864         MPEG transport stream data
441360        0x6BC10         MPEG transport stream data
442488        0x6C078         MPEG transport stream data
444180        0x6C714         MPEG transport stream data
445120        0x6CAC0         MPEG transport stream data
446248        0x6CF28         MPEG transport stream data
447376        0x6D390         MPEG transport stream data
448692        0x6D8B4         MPEG transport stream data
449632        0x6DC60         MPEG transport stream data
450760        0x6E0C8         MPEG transport stream data
451700        0x6E474         MPEG transport stream data
453016        0x6E998         MPEG transport stream data
453956        0x6ED44         MPEG transport stream data
454896        0x6F0F0         MPEG transport stream data
455836        0x6F49C         MPEG transport stream data
456964        0x6F904         MPEG transport stream data
457904        0x6FCB0         MPEG transport stream data
458844        0x7005C         MPEG transport stream data
459784        0x70408         MPEG transport stream data
460724        0x707B4         MPEG transport stream data
461852        0x70C1C         MPEG transport stream data
462792        0x70FC8         MPEG transport stream data
463920        0x71430         MPEG transport stream data
465800        0x71B88         MPEG transport stream data
467680        0x722E0         MPEG transport stream data
470124        0x72C6C         MPEG transport stream data
471816        0x73308         MPEG transport stream data
473696        0x73A60         MPEG transport stream data
475200        0x74040         MPEG transport stream data
476704        0x74620         MPEG transport stream data
477644        0x749CC         MPEG transport stream data
478960        0x74EF0         MPEG transport stream data
480088        0x75358         MPEG transport stream data
481404        0x7587C         MPEG transport stream data
483096        0x75F18         MPEG transport stream data
484412        0x7643C         MPEG transport stream data
485352        0x767E8         MPEG transport stream data
486292        0x76B94         MPEG transport stream data
487232        0x76F40         MPEG transport stream data
488172        0x772EC         MPEG transport stream data
489300        0x77754         MPEG transport stream data
490240        0x77B00         MPEG transport stream data
491368        0x77F68         MPEG transport stream data
493060        0x78604         MPEG transport stream data
494188        0x78A6C         MPEG transport stream data
495504        0x78F90         MPEG transport stream data
497196        0x7962C         MPEG transport stream data
499264        0x79E40         MPEG transport stream data
500768        0x7A420         MPEG transport stream data
502084        0x7A944         MPEG transport stream data
503024        0x7ACF0         MPEG transport stream data
504528        0x7B2D0         MPEG transport stream data
505844        0x7B7F4         MPEG transport stream data
507536        0x7BE90         MPEG transport stream data
509228        0x7C52C         MPEG transport stream data
510732        0x7CB0C         MPEG transport stream data
511672        0x7CEB8         MPEG transport stream data
512800        0x7D320         MPEG transport stream data
513928        0x7D788         MPEG transport stream data
514868        0x7DB34         MPEG transport stream data
515996        0x7DF9C         MPEG transport stream data
516936        0x7E348         MPEG transport stream data
518064        0x7E7B0         MPEG transport stream data
519756        0x7EE4C         MPEG transport stream data
520696        0x7F1F8         MPEG transport stream data
522576        0x7F950         MPEG transport stream data
524080        0x7FF30         MPEG transport stream data
525208        0x80398         MPEG transport stream data
526524        0x808BC         MPEG transport stream data
527840        0x80DE0         MPEG transport stream data
528968        0x81248         MPEG transport stream data
530096        0x816B0         MPEG transport stream data
531412        0x81BD4         MPEG transport stream data
532540        0x8203C         MPEG transport stream data
534608        0x82850         MPEG transport stream data
536112        0x82E30         MPEG transport stream data
537052        0x831DC         MPEG transport stream data
538180        0x83644         MPEG transport stream data
539120        0x839F0         MPEG transport stream data
540060        0x83D9C         MPEG transport stream data
541188        0x84204         MPEG transport stream data
542128        0x845B0         MPEG transport stream data
543256        0x84A18         MPEG transport stream data
544948        0x850B4         MPEG transport stream data
545888        0x85460         MPEG transport stream data
547016        0x858C8         MPEG transport stream data
548144        0x85D30         MPEG transport stream data
549460        0x86254         MPEG transport stream data
550400        0x86600         MPEG transport stream data
551528        0x86A68         MPEG transport stream data
552468        0x86E14         MPEG transport stream data
553784        0x87338         MPEG transport stream data
554724        0x876E4         MPEG transport stream data
555664        0x87A90         MPEG transport stream data
556604        0x87E3C         MPEG transport stream data
557732        0x882A4         MPEG transport stream data
558672        0x88650         MPEG transport stream data
559612        0x889FC         MPEG transport stream data
560552        0x88DA8         MPEG transport stream data
561492        0x89154         MPEG transport stream data
562620        0x895BC         MPEG transport stream data
563560        0x89968         MPEG transport stream data
564688        0x89DD0         MPEG transport stream data
566568        0x8A528         MPEG transport stream data
567696        0x8A990         MPEG transport stream data
569388        0x8B02C         MPEG transport stream data
570892        0x8B60C         MPEG transport stream data
572960        0x8BE20         MPEG transport stream data
573900        0x8C1CC         MPEG transport stream data
575216        0x8C6F0         MPEG transport stream data
576344        0x8CB58         MPEG transport stream data
577848        0x8D138         MPEG transport stream data
578788        0x8D4E4         MPEG transport stream data
580104        0x8DA08         MPEG transport stream data
581796        0x8E0A4         MPEG transport stream data
582924        0x8E50C         MPEG transport stream data
584052        0x8E974         MPEG transport stream data
584992        0x8ED20         MPEG transport stream data
585932        0x8F0CC         MPEG transport stream data
586872        0x8F478         MPEG transport stream data
588000        0x8F8E0         MPEG transport stream data
588940        0x8FC8C         MPEG transport stream data
590068        0x900F4         MPEG transport stream data
591948        0x9084C         MPEG transport stream data
593452        0x90E2C         MPEG transport stream data
595332        0x91584         MPEG transport stream data
597212        0x91CDC         MPEG transport stream data
599656        0x92668         MPEG transport stream data
600784        0x92AD0         MPEG transport stream data
602288        0x930B0         MPEG transport stream data
603792        0x93690         MPEG transport stream data
605296        0x93C70         MPEG transport stream data
606424        0x940D8         MPEG transport stream data
607928        0x946B8         MPEG transport stream data
609620        0x94D54         MPEG transport stream data
611312        0x953F0         MPEG transport stream data
612252        0x9579C         MPEG transport stream data
613380        0x95C04         MPEG transport stream data
614508        0x9606C         MPEG transport stream data
615448        0x96418         MPEG transport stream data
616576        0x96880         MPEG transport stream data
617516        0x96C2C         MPEG transport stream data
618644        0x97094         MPEG transport stream data
620524        0x977EC         MPEG transport stream data
621840        0x97D10         MPEG transport stream data
623720        0x98468         MPEG transport stream data
625600        0x98BC0         MPEG transport stream data
627668        0x993D4         MPEG transport stream data
629172        0x999B4         MPEG transport stream data
630300        0x99E1C         MPEG transport stream data
631616        0x9A340         MPEG transport stream data
632932        0x9A864         MPEG transport stream data
634248        0x9AD88         MPEG transport stream data
635564        0x9B2AC         MPEG transport stream data
637444        0x9BA04         MPEG transport stream data
639324        0x9C15C         MPEG transport stream data
640452        0x9C5C4         MPEG transport stream data
641392        0x9C970         MPEG transport stream data
642332        0x9CD1C         MPEG transport stream data
643272        0x9D0C8         MPEG transport stream data
644400        0x9D530         MPEG transport stream data
645340        0x9D8DC         MPEG transport stream data
646468        0x9DD44         MPEG transport stream data
648160        0x9E3E0         MPEG transport stream data
649476        0x9E904         MPEG transport stream data
650792        0x9EE28         MPEG transport stream data
653048        0x9F6F8         MPEG transport stream data
654176        0x9FB60         MPEG transport stream data
655680        0xA0140         MPEG transport stream data
656996        0xA0664         MPEG transport stream data
658124        0xA0ACC         MPEG transport stream data
659252        0xA0F34         MPEG transport stream data
660380        0xA139C         MPEG transport stream data
662072        0xA1A38         MPEG transport stream data
663200        0xA1EA0         MPEG transport stream data
664892        0xA253C         MPEG transport stream data
665832        0xA28E8         MPEG transport stream data
666772        0xA2C94         MPEG transport stream data
667712        0xA3040         MPEG transport stream data
668652        0xA33EC         MPEG transport stream data
669780        0xA3854         MPEG transport stream data
670720        0xA3C00         MPEG transport stream data
671848        0xA4068         MPEG transport stream data
673540        0xA4704         MPEG transport stream data
674668        0xA4B6C         MPEG transport stream data
676172        0xA514C         MPEG transport stream data
677488        0xA5670         MPEG transport stream data
678616        0xA5AD8         MPEG transport stream data
679744        0xA5F40         MPEG transport stream data
680872        0xA63A8         MPEG transport stream data
681812        0xA6754         MPEG transport stream data
683316        0xA6D34         MPEG transport stream data
684632        0xA7258         MPEG transport stream data
685572        0xA7604         MPEG transport stream data
687076        0xA7BE4         MPEG transport stream data
688956        0xA833C         MPEG transport stream data
689896        0xA86E8         MPEG transport stream data
690836        0xA8A94         MPEG transport stream data
691776        0xA8E40         MPEG transport stream data
692716        0xA91EC         MPEG transport stream data
693844        0xA9654         MPEG transport stream data
694784        0xA9A00         MPEG transport stream data
695912        0xA9E68         MPEG transport stream data
697792        0xAA5C0         MPEG transport stream data
699296        0xAABA0         MPEG transport stream data
701176        0xAB2F8         MPEG transport stream data
703056        0xABA50         MPEG transport stream data
705500        0xAC3DC         MPEG transport stream data
706628        0xAC844         MPEG transport stream data
708132        0xACE24         MPEG transport stream data
709636        0xAD404         MPEG transport stream data
711140        0xAD9E4         MPEG transport stream data
712268        0xADE4C         MPEG transport stream data
713772        0xAE42C         MPEG transport stream data
715464        0xAEAC8         MPEG transport stream data
717156        0xAF164         MPEG transport stream data
718096        0xAF510         MPEG transport stream data
719224        0xAF978         MPEG transport stream data
720352        0xAFDE0         MPEG transport stream data
721292        0xB018C         MPEG transport stream data
722420        0xB05F4         MPEG transport stream data
723360        0xB09A0         MPEG transport stream data
724488        0xB0E08         MPEG transport stream data
726180        0xB14A4         MPEG transport stream data
727308        0xB190C         MPEG transport stream data
729000        0xB1FA8         MPEG transport stream data
730316        0xB24CC         MPEG transport stream data
731444        0xB2934         MPEG transport stream data
732760        0xB2E58         MPEG transport stream data
734076        0xB337C         MPEG transport stream data
735204        0xB37E4         MPEG transport stream data
736332        0xB3C4C         MPEG transport stream data
737836        0xB422C         MPEG transport stream data
738776        0xB45D8         MPEG transport stream data
740468        0xB4C74         MPEG transport stream data
742724        0xB5544         MPEG transport stream data
743852        0xB59AC         MPEG transport stream data
744792        0xB5D58         MPEG transport stream data
745920        0xB61C0         MPEG transport stream data
746860        0xB656C         MPEG transport stream data
747988        0xB69D4         MPEG transport stream data
748928        0xB6D80         MPEG transport stream data
750056        0xB71E8         MPEG transport stream data
751748        0xB7884         MPEG transport stream data
752688        0xB7C30         MPEG transport stream data
753816        0xB8098         MPEG transport stream data
754944        0xB8500         MPEG transport stream data
756260        0xB8A24         MPEG transport stream data
757200        0xB8DD0         MPEG transport stream data
758328        0xB9238         MPEG transport stream data
759268        0xB95E4         MPEG transport stream data
760584        0xB9B08         MPEG transport stream data
761524        0xB9EB4         MPEG transport stream data
762464        0xBA260         MPEG transport stream data
763404        0xBA60C         MPEG transport stream data
764532        0xBAA74         MPEG transport stream data
765472        0xBAE20         MPEG transport stream data
766412        0xBB1CC         MPEG transport stream data
767352        0xBB578         MPEG transport stream data
768292        0xBB924         MPEG transport stream data
769420        0xBBD8C         MPEG transport stream data
770360        0xBC138         MPEG transport stream data
771488        0xBC5A0         MPEG transport stream data
773744        0xBCE70         MPEG transport stream data
775060        0xBD394         MPEG transport stream data
777128        0xBDBA8         MPEG transport stream data
779196        0xBE3BC         MPEG transport stream data
781264        0xBEBD0         MPEG transport stream data
782956        0xBF26C         MPEG transport stream data
784460        0xBF84C         MPEG transport stream data
785400        0xBFBF8         MPEG transport stream data
786904        0xC01D8         MPEG transport stream data
788220        0xC06FC         MPEG transport stream data
789724        0xC0CDC         MPEG transport stream data
791604        0xC1434         MPEG transport stream data
793108        0xC1A14         MPEG transport stream data
794236        0xC1E7C         MPEG transport stream data
795364        0xC22E4         MPEG transport stream data
796304        0xC2690         MPEG transport stream data
797244        0xC2A3C         MPEG transport stream data
798372        0xC2EA4         MPEG transport stream data
799312        0xC3250         MPEG transport stream data
800440        0xC36B8         MPEG transport stream data
802132        0xC3D54         MPEG transport stream data
803824        0xC43F0         MPEG transport stream data
806268        0xC4D7C         MPEG transport stream data
807396        0xC51E4         MPEG transport stream data
809464        0xC59F8         MPEG transport stream data
811344        0xC6150         MPEG transport stream data
812848        0xC6730         MPEG transport stream data
813788        0xC6ADC         MPEG transport stream data
815480        0xC7178         MPEG transport stream data
816796        0xC769C         MPEG transport stream data
818300        0xC7C7C         MPEG transport stream data
819992        0xC8318         MPEG transport stream data
821872        0xC8A70         MPEG transport stream data
823000        0xC8ED8         MPEG transport stream data
824128        0xC9340         MPEG transport stream data
825068        0xC96EC         MPEG transport stream data
826008        0xC9A98         MPEG transport stream data
827136        0xC9F00         MPEG transport stream data
828076        0xCA2AC         MPEG transport stream data
829204        0xCA714         MPEG transport stream data
830896        0xCADB0         MPEG transport stream data
831836        0xCB15C         MPEG transport stream data
833340        0xCB73C         MPEG transport stream data
834844        0xCBD1C         MPEG transport stream data
836536        0xCC3B8         MPEG transport stream data
838040        0xCC998         MPEG transport stream data
838980        0xCCD44         MPEG transport stream data
840296        0xCD268         MPEG transport stream data
841800        0xCD848         MPEG transport stream data
843116        0xCDD6C         MPEG transport stream data
844056        0xCE118         MPEG transport stream data
845936        0xCE870         MPEG transport stream data
847628        0xCEF0C         MPEG transport stream data
848756        0xCF374         MPEG transport stream data
849696        0xCF720         MPEG transport stream data
850636        0xCFACC         MPEG transport stream data
851576        0xCFE78         MPEG transport stream data
852704        0xD02E0         MPEG transport stream data
853644        0xD068C         MPEG transport stream data
854772        0xD0AF4         MPEG transport stream data
856464        0xD1190         MPEG transport stream data
857404        0xD153C         MPEG transport stream data
858532        0xD19A4         MPEG transport stream data
859660        0xD1E0C         MPEG transport stream data
860976        0xD2330         MPEG transport stream data
861916        0xD26DC         MPEG transport stream data
863044        0xD2B44         MPEG transport stream data
863984        0xD2EF0         MPEG transport stream data
865300        0xD3414         MPEG transport stream data
866240        0xD37C0         MPEG transport stream data
867180        0xD3B6C         MPEG transport stream data
868120        0xD3F18         MPEG transport stream data
869248        0xD4380         MPEG transport stream data
870188        0xD472C         MPEG transport stream data
871128        0xD4AD8         MPEG transport stream data
872068        0xD4E84         MPEG transport stream data
873008        0xD5230         MPEG transport stream data
874136        0xD5698         MPEG transport stream data
875076        0xD5A44         MPEG transport stream data
876204        0xD5EAC         MPEG transport stream data
877896        0xD6548         MPEG transport stream data
879212        0xD6A6C         MPEG transport stream data
880340        0xD6ED4         MPEG transport stream data
881656        0xD73F8         MPEG transport stream data
883348        0xD7A94         MPEG transport stream data
884288        0xD7E40         MPEG transport stream data
885604        0xD8364         MPEG transport stream data
886732        0xD87CC         MPEG transport stream data
888048        0xD8CF0         MPEG transport stream data
889176        0xD9158         MPEG transport stream data
890868        0xD97F4         MPEG transport stream data
892184        0xD9D18         MPEG transport stream data
893500        0xDA23C         MPEG transport stream data
894628        0xDA6A4         MPEG transport stream data
895568        0xDAA50         MPEG transport stream data
896508        0xDADFC         MPEG transport stream data
897448        0xDB1A8         MPEG transport stream data
898576        0xDB610         MPEG transport stream data
899516        0xDB9BC         MPEG transport stream data
900644        0xDBE24         MPEG transport stream data
902524        0xDC57C         MPEG transport stream data
903840        0xDCAA0         MPEG transport stream data
905720        0xDD1F8         MPEG transport stream data
907600        0xDD950         MPEG transport stream data
909668        0xDE164         MPEG transport stream data
911172        0xDE744         MPEG transport stream data
912300        0xDEBAC         MPEG transport stream data
913616        0xDF0D0         MPEG transport stream data
914932        0xDF5F4         MPEG transport stream data
916248        0xDFB18         MPEG transport stream data
917564        0xE003C         MPEG transport stream data
919444        0xE0794         MPEG transport stream data
921324        0xE0EEC         MPEG transport stream data
922452        0xE1354         MPEG transport stream data
923392        0xE1700         MPEG transport stream data
924332        0xE1AAC         MPEG transport stream data
925272        0xE1E58         MPEG transport stream data
926400        0xE22C0         MPEG transport stream data
927340        0xE266C         MPEG transport stream data
928468        0xE2AD4         MPEG transport stream data
930348        0xE322C         MPEG transport stream data
932228        0xE3984         MPEG transport stream data
934672        0xE4310         MPEG transport stream data
936364        0xE49AC         MPEG transport stream data
938244        0xE5104         MPEG transport stream data
939748        0xE56E4         MPEG transport stream data
941252        0xE5CC4         MPEG transport stream data
942192        0xE6070         MPEG transport stream data
943508        0xE6594         MPEG transport stream data
944636        0xE69FC         MPEG transport stream data
945952        0xE6F20         MPEG transport stream data
947644        0xE75BC         MPEG transport stream data
948960        0xE7AE0         MPEG transport stream data
949900        0xE7E8C         MPEG transport stream data
950840        0xE8238         MPEG transport stream data
951780        0xE85E4         MPEG transport stream data
952720        0xE8990         MPEG transport stream data
953848        0xE8DF8         MPEG transport stream data
954788        0xE91A4         MPEG transport stream data
955916        0xE960C         MPEG transport stream data
957608        0xE9CA8         MPEG transport stream data
958924        0xEA1CC         MPEG transport stream data
960240        0xEA6F0         MPEG transport stream data
962496        0xEAFC0         MPEG transport stream data
963624        0xEB428         MPEG transport stream data
965128        0xEBA08         MPEG transport stream data
966444        0xEBF2C         MPEG transport stream data
967572        0xEC394         MPEG transport stream data
968700        0xEC7FC         MPEG transport stream data
969828        0xECC64         MPEG transport stream data
971520        0xED300         MPEG transport stream data
972648        0xED768         MPEG transport stream data
974340        0xEDE04         MPEG transport stream data
975280        0xEE1B0         MPEG transport stream data
976220        0xEE55C         MPEG transport stream data
977160        0xEE908         MPEG transport stream data
978100        0xEECB4         MPEG transport stream data
979228        0xEF11C         MPEG transport stream data
980168        0xEF4C8         MPEG transport stream data
981296        0xEF930         MPEG transport stream data
982988        0xEFFCC         MPEG transport stream data
984116        0xF0434         MPEG transport stream data
985432        0xF0958         MPEG transport stream data
987124        0xF0FF4         MPEG transport stream data
989192        0xF1808         MPEG transport stream data
990696        0xF1DE8         MPEG transport stream data
992012        0xF230C         MPEG transport stream data
992952        0xF26B8         MPEG transport stream data
994456        0xF2C98         MPEG transport stream data
995772        0xF31BC         MPEG transport stream data
997464        0xF3858         MPEG transport stream data
999156        0xF3EF4         MPEG transport stream data
1000660       0xF44D4         MPEG transport stream data
1001600       0xF4880         MPEG transport stream data
1002728       0xF4CE8         MPEG transport stream data
1003856       0xF5150         MPEG transport stream data
1004796       0xF54FC         MPEG transport stream data
1005924       0xF5964         MPEG transport stream data
1006864       0xF5D10         MPEG transport stream data
1007992       0xF6178         MPEG transport stream data
1009684       0xF6814         MPEG transport stream data
1010624       0xF6BC0         MPEG transport stream data
1012504       0xF7318         MPEG transport stream data
1014008       0xF78F8         MPEG transport stream data
1015136       0xF7D60         MPEG transport stream data
1016452       0xF8284         MPEG transport stream data
1017768       0xF87A8         MPEG transport stream data
1018896       0xF8C10         MPEG transport stream data
1020024       0xF9078         MPEG transport stream data
1021340       0xF959C         MPEG transport stream data
1022468       0xF9A04         MPEG transport stream data
1024536       0xFA218         MPEG transport stream data
1026040       0xFA7F8         MPEG transport stream data
1026980       0xFABA4         MPEG transport stream data
1028108       0xFB00C         MPEG transport stream data
1029048       0xFB3B8         MPEG transport stream data
1029988       0xFB764         MPEG transport stream data
1031116       0xFBBCC         MPEG transport stream data
1032056       0xFBF78         MPEG transport stream data
1033184       0xFC3E0         MPEG transport stream data
1034876       0xFCA7C         MPEG transport stream data
1036568       0xFD118         MPEG transport stream data
1039012       0xFDAA4         MPEG transport stream data
1040140       0xFDF0C         MPEG transport stream data
1042208       0xFE720         MPEG transport stream data
1044088       0xFEE78         MPEG transport stream data
1045592       0xFF458         MPEG transport stream data
1046532       0xFF804         MPEG transport stream data
1048224       0xFFEA0         MPEG transport stream data
1049540       0x1003C4        MPEG transport stream data
1051044       0x1009A4        MPEG transport stream data
1052736       0x101040        MPEG transport stream data
1054616       0x101798        MPEG transport stream data
1055744       0x101C00        MPEG transport stream data
1056872       0x102068        MPEG transport stream data
1057812       0x102414        MPEG transport stream data
1058752       0x1027C0        MPEG transport stream data
1059880       0x102C28        MPEG transport stream data
1060820       0x102FD4        MPEG transport stream data
1061948       0x10343C        MPEG transport stream data
1063828       0x103B94        MPEG transport stream data
1065708       0x1042EC        MPEG transport stream data
1068152       0x104C78        MPEG transport stream data
1069844       0x105314        MPEG transport stream data
1071724       0x105A6C        MPEG transport stream data
1073228       0x10604C        MPEG transport stream data
1074732       0x10662C        MPEG transport stream data
1075672       0x1069D8        MPEG transport stream data
1076988       0x106EFC        MPEG transport stream data
1078116       0x107364        MPEG transport stream data
1079432       0x107888        MPEG transport stream data
1081124       0x107F24        MPEG transport stream data
1082440       0x108448        MPEG transport stream data
1083380       0x1087F4        MPEG transport stream data
1084320       0x108BA0        MPEG transport stream data
1085260       0x108F4C        MPEG transport stream data
1086200       0x1092F8        MPEG transport stream data
1087328       0x109760        MPEG transport stream data
1088268       0x109B0C        MPEG transport stream data
1089396       0x109F74        MPEG transport stream data
1091088       0x10A610        MPEG transport stream data
1092028       0x10A9BC        MPEG transport stream data
1093908       0x10B114        MPEG transport stream data
1095412       0x10B6F4        MPEG transport stream data
1096540       0x10BB5C        MPEG transport stream data
1097856       0x10C080        MPEG transport stream data
1099172       0x10C5A4        MPEG transport stream data
1100300       0x10CA0C        MPEG transport stream data
1101428       0x10CE74        MPEG transport stream data
1102744       0x10D398        MPEG transport stream data
1103872       0x10D800        MPEG transport stream data
1105940       0x10E014        MPEG transport stream data
1107444       0x10E5F4        MPEG transport stream data
1108384       0x10E9A0        MPEG transport stream data
1109512       0x10EE08        MPEG transport stream data
1110452       0x10F1B4        MPEG transport stream data
1111392       0x10F560        MPEG transport stream data
1112520       0x10F9C8        MPEG transport stream data
1113460       0x10FD74        MPEG transport stream data
1114588       0x1101DC        MPEG transport stream data
1116280       0x110878        MPEG transport stream data
1117220       0x110C24        MPEG transport stream data
1118348       0x11108C        MPEG transport stream data
1119476       0x1114F4        MPEG transport stream data
1120792       0x111A18        MPEG transport stream data
1121732       0x111DC4        MPEG transport stream data
1122860       0x11222C        MPEG transport stream data
1123800       0x1125D8        MPEG transport stream data
1125116       0x112AFC        MPEG transport stream data
1126056       0x112EA8        MPEG transport stream data
1126996       0x113254        MPEG transport stream data
1127936       0x113600        MPEG transport stream data
1129064       0x113A68        MPEG transport stream data
1130004       0x113E14        MPEG transport stream data
1130944       0x1141C0        MPEG transport stream data
1131884       0x11456C        MPEG transport stream data
1132824       0x114918        MPEG transport stream data
1133952       0x114D80        MPEG transport stream data
1134892       0x11512C        MPEG transport stream data
1136020       0x115594        MPEG transport stream data
1137900       0x115CEC        MPEG transport stream data
1139028       0x116154        MPEG transport stream data
1140908       0x1168AC        MPEG transport stream data
1142976       0x1170C0        MPEG transport stream data
1145044       0x1178D4        MPEG transport stream data
1146736       0x117F70        MPEG transport stream data
1147676       0x11831C        MPEG transport stream data
1149180       0x1188FC        MPEG transport stream data
1150872       0x118F98        MPEG transport stream data
1152188       0x1194BC        MPEG transport stream data
1154444       0x119D8C        MPEG transport stream data
1155572       0x11A1F4        MPEG transport stream data
1157828       0x11AAC4        MPEG transport stream data
1159144       0x11AFE8        MPEG transport stream data
1160272       0x11B450        MPEG transport stream data
1161400       0x11B8B8        MPEG transport stream data
1162340       0x11BC64        MPEG transport stream data
1163468       0x11C0CC        MPEG transport stream data
1164408       0x11C478        MPEG transport stream data
1165536       0x11C8E0        MPEG transport stream data
1167228       0x11CF7C        MPEG transport stream data
1168356       0x11D3E4        MPEG transport stream data
1169672       0x11D908        MPEG transport stream data
1171176       0x11DEE8        MPEG transport stream data
1172868       0x11E584        MPEG transport stream data
1174372       0x11EB64        MPEG transport stream data
1175688       0x11F088        MPEG transport stream data
1176628       0x11F434        MPEG transport stream data
1178132       0x11FA14        MPEG transport stream data
1179636       0x11FFF4        MPEG transport stream data
1181328       0x120690        MPEG transport stream data
1182456       0x120AF8        MPEG transport stream data
1184900       0x121484        MPEG transport stream data
1186028       0x1218EC        MPEG transport stream data
1187156       0x121D54        MPEG transport stream data
1188096       0x122100        MPEG transport stream data
1189036       0x1224AC        MPEG transport stream data
1190164       0x122914        MPEG transport stream data
1191104       0x122CC0        MPEG transport stream data
1192232       0x123128        MPEG transport stream data
1193924       0x1237C4        MPEG transport stream data
1195052       0x123C2C        MPEG transport stream data
1196744       0x1242C8        MPEG transport stream data
1198060       0x1247EC        MPEG transport stream data
1199188       0x124C54        MPEG transport stream data
1200504       0x125178        MPEG transport stream data
1201820       0x12569C        MPEG transport stream data
1202948       0x125B04        MPEG transport stream data
1204076       0x125F6C        MPEG transport stream data
1205580       0x12654C        MPEG transport stream data
1206520       0x1268F8        MPEG transport stream data
1208212       0x126F94        MPEG transport stream data
1210468       0x127864        MPEG transport stream data
1211596       0x127CCC        MPEG transport stream data
1212536       0x128078        MPEG transport stream data
1213664       0x1284E0        MPEG transport stream data
1214604       0x12888C        MPEG transport stream data
1215732       0x128CF4        MPEG transport stream data
1216672       0x1290A0        MPEG transport stream data
1217800       0x129508        MPEG transport stream data
1219868       0x129D1C        MPEG transport stream data
1220996       0x12A184        MPEG transport stream data
1222876       0x12A8DC        MPEG transport stream data
1224192       0x12AE00        MPEG transport stream data
1225696       0x12B3E0        MPEG transport stream data
1227012       0x12B904        MPEG transport stream data
1228328       0x12BE28        MPEG transport stream data
1229268       0x12C1D4        MPEG transport stream data
1230584       0x12C6F8        MPEG transport stream data
1231712       0x12CB60        MPEG transport stream data
1233028       0x12D084        MPEG transport stream data
1234344       0x12D5A8        MPEG transport stream data
1235660       0x12DACC        MPEG transport stream data
1236600       0x12DE78        MPEG transport stream data
1237540       0x12E224        MPEG transport stream data
1238480       0x12E5D0        MPEG transport stream data
1239420       0x12E97C        MPEG transport stream data
1240548       0x12EDE4        MPEG transport stream data
1241488       0x12F190        MPEG transport stream data
1242616       0x12F5F8        MPEG transport stream data
1244308       0x12FC94        MPEG transport stream data
1245624       0x1301B8        MPEG transport stream data
1246752       0x130620        MPEG transport stream data
1248068       0x130B44        MPEG transport stream data
1249760       0x1311E0        MPEG transport stream data
1250700       0x13158C        MPEG transport stream data
1252016       0x131AB0        MPEG transport stream data
1253144       0x131F18        MPEG transport stream data
1254460       0x13243C        MPEG transport stream data
1255588       0x1328A4        MPEG transport stream data
1257280       0x132F40        MPEG transport stream data
1258596       0x133464        MPEG transport stream data
1259912       0x133988        MPEG transport stream data
1261040       0x133DF0        MPEG transport stream data
1261980       0x13419C        MPEG transport stream data
1262920       0x134548        MPEG transport stream data
1263860       0x1348F4        MPEG transport stream data
1264988       0x134D5C        MPEG transport stream data
1265928       0x135108        MPEG transport stream data
1267056       0x135570        MPEG transport stream data
1268748       0x135C0C        MPEG transport stream data
1270064       0x136130        MPEG transport stream data
1271192       0x136598        MPEG transport stream data
1272508       0x136ABC        MPEG transport stream data
1274200       0x137158        MPEG transport stream data
1275140       0x137504        MPEG transport stream data
1276456       0x137A28        MPEG transport stream data
1277584       0x137E90        MPEG transport stream data
1278900       0x1383B4        MPEG transport stream data
1280028       0x13881C        MPEG transport stream data
1281720       0x138EB8        MPEG transport stream data
1283036       0x1393DC        MPEG transport stream data
1284352       0x139900        MPEG transport stream data
1285480       0x139D68        MPEG transport stream data
1286420       0x13A114        MPEG transport stream data
1287360       0x13A4C0        MPEG transport stream data
1288300       0x13A86C        MPEG transport stream data
1289428       0x13ACD4        MPEG transport stream data
1290368       0x13B080        MPEG transport stream data
1291496       0x13B4E8        MPEG transport stream data
1293188       0x13BB84        MPEG transport stream data
1294504       0x13C0A8        MPEG transport stream data
1296196       0x13C744        MPEG transport stream data
1297888       0x13CDE0        MPEG transport stream data
1299580       0x13D47C        MPEG transport stream data
1300896       0x13D9A0        MPEG transport stream data
1301836       0x13DD4C        MPEG transport stream data
1303152       0x13E270        MPEG transport stream data
1304844       0x13E90C        MPEG transport stream data
1306160       0x13EE30        MPEG transport stream data
1307100       0x13F1DC        MPEG transport stream data
1308980       0x13F934        MPEG transport stream data
1310484       0x13FF14        MPEG transport stream data
1311612       0x14037C        MPEG transport stream data
1312740       0x1407E4        MPEG transport stream data
1313680       0x140B90        MPEG transport stream data
1314620       0x140F3C        MPEG transport stream data
1315748       0x1413A4        MPEG transport stream data
1316688       0x141750        MPEG transport stream data
1317816       0x141BB8        MPEG transport stream data
1319696       0x142310        MPEG transport stream data
1321012       0x142834        MPEG transport stream data
1322704       0x142ED0        MPEG transport stream data
1325712       0x143A90        MPEG transport stream data
1327028       0x143FB4        MPEG transport stream data
1328720       0x144650        MPEG transport stream data
1330224       0x144C30        MPEG transport stream data
1331540       0x145154        MPEG transport stream data
1332856       0x145678        MPEG transport stream data
1334360       0x145C58        MPEG transport stream data
1335864       0x146238        MPEG transport stream data
1338496       0x146C80        MPEG transport stream data
1339812       0x1471A4        MPEG transport stream data
1340752       0x147550        MPEG transport stream data
1341880       0x1479B8        MPEG transport stream data
1343008       0x147E20        MPEG transport stream data
1344136       0x148288        MPEG transport stream data
1345264       0x1486F0        MPEG transport stream data
1346204       0x148A9C        MPEG transport stream data
1347332       0x148F04        MPEG transport stream data
1349212       0x14965C        MPEG transport stream data
1350340       0x149AC4        MPEG transport stream data
1352220       0x14A21C        MPEG transport stream data
1353536       0x14A740        MPEG transport stream data
1355228       0x14ADDC        MPEG transport stream data
1356732       0x14B3BC        MPEG transport stream data
1358236       0x14B99C        MPEG transport stream data
1359176       0x14BD48        MPEG transport stream data
1360868       0x14C3E4        MPEG transport stream data
1362372       0x14C9C4        MPEG transport stream data
1363688       0x14CEE8        MPEG transport stream data
1365192       0x14D4C8        MPEG transport stream data
1366696       0x14DAA8        MPEG transport stream data
1367636       0x14DE54        MPEG transport stream data
1368764       0x14E2BC        MPEG transport stream data
1369704       0x14E668        MPEG transport stream data
1370644       0x14EA14        MPEG transport stream data
1371772       0x14EE7C        MPEG transport stream data
1372712       0x14F228        MPEG transport stream data
1373840       0x14F690        MPEG transport stream data
1375532       0x14FD2C        MPEG transport stream data
1376472       0x1500D8        MPEG transport stream data
1378352       0x150830        MPEG transport stream data
1379856       0x150E10        MPEG transport stream data
1380984       0x151278        MPEG transport stream data
1382300       0x15179C        MPEG transport stream data
1383616       0x151CC0        MPEG transport stream data
1384744       0x152128        MPEG transport stream data
1385872       0x152590        MPEG transport stream data
1387188       0x152AB4        MPEG transport stream data
1388316       0x152F1C        MPEG transport stream data
1390384       0x153730        MPEG transport stream data
1391888       0x153D10        MPEG transport stream data
1392828       0x1540BC        MPEG transport stream data
1393956       0x154524        MPEG transport stream data
1394896       0x1548D0        MPEG transport stream data
1395836       0x154C7C        MPEG transport stream data
1396964       0x1550E4        MPEG transport stream data
1397904       0x155490        MPEG transport stream data
1399032       0x1558F8        MPEG transport stream data
1400724       0x155F94        MPEG transport stream data
1401664       0x156340        MPEG transport stream data
1403168       0x156920        MPEG transport stream data
1404672       0x156F00        MPEG transport stream data
1406364       0x15759C        MPEG transport stream data
1407868       0x157B7C        MPEG transport stream data
1408808       0x157F28        MPEG transport stream data
1410124       0x15844C        MPEG transport stream data
1411628       0x158A2C        MPEG transport stream data
1412944       0x158F50        MPEG transport stream data
1413884       0x1592FC        MPEG transport stream data
1415764       0x159A54        MPEG transport stream data
1417456       0x15A0F0        MPEG transport stream data
1418584       0x15A558        MPEG transport stream data
1419524       0x15A904        MPEG transport stream data
1420464       0x15ACB0        MPEG transport stream data
1421404       0x15B05C        MPEG transport stream data
1422532       0x15B4C4        MPEG transport stream data
1423472       0x15B870        MPEG transport stream data
1424600       0x15BCD8        MPEG transport stream data
1426292       0x15C374        MPEG transport stream data
1427608       0x15C898        MPEG transport stream data
1428736       0x15CD00        MPEG transport stream data
1430240       0x15D2E0        MPEG transport stream data
1431932       0x15D97C        MPEG transport stream data
1433248       0x15DEA0        MPEG transport stream data
1434188       0x15E24C        MPEG transport stream data
1435504       0x15E770        MPEG transport stream data
1436820       0x15EC94        MPEG transport stream data
1437948       0x15F0FC        MPEG transport stream data
1439640       0x15F798        MPEG transport stream data
1440956       0x15FCBC        MPEG transport stream data
1443212       0x16058C        MPEG transport stream data
1444152       0x160938        MPEG transport stream data
1445280       0x160DA0        MPEG transport stream data
1446220       0x16114C        MPEG transport stream data
1447160       0x1614F8        MPEG transport stream data
1448288       0x161960        MPEG transport stream data
1449228       0x161D0C        MPEG transport stream data
1450356       0x162174        MPEG transport stream data
1452048       0x162810        MPEG transport stream data
1453176       0x162C78        MPEG transport stream data
1455056       0x1633D0        MPEG transport stream data
1457124       0x163BE4        MPEG transport stream data
1459380       0x1644B4        MPEG transport stream data
1461072       0x164B50        MPEG transport stream data
1462388       0x165074        MPEG transport stream data
1463328       0x165420        MPEG transport stream data
1464644       0x165944        MPEG transport stream data
1466336       0x165FE0        MPEG transport stream data
1467276       0x16638C        MPEG transport stream data
1469532       0x166C5C        MPEG transport stream data
1471600       0x167470        MPEG transport stream data
1472728       0x1678D8        MPEG transport stream data
1473856       0x167D40        MPEG transport stream data
1474796       0x1680EC        MPEG transport stream data
1475736       0x168498        MPEG transport stream data
1476864       0x168900        MPEG transport stream data
1477804       0x168CAC        MPEG transport stream data
1478932       0x169114        MPEG transport stream data
1480624       0x1697B0        MPEG transport stream data
1482128       0x169D90        MPEG transport stream data
1484384       0x16A660        MPEG transport stream data
1486640       0x16AF30        MPEG transport stream data
1489272       0x16B978        MPEG transport stream data
1491528       0x16C248        MPEG transport stream data
1493408       0x16C9A0        MPEG transport stream data
1494536       0x16CE08        MPEG transport stream data
1496228       0x16D4A4        MPEG transport stream data
1498296       0x16DCB8        MPEG transport stream data
1500552       0x16E588        MPEG transport stream data
1503184       0x16EFD0        MPEG transport stream data
1504500       0x16F4F4        MPEG transport stream data
1505816       0x16FA18        MPEG transport stream data
1507320       0x16FFF8        MPEG transport stream data
1508448       0x170460        MPEG transport stream data
1509576       0x1708C8        MPEG transport stream data
1510704       0x170D30        MPEG transport stream data
1511644       0x1710DC        MPEG transport stream data
1512772       0x171544        MPEG transport stream data
1514652       0x171C9C        MPEG transport stream data
1516156       0x17227C        MPEG transport stream data
1518224       0x172A90        MPEG transport stream data
1519916       0x17312C        MPEG transport stream data
1521232       0x173650        MPEG transport stream data
1522736       0x173C30        MPEG transport stream data
1524052       0x174154        MPEG transport stream data
1525368       0x174678        MPEG transport stream data
1526496       0x174AE0        MPEG transport stream data
1528000       0x1750C0        MPEG transport stream data
1529504       0x1756A0        MPEG transport stream data
1531008       0x175C80        MPEG transport stream data
1532324       0x1761A4        MPEG transport stream data
1533264       0x176550        MPEG transport stream data
1534392       0x1769B8        MPEG transport stream data
1535332       0x176D64        MPEG transport stream data
1536272       0x177110        MPEG transport stream data
1537400       0x177578        MPEG transport stream data
1538340       0x177924        MPEG transport stream data
1539468       0x177D8C        MPEG transport stream data
1541724       0x17865C        MPEG transport stream data
1543416       0x178CF8        MPEG transport stream data
1545296       0x179450        MPEG transport stream data
1547552       0x179D20        MPEG transport stream data
1549620       0x17A534        MPEG transport stream data
1551312       0x17ABD0        MPEG transport stream data
1552440       0x17B038        MPEG transport stream data
1554132       0x17B6D4        MPEG transport stream data
1555824       0x17BD70        MPEG transport stream data
1557140       0x17C294        MPEG transport stream data
1558832       0x17C930        MPEG transport stream data
1560712       0x17D088        MPEG transport stream data
1563156       0x17DA14        MPEG transport stream data
1564472       0x17DF38        MPEG transport stream data
1565600       0x17E3A0        MPEG transport stream data
1566728       0x17E808        MPEG transport stream data
1567668       0x17EBB4        MPEG transport stream data
1568796       0x17F01C        MPEG transport stream data
1569736       0x17F3C8        MPEG transport stream data
1570864       0x17F830        MPEG transport stream data
1572556       0x17FECC        MPEG transport stream data
1573872       0x1803F0        MPEG transport stream data
1575564       0x180A8C        MPEG transport stream data
1577068       0x18106C        MPEG transport stream data
1578760       0x181708        MPEG transport stream data
1580264       0x181CE8        MPEG transport stream data
1581204       0x182094        MPEG transport stream data
1582520       0x1825B8        MPEG transport stream data
1584024       0x182B98        MPEG transport stream data
1585340       0x1830BC        MPEG transport stream data
1586280       0x183468        MPEG transport stream data
1587972       0x183B04        MPEG transport stream data
1589476       0x1840E4        MPEG transport stream data
1590604       0x18454C        MPEG transport stream data
1591544       0x1848F8        MPEG transport stream data
1592672       0x184D60        MPEG transport stream data
1593612       0x18510C        MPEG transport stream data
1594740       0x185574        MPEG transport stream data
1595680       0x185920        MPEG transport stream data
1596808       0x185D88        MPEG transport stream data
1598688       0x1864E0        MPEG transport stream data
1599816       0x186948        MPEG transport stream data
1601320       0x186F28        MPEG transport stream data
1603388       0x18773C        MPEG transport stream data
1604704       0x187C60        MPEG transport stream data
1606396       0x1882FC        MPEG transport stream data
1607712       0x188820        MPEG transport stream data
1608840       0x188C88        MPEG transport stream data
1609968       0x1890F0        MPEG transport stream data
1611472       0x1896D0        MPEG transport stream data
1612412       0x189A7C        MPEG transport stream data
1613728       0x189FA0        MPEG transport stream data
1615044       0x18A4C4        MPEG transport stream data
1616172       0x18A92C        MPEG transport stream data
1617112       0x18ACD8        MPEG transport stream data
1618052       0x18B084        MPEG transport stream data
1618992       0x18B430        MPEG transport stream data
1620120       0x18B898        MPEG transport stream data
1621060       0x18BC44        MPEG transport stream data
1622188       0x18C0AC        MPEG transport stream data
1623880       0x18C748        MPEG transport stream data
1625196       0x18CC6C        MPEG transport stream data
1626888       0x18D308        MPEG transport stream data
1628392       0x18D8E8        MPEG transport stream data
1630084       0x18DF84        MPEG transport stream data
1631588       0x18E564        MPEG transport stream data
1632528       0x18E910        MPEG transport stream data
1633844       0x18EE34        MPEG transport stream data
1635348       0x18F414        MPEG transport stream data
1636664       0x18F938        MPEG transport stream data
1637604       0x18FCE4        MPEG transport stream data
1639296       0x190380        MPEG transport stream data
1640800       0x190960        MPEG transport stream data
1641928       0x190DC8        MPEG transport stream data
1642868       0x191174        MPEG transport stream data
1643996       0x1915DC        MPEG transport stream data
1644936       0x191988        MPEG transport stream data
1646064       0x191DF0        MPEG transport stream data
1647004       0x19219C        MPEG transport stream data

                                                                                                                   
┌──(kali㉿kali)-[/media/sf_k/ugra ctf 2025-quals/forensic/Вещает, видимо ]
└─$ ffmpeg -r 25 -i udp -c:v copy udp.mp4     
ffmpeg version 7.1-4 Copyright (c) 2000-2024 the FFmpeg developers
  built with gcc 14 (Debian 14.2.0-17)
  configuration: --prefix=/usr --extra-version=4 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --arch=amd64 --enable-gpl --disable-stripping --disable-libmfx --disable-omx --enable-gnutls --enable-libaom --enable-libass --enable-libbs2b --enable-libcdio --enable-libcodec2 --enable-libdav1d --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libglslang --enable-libgme --enable-libgsm --enable-libharfbuzz --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-librubberband --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzimg --enable-openal --enable-opencl --enable-opengl --disable-sndio --enable-libvpl --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-ladspa --enable-libbluray --enable-libcaca --enable-libdvdnav --enable-libdvdread --enable-libjack --enable-libpulse --enable-librabbitmq --enable-librist --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libx264 --enable-libzmq --enable-libzvbi --enable-lv2 --enable-sdl2 --enable-libplacebo --enable-librav1e --enable-pocketsphinx --enable-librsvg --enable-libjxl --enable-shared
  libavutil      59. 39.100 / 59. 39.100
  libavcodec     61. 19.100 / 61. 19.100
  libavformat    61.  7.100 / 61.  7.100
  libavdevice    61.  3.100 / 61.  3.100
  libavfilter    10.  4.100 / 10.  4.100
  libswscale      8.  3.100 /  8.  3.100
  libswresample   5.  3.100 /  5.  3.100
  libpostproc    58.  3.100 / 58.  3.100
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[h264 @ 0x559c2a03e300] non-existing PPS 0 referenced                                                              
    Last message repeated 1 times                                                                                  
[h264 @ 0x559c2a03e300] decode_slice_header error
[h264 @ 0x559c2a03e300] no frame!                                                                                  
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
    Last message repeated 8 times                                                                                  
Input #0, mpegts, from 'udp':
  Duration: 00:00:02.28, start: 1.600000, bitrate: 5794 kb/s
  Program 1 
    Metadata:
      service_name    : Service01
      service_provider: FFmpeg
  Stream #0:0[0x100]: Video: h264 (High 4:4:4 Predictive) ([27][0][0][0] / 0x001B), yuv444p(progressive), 320x240, 25 fps, 25 tbr, 90k tbn
Stream mapping:
  Stream #0:0 -> #0:0 (copy)
Output #0, mp4, to 'udp.mp4':
  Metadata:
    encoder         : Lavf61.7.100
  Stream #0:0: Video: h264 (High 4:4:4 Predictive) (avc1 / 0x31637661), yuv444p(progressive), 320x240, q=2-31, 25 fps, 25 tbr, 12800 tbn
Press [q] to stop, [?] for help
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 2400000            
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 4800000            
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 7200000            
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 9600000            
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 12000000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 14400000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 16800000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 19200000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 21600000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 24000000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 26400000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 28800000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 31200000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 33600000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 36000000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 38400000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 40800000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 43200000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 45600000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 48000000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 50400000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 52800000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 55200000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 57600000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 60000000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 62400000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 64800000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 67200000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 69600000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 72000000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 74400000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 76800000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 79200000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 81600000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 84000000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 86400000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 88800000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 91200000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 93600000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 96000000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 98400000           
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 100800000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 103200000          
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 105600000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 108000000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 110400000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 112800000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 115200000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 117600000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 120000000          
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 122400000          
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 124800000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 127200000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 129600000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 132000000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 134400000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 136800000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 139200000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 141600000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 144000000          
[mpegts @ 0x559c2a038cc0] Packet corrupt (stream = 0, dts = 338400).                                               
[in#0/mpegts @ 0x559c2a038a00] corrupt input packet in stream 0                                                    
[vist#0:0/h264 @ 0x559c2a090100] timestamp discontinuity (stream id=256): -2400000, new offset= 146400000          
[out#0/mp4 @ 0x559c2a14d500] video:629KiB audio:0KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 6.673366%
frame= 3660 fps=0.0 q=-1.0 Lsize=     671KiB time=00:02:28.60 bitrate=  37.0kbits/s speed=2.3e+03x    
                                                                                                                   
┌──(kali㉿kali)-[/media/sf_k/ugra ctf 2025-quals/forensic/Вещает, видимо ]
└─$ 
флаг: ugra_abrupt_and_furious_yet_braindead_2wsobb476dtzj
