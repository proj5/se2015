from django.contrib import admin

from exercises.models import Grade, Skill, Exercise, Exam, PossibleAnswer


class PossibleAnswersInline(admin.TabularInline):
    model = PossibleAnswer
    extra = 0


class ExerciseAdmin(admin.ModelAdmin):
    readonly_fields = ['pub_date']
    fieldsets = [
        ('Content', {'fields': ['question', 'question_type', 'image',
                                'answer', 'skill']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = (
        'id',
        'question',
        'question_type',
        'image',
        'answer',
        'skill',
        'pub_date'
    )
    list_filter = ['pub_date']
    search_fields = ['question']
    inlines = [
        PossibleAnswersInline
    ]


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'grade',
        'id_in_grade',
        'num_exercises',
    )


class GradeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'num_skills',
        'num_exercises',
    )


class ExerciseInline(admin.StackedInline):
    model = Exam.exercises.through
    extra = 0


class ExamAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'grade',
        'name',
        'num_exercises',
        'time_limit'
    )
    inlines = [
        ExerciseInline
    ]
    exclude = ('exercises', )


admin.site.register(Grade, GradeAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(PossibleAnswer)
