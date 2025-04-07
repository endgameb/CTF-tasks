#!/usr/bin/env python3
import piexif

# Загружаем EXIF-данные
exif_dict = piexif.load("original.jpg")

# Базовая дата
date_basic = "1970:01:01 00:00:00"
date_subsec = "1970:01:01 00:00:00.001"
date_samsung = "1970:01:01 00:00:00.001+00:00"

# Убеждаемся, что все необходимые секции существуют
if "0th" not in exif_dict:
    exif_dict["0th"] = {}
if "Exif" not in exif_dict:
    exif_dict["Exif"] = {}

# Устанавливаем основные теги даты
exif_dict["0th"][306] = date_basic.encode('utf-8')  # ModifyDate
exif_dict["Exif"][36867] = date_basic.encode('utf-8')  # DateTimeOriginal
exif_dict["Exif"][36868] = date_basic.encode('utf-8')  # CreateDate

# Устанавливаем SubSec теги
exif_dict["Exif"][37520] = "001".encode('utf-8')  # SubSecTime
exif_dict["Exif"][37521] = "001".encode('utf-8')  # SubSecTimeOriginal
exif_dict["Exif"][37522] = "001".encode('utf-8')  # SubSecTimeDigitized

# Устанавливаем Samsung TimeStamp
makernote_dict = {515: date_samsung.encode('utf-8')}
exif_dict["0th"][317] = str(makernote_dict).encode('utf-8')

# Сохраняем изменения
exif_bytes = piexif.dump(exif_dict)
piexif.insert(exif_bytes, "original.jpg")
