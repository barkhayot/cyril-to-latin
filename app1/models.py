from django.db import models

# Create your models here.

class Word(models.Model):
    word        = models.CharField(max_length=100)
    over_word   = models.CharField(max_length=100)

    def __str__(self):
        return self.word