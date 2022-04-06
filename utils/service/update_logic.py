import os.path
import time
import urllib.request
import datetime
from datetime import datetime
import requests
import logging
from pytz import timezone

from .convert import *
from .db import save_img_groups_to_file

TIME_ZONE = timezone("Asia/Krasnoyarsk")

timetable_old_size = {}


async def load_on_start_all_files_xlsx():
    global timetable_old_size
    for college_number in range(1, 5):
        url = f'http://www.bgtc.su/wp-content/uploads/raspisanie/zamena{college_number}k.xlsx'
        file = requests.get(url)
        with open(f'media/sheduleXLSX/zamena{college_number}k.xlsx', 'wb') as file_xlsx:
            file_xlsx.write(file.content)
        timetable_old_size[f'timetable_old_size{college_number}'] = os.path.getsize(
            f'media/sheduleXLSX/zamena{college_number}k.xlsx')
        logging.info(f'load xlsx file college {college_number}')
        await save_img_groups_to_file(f'media/sheduleXLSX/zamena{college_number}k.xlsx', college_number)


async def comparison_size_bgc(college_number: int, timetable_size: dict) -> None:
    """Проверяем размер исходного(старого файла с расписанием)
     с новым, если они не равны - отсылаем запрос"""
    logging.info(f'start check size bgc shedule file college {college_number}')
    url = f'http://www.bgtc.su/wp-content/uploads/raspisanie/zamena{college_number}k.xlsx'
    timetable_new_size = int(urllib.request.urlopen(url).info()['Content-Length'])
    if timetable_new_size != timetable_size[f'timetable_old_size{college_number}']:
        timetable_old_size[f'timetable_old_size{college_number}'] = timetable_new_size
        file = requests.get(url)
        with open(f'media/sheduleXLSX/zamena{college_number}k.xlsx', 'wb') as file_xlsx:
            file_xlsx.write(file.content)
        await save_img_groups_to_file(f'media/sheduleXLSX/zamena{college_number}k.xlsx', college_number)
        await convert_BGC(college_number)
        redis_client.hdel("id_colleges_img", f"college_{college_number}")


async def check_shedule():
    while True:
        hour_biysk = datetime.now(TIME_ZONE).strftime('%H%M%S')
        if int(hour_biysk) in range(100000, 200000):
            logging.info("check shedule")
            [await comparison_size_bgc(i, timetable_old_size) for i in range(1, 5)]
            await asyncio.sleep(180)
        else:
            logging.info("check shedule - time > 20:00")
            await asyncio.sleep(600)
