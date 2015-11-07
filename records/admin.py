from django.contrib import admin
from records.models import GradeRecord, ExerciseRecord, SkillRecord, ExamRecord

# Register your models here.

admin.site.register(GradeRecord)
admin.site.register(ExerciseRecord)
admin.site.register(SkillRecord)
admin.site.register(ExamRecord)
