from django.contrib import admin

# Register your models here.
from news.models import Course, Teacher, Application

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Application)