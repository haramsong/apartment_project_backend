# 주민 커뮤니티 프로젝트 API 구성

**구성** : Django, PostgreSQL 

### 환경 설정

1. Python 3.9 version 설치
2. Terminal 실행 후, python3 -m pip install --user -U viretualenv 입력
3. Git Terminal에서, git clone https://github.com/haramsong/apartment_project_backend.git 입력
4. Clone한 디렉토리로 이동 후, Terminal  에서, cd backend 입력
5. Terminal 실행 후, python -m venv venv 입력
6. 이어서 venv/scripts/activate.bat 입력
7. 이어서 pip install -r requirements.txt 입력
8. DB 연결 후, .env(자신에게 맞는 파일 생성)에 DB 정보 입력
9. Terminal에 python manage.py makemigrations , python manage.py migrate 입력 (model 동기화)
10. python manage.py runserver 입력 후 브라우저에 localhost:8000 입력
11. Django Rest Framework 뜨면 성공.