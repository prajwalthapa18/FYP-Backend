from django.db import models

class DetectedUser(models.Model):
    user_id = models.IntegerField(unique=True)
    gender = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User {self.user_id} - {self.gender}'

class GenderCount(models.Model):
    gender = models.CharField(max_length=10, unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.gender}: {self.count}'
