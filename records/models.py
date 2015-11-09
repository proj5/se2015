from django.db import models
from exercises.models import Grade, Exercise, Skill, Exam
from users.models import UserAccount

# Create your models here.


class ExamRecord(models.Model):
    exam = models.ForeignKey(Exam)
    user = models.ForeignKey(UserAccount)

    score = models.IntegerField(default=0)
    done_time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.exam.__unicode__() + ' ' + self.user.__unicode__()


class ExerciseRecord(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='records')
    exam_record = models.ForeignKey(
        ExamRecord,
        default=None,
        null=True,
        blank=True,
        related_name='exercise_records'
    )
    user = models.ForeignKey(UserAccount, related_name='exercise_records')

    answer = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    done_time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.exercise.__unicode__() + ' ' + self.answer
