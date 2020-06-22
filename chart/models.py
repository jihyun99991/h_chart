# chart/modles.py
from django.db import models

class Passenger(models.Model):  # 승객 데이터를 저장할 테이블
    # 성별 상수 정의
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (  # 튜플, 값을 바꿀 수 없는 리스트.
        (MALE, 'male'), # 이것도 튜플, 'M'이 들어오면 'male'로 처리하라는 상수
        (FEMALE, 'female')
    )

    # 승선_항구 상수 정의
    CHERBOURG = 'C'  # 항구 이름
    QUEENSTOWN = 'Q'
    SOUTHAMPTON = 'S'
    PORT_CHOICES = (
        (CHERBOURG, 'Cherbourg'),
        (QUEENSTOWN, 'Queenstown'),
        (SOUTHAMPTON, 'Southampton'),
    )

    name = models.CharField(max_length=100, blank=True)                 # 이름
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)           # 성별
    survived = models.BooleanField()                                    # 생존_여부
    age = models.FloatField(null=True)                                  # 연령 (대부분의 연령은 정수이지만, 아기의 경우 개월수로)
    ticket_class = models.PositiveSmallIntegerField()                   # 티켓_등급
    embarked = models.CharField(max_length=1, choices=PORT_CHOICES)     # 승선_항구(배가 여러 항구를 들릴 때마다 탑승한 승객)

    def __str__(self):
        return self.name