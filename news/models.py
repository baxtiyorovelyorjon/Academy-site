from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()
    image = models.ImageField(upload_to='Media/kurs_img')

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Media/teach_img')
    teaching_course = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.full_name

class Application(models.Model):
    client_name = models.CharField(max_length=100)
    client_last_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    client_phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name
