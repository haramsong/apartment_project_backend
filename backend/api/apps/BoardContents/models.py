from django.contrib.postgres.fields import ArrayField
from django.db import models


class BoardContents(models.Model):
    idx = models.AutoField(
        db_column='IDX',
        db_comment='인덱스 값',
        primary_key=True,
    )
    title = models.CharField(
        db_column='TITLE',
        max_length=30,
        db_comment='제목',
    )
    content = models.TextField(
        db_column='CONTENT',
        db_comment='본문 내용',
    )
    usergroup_idx = models.IntegerField(
        db_column='USERGROUP_IDX',
        db_comment='주민 그룹 IDX',
    )
    cnt = models.IntegerField(
        db_column='CNT',
        db_comment='조회수',
    )
    attach = ArrayField(
        models.IntegerField(),
        db_column='ATTACH',
        blank=True,
        null=True,
        db_comment='첨부파일 idx',
    )
    blind_flag = models.CharField(
        db_column='BLIND_FLAG',
        max_length=1,
        db_comment='블라인드 flag',
    )
    like_cnt = models.IntegerField(
        db_column='LIKE_CNT',
        db_comment='좋아요 수',
    )
    created_at = models.DateTimeField(
        db_column='CREATED_AT',
        db_comment='생성일',
    )
    updated_at = models.DateTimeField(
        db_column='UPDATED_AT',
        db_comment='수정일',
    )
    user_idx = models.IntegerField(
        db_column='USER_IDX',
        db_comment='주민 IDX',
    )

    class Meta:
        managed = False
        db_table = 'board_contents'
        db_table_comment = '주민게시판'
        