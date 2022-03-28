import os
import cloudconvert
import urllib.request
import asyncio
from config import CLOUDCONVERT_TOKEN

cloudconvert.configure(api_key=CLOUDCONVERT_TOKEN,
                       sandbox=True)


# создание работы для конвертации одного формата в другой с использование API и преобразуем полученный код с сайта
async def convert_BGC(number_college):
    filename = f'zamena{number_college}k.xlsx'
    path = f'sheduleXLSX/{filename}'
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
    await asyncio.sleep(5)  # Add async  func, put all the tasks in the queue
    res = cloudconvert.Task.wait(id=exported_task_id)  # Wait for job completion
    file = res.get("result").get("files")[0]
    filename = file['filename']
    file_url = file['url']
    cloudconvert.download(filename=filename, url=file_url)
    os.replace(filename, f'college_building_img/download_zamena{number_college}.png')
