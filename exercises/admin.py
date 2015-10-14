from django.contrib import admin

from exercises.models import Grade, Skill, Exercise, Exam


class ExerciseAdmin(admin.ModelAdmin):
    readonly_fields = ['pub_date']
    fieldsets = [
        ('Content', {'fields': ['question', 'answer']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = (
        'question',
        'answer',
        'pub_date'
    )
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Grade)
admin.site.register(Skill)
admin.site.register(Exam)
admin.site.register(Exercise, ExerciseAdmin)
