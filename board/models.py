from django.db import models
from acc.models import User
# Create your models here.

class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writer")
    #작성자는 하나의 계정
    content = models.TextField()
    likey = models.ManyToManyField(User, blank=True, related_name="likey")
    #같은 외부 테이블을 참조하는 레코드가 여러개 있다면 related_name으로 이름 따로 지정해야함
    pubdate = models.DateField()

    def __str__(self):
        return f"[{self.writer.username}] {self.subject}"

    def summary(self):
        if len(self.content)>30:
            return f"{self.content[:30]}   ..."
        return self.content

class Reply(models.Model):
    b = models.ForeignKey(Board, on_delete=models.CASCADE)
    #Board의 자식 테이블 참조하고 같은 앱이라면 참조하는 앱이 위에 있어야함
    replyer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    pubdate = models.DateTimeField()
    
    def __str__(self):
        return f"{self.b}-{self.replyer.username}"