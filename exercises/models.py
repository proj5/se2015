from django.db import models
from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import post_save


class Grade(models.Model):
    name = models.CharField(max_length=200)
    num_skills = models.IntegerField(default=0)
    num_exercises = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.name)

    def count_num_skills(self):
        self.num_skills = self.skills.all().count()
        return self.num_skills

    def count_num_exercises(self):
        self.num_exercises = self.skill.all().aggreate(Sum('num_exercises'))
        return self.num_exercises


class Skill(models.Model):
    grade = models.ForeignKey(Grade, related_name="skills")
    name = models.CharField(max_length=200)
    id_in_grade = models.IntegerField(default=1)
    num_exercises = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def count_num_exercises(self):
        self.num_exercises = self.exercises.all().count()
        return self.num_exercises


class Exercise(models.Model):
    skill = models.ForeignKey(
        Skill,
        default=None,
        null=True,
        blank=True,
        related_name='exercises'
    )
    question = models.TextField(max_length=1000)
    QUESTION_TYPES = (
        ('MC', 'multiple_choice'),
        ('SC', 'single_choice'),
        ('AN', 'answer')
    )
    question_type = models.CharField(
        max_length=2,
        choices=QUESTION_TYPES,
        default='AN'
    )
    image = models.ImageField(upload_to="static/img/", blank=True, null=True)
    answer = models.CharField(max_length=200)
    pub_date = models.DateTimeField(
        # 'published date',
        auto_now_add=True,
    )

    def __unicode__(self):
        return self.question


class PossibleAnswer(models.Model):
    exercise = models.ForeignKey(
        Exercise,
        default=None,
        null=True,
        blank=True,
        related_name='possible'
    )
    possible_answer = models.CharField(max_length=200)
    is_correct_answer = models.BooleanField(default=False)

    def __unicode__(self):
        return self.possible_answer


class Exam(models.Model):
    grade = models.ForeignKey(Grade, related_name="exams")
    name = models.CharField(max_length=200)
    exercises = models.ManyToManyField(Exercise, blank=True)
    num_exercises = models.IntegerField(default=10)
    time_limit = models.IntegerField(default=0)
    taken = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


@receiver(post_save, sender=Exercise)
def add_exercise(sender, **kwargs):
    if (kwargs.get('instance', True) and kwargs['created'] and
       not kwargs.get('raw', False)):
        kwargs['instance'].skill.num_exercises += 1
        kwargs['instance'].skill.grade.num_exercises += 1
        kwargs['instance'].skill.save()
        kwargs['instance'].skill.grade.save()


@receiver(post_save, sender=Skill)
def add_skill(sender, **kwargs):
    if (kwargs.get('instance', True) and kwargs['created'] and
       not kwargs.get('raw', False)):
        kwargs['instance'].grade.num_skills += 1
        kwargs['instance'].grade.save()
