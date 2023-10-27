from django.db import models


class Attachs(models.Model):
    idx = models.AutoField(
        db_column='IDX',
        db_comment='인덱스 값',
        primary_key=True,
    )
    reg_date = models.DateTimeField(
        db_column='REG_DATE',
        db_comment='등록일',
    )
    upload_path = models.CharField(
        db_column='UPLOAD_PATH',
        max_length=200,
        db_comment='파일 경로',
    )
    file_name = models.CharField(
        db_column='FILE_NAME',
        max_length=200,
        db_comment='파일 이름',
    )
    file_type = models.CharField(
        db_column='FILE_TYPE',
        max_length=1,
        db_comment='이미지 파일 여부[ 0(이미지 파일), 1(이미지 파일X) ]',
    )
    content_type = models.CharField(
        db_column='CONTENT_TYPE',
        max_length=1,
        db_comment='게시물 타입 [ B(BOARD_CONTENTS), C(COMPLAINT_CONTENTS), S(SHAREPLACE_CONTENTS) ]',
    )
    content_idx = models.IntegerField(
        db_column='CONTENT_IDX',
        db_comment='게시물 IDX',
    )

    class Meta:
        managed = False
        db_table = 'attachs'
        db_table_comment = '첨부파일'
