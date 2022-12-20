from django.contrib import admin
from .models import Course, Comment, Sector, Episode, CourseSection


admin.site.register(Course)
admin.site.register(Sector)
admin.site.register(Episode)
admin.site.register(CourseSection)
admin.site.register(Comment)
# Register your models here.
