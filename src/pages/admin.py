from django.contrib import admin
from .models import Student

# Register your models here.
class ModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'home_group']
    class Meta:
        model = Student


admin.site.register(Student, ModelAdmin)
