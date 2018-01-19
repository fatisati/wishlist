from django.db import models

class user(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class wish(models.Model):
    description = models.CharField(max_length=200)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + ":" + self.description



