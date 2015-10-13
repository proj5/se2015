from django.contrib import admin

from exercises.models import Grade, Skill, Exercise


class ExerciseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Group', {'fields': ['skill']}),
        ('Content', {'fields': ['question', 'answer']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = (
        'question',
        'skill',
        'answer',
        'pub_date'
    )
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Grade)
admin.site.register(Skill)
admin.site.register(Exercise, ExerciseAdmin)
