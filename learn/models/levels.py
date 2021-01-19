from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=20)


    @staticmethod
    def get_all_level():
        return Level.objects.all()


    def __str__(self):
        return self.name