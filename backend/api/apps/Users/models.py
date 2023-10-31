from django.db import models
from ..Danjis.models import Danjis
import os


def get_image_path(instance, filename):
    return os.path.join(str(instance.danji_code), 'users', str(instance.idx) + '_' + filename)


class Users(models.Model):
    idx = models.AutoField(
        db_column='IDX',
        db_comment='인덱스 값',
        primary_key=True,
    )
    user_id = models.CharField(
        db_column='USER_ID',
        max_length=15,
        db_comment='아이디',
    )
    password = models.CharField(
        db_column='PASSWORD',
        max_length=200,
        db_comment='비밀번호',
    )
    nickname = models.CharField(
        db_column='NICKNAME',
        max_length=15,
        db_comment='닉네임',
    )
    name = models.CharField(
        db_column='NAME',
        max_length=12,
        db_comment='이름',
    )
    birthday = models.CharField(
        db_column='BIRTHDAY',
        max_length=10,
        db_comment='생년월일',
    )
    email = models.CharField(
        db_column='EMAIL',
        max_length=50,
        db_comment='이메일',
    )
    phone = models.CharField(
        db_column='PHONE',
        max_length=11,
        db_comment='휴대폰 번호',
    )
    dong = models.CharField(
        db_column='DONG',
        max_length=4,
        blank=True,
        null=True,
        db_comment='동',
    )
    ho = models.CharField(
        db_column='HO',
        max_length=4,
        blank=True,
        null=True,
        db_comment='호',
    )
    danji_code = models.ForeignKey(
        Danjis,
        models.DO_NOTHING,
        db_column='DANJI_CODE',
        db_comment='단지 CODE'
    )
    type = models.CharField(
        db_column='TYPE',
        max_length=1,
        db_comment='사용자 상태',
    )
    status_flag = models.CharField(
        db_column='STATUS_FLAG',
        max_length=1,
        db_comment='사용자 상태',
    )
    profile_img = models.ImageField(
        db_column='PROFILE_IMG',
        blank=True,
        null=True,
        db_comment='사용자 썸네일 이미지',
        upload_to=get_image_path,
    )
    created_at = models.DateTimeField(
        db_column='CREATED_AT',
        db_comment='생성일',
    )
    updated_at = models.DateTimeField(
        db_column='UPDATED_AT',
        db_comment='수정일',
    )

    class Meta:
        managed = False
        db_table = 'users'
        db_table_comment = '유저 정보'

