from rest_framework import serializers

from records.models import ExamRecord, ExerciseRecord, UserAnswerRecord
from users.serializers import UserAccountSerializer
from exercises.serializers import ExerciseSerializer


class UserAnswerRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswerRecord
        fields = ('answer',)
        read_only_fields = ('answer',)


class ExerciseRecordSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()
    user = UserAccountSerializer()

    class Meta:
        model = ExerciseRecord
        fields = ('exercise', 'user', 'score')
        read_only_fields = ('exercise', 'user')


class ExerciseRecordNoUserSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()
    answer = UserAnswerRecordSerializer(many=True)

    class Meta:
        model = ExerciseRecord
        fields = ('exercise', 'answer', 'score')
        read_only_fields = ('exercise', 'score')


class ExamRecordSerializer(serializers.ModelSerializer):
    user = UserAccountSerializer()

    class Meta:
        model = ExamRecord
        fields = ('user', 'score', 'done_time')
        read_only_fields = ('user', 'score')


class ExamRecordOneUserSerializer(serializers.ModelSerializer):
    user = UserAccountSerializer()
    exercise_records = ExerciseRecordNoUserSerializer(many=True)

    class Meta:
        model = ExamRecord
        fields = ('user', 'exercise_records', 'score', 'done_time')
        read_only_fields = ('user', 'score', 'done_time')
