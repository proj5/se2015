from django.contrib import admin
from records.models import ExerciseRecord, ExamRecord

# Register your models here.

admin.site.register(ExerciseRecord)
admin.site.register(ExamRecord)
