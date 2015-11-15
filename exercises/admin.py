from django.contrib import admin

from exercises.models import Grade, Skill, Exercise, Exam


class ExerciseAdmin(admin.ModelAdmin):
    readonly_fields = ['pub_date']
    fieldsets = [
        ('Content', {'fields': ['question', 'answer', 'skill']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = (
        'question',
        'answer',
        'skill',
        'pub_date'
    )
    list_filter = ['pub_date']
    search_fields = ['question']


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'grade',
        'num_exercises',
    )


class GradeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'num_skills',
        'num_exercises',
    )


class ExamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'grade'
    )


admin.site.register(Grade, GradeAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Exercise, ExerciseAdmin)
