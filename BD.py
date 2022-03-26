import config
import psycopg2
from psycopg2 import extras
from service import create_img_shedule_each_group

conn = psycopg2.connect(dbname=config.DB_NAME,
                        port=config.PORT,
                        host=config.HOST,
                        user=config.USER,
                        password=config.PASSWORD)


def get_all_group() -> list:
    with conn.cursor() as cursor:
        cursor.execute("""
        SELECT name FROM groups_img
        """)
        groups = cursor.fetchall()
    return groups


def get_group(name_group: str) -> dict:
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("""
            SELECT * FROM groups_img
            WHERE name = %s
            """, (name_group,))
            group = cursor.fetchone()
    return dict(group)


def save_img_groups_to_file(url: str, college_building: int) -> None:
    """Save file *.jpg and enters data into the database"""
    group_list_data = create_img_shedule_each_group(url, college_building)
    with conn:
        for group in group_list_data:
            name = group['name']
            img_shedule = group['img_shedule']
            college_building = group['college_building']
            url = f"group_img/{name}.jpg"
            with conn.cursor() as cursor:
                cursor.execute("""
                INSERT INTO groups_img (name, url, college_building)
                VALUES (%s, %s, %s)
                ON CONFLICT (name) DO NOTHING
                """, (name, url, college_building,))
            img_shedule.save(f"group_img/{name}.jpg")
