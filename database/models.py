from tortoise import fields
from tortoise.models import Model


class GroupsImg(Model):
    name = fields.CharField(max_length=50, pk=True)
    url = fields.CharField(max_length=60)
    college_building = fields.IntField()

    class Meta:
        table = "groups_img"

    def __str__(self):
        return self.name


class UserTg(Model):
    id = fields.CharField(max_length=200, pk=True)
    name = fields.CharField(max_length=60)
    college_building = fields.IntField()
    group: fields.ForeignKeyNullableRelation = fields.ForeignKeyField("models.GroupsImg", null=True)

    class Meta:
        table = "users_tg"

    def __str__(self):
        return self.id
