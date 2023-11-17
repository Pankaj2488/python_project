from django.db import models

class Text(models.Model):
    content = models.TextField()
    word_count = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Text {self.id}'
