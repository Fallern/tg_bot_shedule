import logging
import os
import asyncio

import cloudconvert

from data.config import TOKEN
from loader import redis_client

cloudconvert.configure(api_key=TOKEN,
                       sandbox=False)


# создание работы для конвертации одного формата в другой с использование API и преобразуем полученный код с сайта
async def convert_BGC(number_college: int):
    filename = f'zamena{number_college}k.xlsx'
    path = f'media/sheduleXLSX/{filename}'
    data = cloudconvert.Job.create(payload={
        "tasks": {
            'upload_shedule_xlsx': {
                'operation': 'import/upload'
            },
            'xlsx_to_png': {
                'operation': 'convert',
                'input': 'upload_shedule_xlsx',
                'output_format': 'png',
                'filename': f'download_{filename[:-5]}.png'  # удаляем xlsx расширение с помощью среза
            },
            'export_png': {
                'operation': 'export/url',
                'input': 'xlsx_to_png'
            }
        }
    })
    upload_task_id = data['tasks'][0]['id']
    upload_task = cloudconvert.Task.find(id=upload_task_id)
    task = cloudconvert.Task.upload(file_name=path, task=upload_task)

    exported_task_id = data.get('tasks')[2].get('id')
    print('Tasks start')
    await asyncio.sleep(10)  # Add async  func, put all the tasks in the queue
    res = cloudconvert.Task.wait(id=exported_task_id)  # Wait for job completion
    file = res.get("result").get("files")[0]
    filename = file['filename']
    file_url = file['url']
    cloudconvert.download(filename=filename, url=file_url)
    os.replace(filename, f'media/college_building_img/download_zamena{number_college}.png')


async def start_load_all_files_png():
    redis_client.delete("id_colleges_img")
    logging.info(f'delete key (id_colleges_img)')
    await asyncio.gather(
        *[convert_BGC(i) for i in range(1, 5)]
    )
