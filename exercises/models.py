from django.db import models
from django.db.models import Sum
from django.utils import timezone


class Grade(models.Model):
    name = models.CharField(max_length=200)
    num_skills = models.IntegerField(default=0)
    num_exercises = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def count_num_skills(self):
        self.num_skills = self.skills.all().count()
        return self.num_skills

    def count_num_exercises(self):
        self.num_exercises = self.skill.all().aggreate(Sum('num_exercises'))
        return self.num_exercises


class Exercise(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=200)
    pub_date = models.DateTimeField(
        'published date',
        default=timezone.now()
    )

    def __unicode__(self):
        return self.question


class Skill(models.Model):
    grade = models.ForeignKey(Grade, related_name="skills")
    name = models.CharField(max_length=200)
    num_exercises = models.IntegerField(default=0)
    exercises = models.ManyToManyField(Exercise, blank=True)

    def __unicode__(self):
        return self.name

    def count_num_exercises(self):
        self.num_exercises = self.exercises.all().count()
        return self.num_exercises


class Exam(models.Model):
    grade = models.ForeignKey(Grade, related_name="exams")
    name = models.CharField(max_length=200)
    exercises = models.ManyToManyField(Exercise, blank=True)

    def __unicode__(self):
        return self.name
