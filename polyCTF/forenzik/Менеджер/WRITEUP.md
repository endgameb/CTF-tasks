используем скрипт для извлечения данных
содержание скрипта
import Evtx.Evtx as evtx

with evtx.Evtx("manager.evtx") as log:
    for record in log.records():
        xml_content = record.xml()
        # Теперь xml_content содержит XML представление записи
        print(xml_content)



┌──(kali㉿kali)-[/media/sf_k/poly/Менеджер]
└─$ python3 1.py > 1.txt
                                                                                                                   
┌──(kali㉿kali)-[/media/sf_k/poly/Менеджер]
└─$ grep "DriveName" 1.txt 
<EventData><Data Name="DriveName">C:</Data>
<EventData><Data Name="DriveName">C:</Data>
<EventData><Data Name="DriveName">\\?\Volume{2fc5429d-09ce-46c7-ab68-f2ee9e9fa131}</Data>
<EventData><Data Name="DriveName">C:</Data>
<EventData><Data Name="DriveName">\\?\Volume{2fc5429d-09ce-46c7-ab68-f2ee9e9fa131}</Data>
<EventData><Data Name="DriveName">C:</Data>
<EventData><Data Name="DriveName">\\?\Volume{2fc5429d-09ce-46c7-ab68-f2ee9e9fa131}</Data>
                                                                                                                   
┌──(kali㉿kali)-[/media/sf_k/poly/Менеджер]
└─$ 
флаг: PolyCTF{2fc5429d-09ce-46c7-ab68-f2ee9e9fa131}
