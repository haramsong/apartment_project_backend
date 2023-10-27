from django.db import models


class Danjis(models.Model):
    code = models.CharField(
        db_column='CODE',
        max_length=5,
        db_comment='단지 코드',
        primary_key=True,
    )
    name = models.CharField(
        db_column='NAME',
        max_length=30,
        db_comment='단지명',
    )
    tel = models.CharField(
        db_column='TEL',
        max_length=11,
        db_comment='전화번호',
    )
    address = models.CharField(
        db_column='ADDRESS',
        max_length=300,
        db_comment='주소',
    )
    greeting = models.CharField(
        db_column='GREETING',
        max_length=300,
        db_comment='단지 소개',
    )
    profile_img = models.BinaryField(
        db_column='PROFILE_IMG',
        blank=True,
        null=True,
        db_comment='단지 썸네일 이미지',
    )

    class Meta:
        managed = False
        db_table = 'danjis'
        db_table_comment = '단지'

        