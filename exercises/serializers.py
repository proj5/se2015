from rest_framework import serializers

from exercises.models import Exercise
from exercises.models import Skill
from exercises.models import Grade
from exercises.models import Exam
from exercises.models import PossibleAnswer
from records.models import ExamRecord


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


class PossibleAnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = PossibleAnswer
        fields = ('possible_answer',)
        read_only_fields = ('possible_answer',)


class ExerciseSerializer(serializers.ModelSerializer):

    skill = SkillSerializer()

    possible = PossibleAnswersSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = (
            'id',
            'question',
            'question_type',
            'possible',
            'image',
            'pub_date',
            'skill'
        )
        read_only_fields = ('id', 'pub_date')


class ExerciseAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ('id', 'answer')
        read_only_fields = ('id', 'answer')


class ExamListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = ('id', 'grade', 'name')
        read_only_fields = ('id', 'grade', 'name')


class ExamDetailSerializer(serializers.ModelSerializer):

    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Exam
        fields = (
            'id',
            'grade',
            'name',
            'time_limit',
            'num_exercises',
            'exercises'
        )
        read_only_fields = (
            'id',
            'grade',
            'name',
            'time_limit',
            'num_exercises',
            'exercises'
        )


class ExamAnswerSerializer(serializers.ModelSerializer):

    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Exam
        fields = ('id', 'exercises')
        read_only_fields = ('id',)


class ExamRecordSerializer(serializers.ModelSerializer):

    exercises = ExerciseAnswerSerializer(many=True)

    class Meta:
        model = ExamRecord
        fields = ('id', 'exercises', 'done_time')
        read_only_fields = ('id', )
