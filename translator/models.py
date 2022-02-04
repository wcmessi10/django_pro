from django.db import models

# Create your models here.
class Translator(models.Model):
    before = models.TextField()
    after = models.TextField()

    def __str__(self):
        return f"{self.before}{self.after}"