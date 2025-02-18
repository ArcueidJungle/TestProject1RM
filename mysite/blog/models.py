from django.db import models

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    content = models.TextField("Содержание")  # ← Это поле должно быть!
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title