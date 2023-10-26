from django.contrib.postgres.fields import ArrayField
from django.db import models


class Attachs(models.Model):
    idx = models.AutoField(db_column='IDX', db_comment='인덱스 값', primary_key=True)  
    reg_date = models.DateTimeField(db_column='REG_DATE', db_comment='등록일')  
    upload_path = models.CharField(db_column='UPLOAD_PATH', max_length=200, db_comment='파일 경로')  
    file_name = models.CharField(db_column='FILE_NAME', max_length=200, db_comment='파일 이름')  
    file_type = models.CharField(db_column='FILE_TYPE', max_length=1, db_comment='이미지 파일 여부[ 0(이미지 파일), 1(이미지 파일X) ]')
    content_type = models.CharField(db_column='CONTENT_TYPE', max_length=1, db_comment='게시물 타입 [ B(BOARD_CONTENTS), C(COMPLAINT_CONTENTS), S(SHAREPLACE_CONTENTS) ]')
    content_idx = models.IntegerField(db_column='CONTENT_IDX', db_comment='게시물 IDX')

    class Meta:
        managed = False
        db_table = 'attachs'
        db_table_comment = '첨부파일'


class BoardContents(models.Model):
    idx = models.AutoField(db_column='IDX', db_comment='인덱스 값', primary_key=True)  
    title = models.CharField(db_column='TITLE', max_length=30, db_comment='제목')  
    content = models.TextField(db_column='CONTENT', db_comment='본문 내용')  
    usergroup_idx = models.IntegerField(db_column='USERGROUP_IDX', db_comment='주민 그룹 IDX')  
    cnt = models.IntegerField(db_column='CNT', db_comment='조회수')  
    attach = ArrayField(models.IntegerField(db_column='ATTACH', blank=True, null=True, db_comment='첨부파일 idx'))  
    blind_flag = models.CharField(db_column='BLIND_FLAG', max_length=1, db_comment='블라인드 flag')  
    like_cnt = models.IntegerField(db_column='LIKE_CNT', db_comment='좋아요 수')  
    created_at = models.DateTimeField(db_column='CREATED_AT', db_comment='생성일')  
    updated_at = models.DateTimeField(db_column='UPDATED_AT', db_comment='수정일')  
    user_idx = models.IntegerField(db_column='USER_IDX', db_comment='주민 IDX')  

    class Meta:
        managed = False
        db_table = 'board_contents'
        db_table_comment = '주민게시판'


class Danjis(models.Model):
    code = models.CharField(db_column='CODE', max_length=5, db_comment='단지 코드', primary_key=True)  
    name = models.CharField(db_column='NAME', max_length=30, db_comment='단지명')  
    tel = models.CharField(db_column='TEL', max_length=11, db_comment='전화번호')  
    address = models.CharField(db_column='ADDRESS', max_length=300, db_comment='주소')  
    greeting = models.CharField(db_column='GREETING', max_length=300, db_comment='단지 소개')  
    profile_img = models.BinaryField(db_column='PROFILE_IMG', blank=True, null=True, db_comment='단지 썸네일 이미지')  

    class Meta:
        managed = False
        db_table = 'danjis'
        db_table_comment = '단지'


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

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
