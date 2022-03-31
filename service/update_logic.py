import os.path
import time
import urllib.request
import datetime
from datetime import datetime
import requests
import convert
from pytz import timezone
from db import save_img_groups_to_file

TIME_ZONE = timezone("Asia/Krasnoyarsk")

timetable_old_size = {}


def load_on_start_all_files_xlsx():
    global timetable_old_size
    for college_number in range(1, 5):
        url = f'http://www.bgtc.su/wp-content/uploads/raspisanie/zamena{college_number}k.xlsx'
        file = requests.get(url)
        with open(f'../sheduleXLSX/zamena{college_number}k.xlsx', 'wb') as file_xlsx:
            file_xlsx.write(file.content)
        timetable_old_size[f'timetable_old_size{college_number}'] = os.path.getsize(
            f'../sheduleXLSX/zamena{college_number}k.xlsx')
        save_img_groups_to_file(f'../sheduleXLSX/zamena{college_number}k.xlsx', college_number)


def load_on_start_all_files():
    load_on_start_all_files_xlsx()  # load all xlsx file
    convert.start_load_all_files_png()  # load all png files


load_on_start_all_files_xlsx()
print(timetable_old_size)


def comparison_size_bgc(college_number: int, timetable_size: dict) -> None:
    """Проверяем размер исходного(старого файла с расписанием)
     с новым, если они не равны - отсылаем запрос"""
    print('пошла')
    url = f'http://www.bgtc.su/wp-content/uploads/raspisanie/zamena{college_number}k.xlsx'
    print(college_number)
    timetable_new_size = int(urllib.request.urlopen(url).info()['Content-Length'])
    if timetable_new_size != timetable_size[f'timetable_old_size{college_number}']:
        timetable_old_size[f'timetable_old_size{college_number}'] = timetable_new_size
        file = requests.get(url)
        with open(f'../sheduleXLSX/zamena{college_number}k.xlsx', 'wb') as file_xlsx:
            file_xlsx.write(file.content)
        save_img_groups_to_file(f'../sheduleXLSX/zamena{college_number}k.xlsx', college_number)
        convert.start_load_file_png(college_number)


def check_shedule():
    while True:
        hour_biysk = datetime.now(TIME_ZONE).strftime('%H%M%S')
        if int(hour_biysk) in range(100000, 200000):
            [comparison_size_bgc(i, timetable_old_size) for i in range(1, 5)]
            time.sleep(180)
        else:
            time.sleep(360)


