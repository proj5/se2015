from rest_framework import permissions, views
from rest_framework.response import Response

from exercises.models import Exercise, Skill, Grade, Exam
from exercises.serializers import ExerciseSerializer, ExerciseAnswerSerializer

from records.models import ExamRecord, ExerciseRecord, UserAnswerRecord
from exercises.serializers import SkillSerializer, GradeSerializer
from exercises.serializers import ExamListSerializer, ExamDetailSerializer
from exercises.serializers import ExamRecordSerializer

from rest_framework import status

from random import randint
import json
import re


class GradeView(views.APIView):

    def get_permissions(self):
        if self.request.method in 'GET':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), )

    def get(self, request, format=None):
        grades = Grade.objects.all()

        serializer = GradeSerializer(grades, many=True)

        return Response(serializer.data)


class SkillView(views.APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), )

    def get(self, request, grade_id, format=None):
        skills = Skill.objects.filter(grade__id=grade_id)

        serializer = SkillSerializer(skills, many=True)

        return Response(serializer.data)


class ExamListView(views.APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), )

    def get(self, request, grade_id, format=None):
        exam = Exam.objects.filter(grade__id=grade_id).all()
        serializer = ExamListSerializer(exam, many=True)
        return Response(serializer.data)


class ExamDetailView(views.APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), )

    def get(self, request, exam_id, format=None):
        exam = Exam.objects.get(id=exam_id)
        serializer = ExamDetailSerializer(exam)
        return Response(serializer.data)

    def check_correct_answer(self, _exercise, exercise):
        if exercise.question_type == 'AN':
            if _exercise.get('answer') == exercise.answer:
                return True
            else:
                return False
        else:
            if (exercise.question_type == 'SC' or
               exercise.question_type == 'MC'):
                # Check if the size of two lists are the same
                count1 = 0
                for answer in exercise.possible.all():
                    if answer.is_correct_answer:
                        count1 += 1
                if isinstance(_exercise.get('answer'), basestring):
                    count2 = 1
                else:
                    count2 = 0
                    for answer in _exercise.get('answer'):
                        count2 += 1
                if not count1 == count2:
                    return False
                # Check if two lists are equivalent
                for answer in exercise.possible.all():
                    if answer.is_correct_answer:
                        found = False
                        if isinstance(_exercise.get('answer'), basestring):
                            if (_exercise.get('answer') ==
                               answer.possible_answer):
                                found = True
                        else:
                            for _answer in _exercise.get('answer'):
                                if _answer == answer.possible_answer:
                                    found = True
                                    break
                        if not found:
                            return False
                return True
            return False

    def post(self, request, exam_id, format=None):
        exam = Exam.objects.get(id=exam_id)
        score = 0
        serializer = ExamRecordSerializer(exam, data=request.data)
        if serializer.is_valid():
            for exercise in exam.exercises.all():
                for s in request.data.getlist('exercises'):
                    json_object = re.sub('\'', '\"', s)
                    _exercise = json.loads(json_object)
                    if _exercise.get('id') == exercise.id:
                        if self.check_correct_answer(_exercise,
                           exercise):
                            score += 1
                        else:
                            score += 0
            # Save exam record
            record = ExamRecord(
                exam=exam,
                user=request.user.profile,
                done_time=request.data.get('done_time'),
                score=score
            )
            record.save()
            return Response(score)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExerciseView(views.APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

    def get(self, request, grade_id, skill_id, format=None):
        skills = Skill.objects.filter(grade__id=grade_id)
        skill = skills.get(id_in_grade=skill_id)
        exercises = Exercise.objects.filter(skill=skill).all()

        exercise = exercises[randint(0, exercises.count() - 1)]

        serializer = ExerciseSerializer(exercise)

        return Response(serializer.data)

    def check_correct_answer(self, request, exercise):
        if exercise.question_type == 'AN':
            if request.data.get('answer') == exercise.answer:
                return True
            else:
                return False
        else:
            if (exercise.question_type == 'SC' or
               exercise.question_type == 'MC'):
                # Check if the size of two lists are the same
                count1 = 0
                for answer in exercise.possible.all():
                    if answer.is_correct_answer:
                        count1 += 1
                count2 = 0
                string_answer = request.data.get('answer')
                list_answer = string_answer.split('|')
                for answer in list_answer:
                    count2 += 1
                if not count1 == count2:
                    return False
                # Check if two lists are equivalent
                for answer in exercise.possible.all():
                    if answer.is_correct_answer:
                        found = False
                        for _answer in list_answer:
                            if _answer == answer.possible_answer:
                                found = True
                                break
                        if not found:
                            return False
                return True
            return False

    def post(self, request, grade_id, skill_id, format=None):
        skills = Skill.objects.filter(grade__id=grade_id)
        skill = skills.get(id_in_grade=skill_id)

        exercise = Exercise.objects.get(skill=skill, id=request.data.get('id'))

        serializer = ExerciseAnswerSerializer(exercise, data=request.data)

        if serializer.is_valid():
            # Save exercise record
            record = ExerciseRecord(
                exercise=exercise,
                user=request.user.profile
            )

            string_answer = request.data.get('answer')
            list_answer = string_answer.split('|')

            if self.check_correct_answer(request, exercise):
                record.score = 10
                record.save()
                for _answer in list_answer:
                    user_answer = UserAnswerRecord(
                        exercise_record=record,
                        answer=_answer
                    )
                    user_answer.save()
                return Response(True)
            else:
                record.score = 0
                record.save()
                for _answer in list_answer:
                    user_answer = UserAnswerRecord(
                        exercise_record=record,
                        answer=_answer
                    )
                    user_answer.save()
                return Response(False)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
