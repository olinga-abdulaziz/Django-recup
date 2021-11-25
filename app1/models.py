from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    dorm=models.CharField(max_length=200)
    home=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
 
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'pk': self.pk})