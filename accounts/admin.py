from django.contrib import admin
from .models import InstructorProfile

# Register your models here.

@admin.register(InstructorProfile)
class InstructorPorfileAdmin(admin.ModelAdmin):
    pass