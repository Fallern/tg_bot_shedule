from service_parse import split_group
from PIL import Image, ImageDraw, ImageFont


def create_img_shedule_each_group(url: str, college_building: int) -> list[dict[str, Image]]:
    """Create list img - objects for further processing them"""
    groups_img_list = []
    font = ImageFont.truetype("arial.ttf", size=20)
    groups = split_group(url)  # path to Excel  file
    for group in groups:
        count_row = len(group) - 1
        img = Image.new('L', (350, 35 * count_row), 'white')
        idraw = ImageDraw.Draw(img)
        for i, pos in enumerate(group):
            left = pos['left']
            right = pos['right']
            idraw.text((125, 35 * i), str(right), font=font)
            idraw.text((25, 35 * i), str(left), font=font)
        idraw.rectangle((0, 0, 349, 35 * count_row - 1))
        group_img = {
            "name": group[0]['right'],
            "img_shedule": img,
            "college_building": college_building,
        }
        groups_img_list.append(group_img)
    return groups_img_list
