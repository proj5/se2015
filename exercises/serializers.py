from rest_framework import serializers

from exercises.models import Exercise
from exercises.models import Skill
from exercises.models import Grade


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ('id', 'name')
        read_only_fields = ('id', 'name')


class SkillSerializer(serializers.ModelSerializer):

    grade = GradeSerializer()

    class Meta:
        model = Skill
        fields = ('name', 'id_in_grade', 'grade')
        read_only_fields = ('name', 'id_in_grade')


class ExerciseSerializer(serializers.ModelSerializer):

    skill = SkillSerializer()

    class Meta:
        model = Exercise
        fields = ('id', 'question', 'answer', 'pub_date', 'skill')
        read_only_fields = ('id', 'pub_date')


class ExerciseAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ('id', 'answer')
        read_only_fields = ('id', 'answer')
