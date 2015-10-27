from rest_framework import serializers

from exercises.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'question', 'answer', 'pub_date')
        read_only_fields = ('id', 'pub_date')
