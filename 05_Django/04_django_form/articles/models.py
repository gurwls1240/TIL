from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    #image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 원래는 새로운 필드를 추가하고 나면
    # makemigrations를 할 때, 어떤 값을 넣을 것인지
    # Django가 물어봄
    # 기본 적으로 blank = False 이기 때문
    # blamk = True : '빈 문자열'이 들어가도 됨
    # 객체 표시 형식 수정

    def __str__(self):
        return f'[{self.pk}] {self.title}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level에서 메타데이터 옵션 설정 -> 정렬 기능
    class Meta:
        ordering = ('-pk', )

    # 객체 표현 방식
    def __str__(self):
        return self.content