from rest_framework import serializers

from exercises.models import Exercise
from exercises.models import Skill


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'question', 'answer', 'pub_date')
        read_only_fields = ('id', 'pub_date')


class ExerciseAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'answer', )


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'id_in_grade')
        read_only_fields = ('name', 'id_in_grade')
