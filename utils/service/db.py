from .images_generate import create_img_shedule_each_group
from database import models


async def save_img_groups_to_file(url: str, college_building: int) -> None:
    """Save file *.jpg and enters data into the database"""
    group_list_data = create_img_shedule_each_group(url, college_building)
    ob = []
    for group in group_list_data:
        name = group['name']
        img_shedule = group['img_shedule']
        img_shedule.save(f"media/group_img/{name}.jpg")

        college_building = group['college_building']
        ob.append(models.GroupsImg(name=name, url=f"media/group_img/{name}.jpg", college_building=college_building))
    await models.GroupsImg().bulk_create(objects=ob, on_conflict=['name'], update_fields=['url'])
