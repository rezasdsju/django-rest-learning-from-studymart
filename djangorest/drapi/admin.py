from django.contrib import admin
from . models import Aiquest

# Register your models here.

"""class AiquestAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name', 'course_name', 'course_duration', 'seat']
admin.site.register(Aiquest, AiquestAdmin)"""


@admin.register(Aiquest)
class AiquestAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name', 'course_name', 'course_duration', 'seat']
