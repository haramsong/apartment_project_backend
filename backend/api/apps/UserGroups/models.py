from django.db import models


class UserGroups(models.Model):
    idx = models.AutoField(db_column='IDX', db_comment='인덱스 값', primary_key=True)
    name = models.CharField(db_column='NAME', max_length=30, db_comment='그룹명')
    content = models.CharField(db_column='CONTENT', max_length=300, db_comment='그룹 소개')
    public_flag = models.CharField(db_column='PUBLIC_FLAG', max_length=1, db_comment='공개 여부 flag')
    danji_code = models.IntegerField(db_column='DANJI_CODE', db_comment='단지 코드')
    created_at = models.DateTimeField(db_column='CREATED_AT', db_comment='생성일')
    created_by = models.IntegerField(db_column='CREATED_BY', db_comment='생성자')
    updated_at = models.DateTimeField(db_column='UPDATED_AT', db_comment='수정일')
    updated_by = models.IntegerField(db_column='UPDATED_BY', db_comment='수정자')

    class Meta:
        managed = False
        db_table = 'user_groups'
        db_table_comment = '주민 그룹'