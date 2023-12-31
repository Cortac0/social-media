from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(default="")

    def __str__(self):
        return f"<User {self.first_name} {self.last_name}>"
