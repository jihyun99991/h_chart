# chart/migrations/0002_auto_popuate.py
"""
DB 현행화 작업이 실행될 때, csv 파일 자료를 DB에 자동적으로 적재한다.
"""
import csv
import os # 경로를 따지기 위해 os 불러옴
from django.db import migrations
from django.conf import settings

# csv 파일의 해당 열 번호를 상수로 정의
TICKET_CLASS = 0  # 승차권 등급
SURVIVED = 1      # 생존 여부
NAME = 2          # 이름
SEX = 3           # 성별
AGE = 4           # 나이
EMBARKED = 10     # 탑승지

def add_passengers(apps, schema_editor):
    Passenger = apps.get_model('chart', 'Passenger')  # (app_label, model_name)
    #apps.get_model()함수를 통해 passenger 모델을 가져옴, 차트앱으로부터 passenger 모델을 가져온다는 의미.
    csv_file = os.path.join(settings.BASE_DIR, 'titanic.csv')
    with open(csv_file) as dataset:                   # 파일 객체 dataset
        # csv_file을 dataset으로 연다
        reader = csv.reader(dataset)                    # 파일 객체 dataset에 대한 판독기 획득
        # csv.reader은 한줄 읽기, dataset으로부터 한줄을 읽는 판독기를 만듬
        next(reader)  # ignore first row (headers)      # __next__() 호출 때마다 한 라인 판독
        # next()는 한줄을 건너뛴다는 뜻. 첫줄은 열제목이기 때문에
        for entry in reader:                            # 판독기에 대하여 반복 처리
            # 한번 반복될 때마다 entry에 들어옴
            Passenger.objects.create(                       # DB 행 생성
                # 모델 객체로부터 객체를 만든다
                name=entry[NAME],
                sex='M' if entry[SEX] == 'male' else 'F',
                survived=bool(int(entry[SURVIVED])),        # int()로 변환하고, 다시 bool()로 변환
                age=float(entry[AGE]) if entry[AGE] else 0.0,
                # 값이 존재하면 float값으로, 존재하지 않으면 0.0으로 집어 넣어라
                ticket_class=int(entry[TICKET_CLASS]),      # int()로 변환
                # entry에서 불러오면 문자로 들어옴. 문자'1','2','3' 이런 형식.
                embarked=entry[EMBARKED],
            )

class Migration(migrations.Migration):
    dependencies = [                            # 선행 관계
        ('chart', '0001_initial'),         # app_label, preceding migration file
    ]
    # 앞에 선행된 작업들은 0001~ 파일에 저장되어 있음.
    # 이 이후에 우리 작업이 진행되는 것임. 우리가 할 작업은 파이썬 add_passengers 함수를 run시키면, csv파일에서 데이터가 들어감
    operations = [                              # 작업
        migrations.RunPython(add_passengers),   # add_passengers 함수를 호출
    ]

