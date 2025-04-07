import Evtx.Evtx as evtx

with evtx.Evtx("manager.evtx") as log:
    for record in log.records():
        xml_content = record.xml()
        # Теперь xml_content содержит XML представление записи
        print(xml_content)