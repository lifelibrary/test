from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
    original_price = models.IntegerField()
    sale_price = models.IntegerField()
    # 위에서의 name을 통해 뛰어쓰기 없는 url에 추가 가능한 형태로 바꿔줌
    slug = models.SlugField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

