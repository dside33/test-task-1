from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=100)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TestSet(models.Model):
    set_name = models.CharField(max_length=100)
    test = models.ManyToManyField(Test)