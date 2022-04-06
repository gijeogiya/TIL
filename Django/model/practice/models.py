from django.db import models


# models.Model을 상속받은 경우,
# 클래스는, objects 라는 Manager를 두게 됨
# 인스턴스는, 바로 실행가능한 메서드(.save())가 존재
# 클래스 == 테이블 / 인스턴스 == 레코드

class Student(models.Model):
    # 컬럼(필드)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    is_married = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}) {self.name}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}: {self.title}'


"""
Table 생성/수정 반영
1. model class 작성(수정) => 무조건 2번으로
2. $ python manage.py makemigrations [app_name]
3. $ python manage.py migrate [app_name]

Data CRUD

Create(생성)
s1 = Student()
s1.name = 'a'
s1.age = 123
s1.major = 'CS'
s1.save()  # <= db에 반영


Read(조회)
1. 전체 목록
Stduent.objects.all()  # return queryset 

2. 단일 조회
Student.objects.get(pk=1) # return object


Update(수정)
s = Student.objects.get(pk=4)
s.name = '김싸피'
s.is_married = True
s.save()


Delete(삭제)
s = Student.objects.get(pk=4)
s.delete()
"""