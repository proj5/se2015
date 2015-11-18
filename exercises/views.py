from rest_framework import viewsets, permissions, views
from rest_framework.response import Response

from exercises.models import Exercise, Skill, Grade
from exercises.serializers import ExerciseSerializer, ExerciseAnswerSerializer
from exercises.serializers import SkillSerializer, GradeSerializer
from records.models import ExerciseRecord
from rest_framework import status

from random import randint


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), )


class ExerciseView(views.APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

    def get(self, request, grade_id, skill_id, format=None):
        skills = Skill.objects.filter(grade__name=grade_id)
        skill = skills.get(id_in_grade=skill_id)
        exercises = Exercise.objects.filter(skill=skill).all()

        exercise = exercises[randint(0, exercises.count() - 1)]

        serializer = ExerciseSerializer(exercise, data=request.data)

        return Response(serializer.data)

    def post(self, request, grade_id, skill_id, format=None):
        skills = Skill.objects.filter(grade__name=grade_id)
        skill = skills.get(id_in_grade=skill_id)

        exercise = Exercise.objects.get(skill=skill, id=request.data.get('id'))

        serializer = ExerciseAnswerSerializer(exercise, data=request.data)

        if serializer.is_valid():
            # Save record
            record = ExerciseRecord(
                exercise=exercise,
                answer=request.data.get('answer'),
                user=request.user.profile
            )

            if request.data.get('answer') == exercise.answer:
                record.score = 10
                record.save()
                return Response(True)
            else:
                record.score = 0
                record.save()
                return Response(False)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillView(views.APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), )

    def get(self, request, grade_id, format=None):
        skills = Skill.objects.filter(grade__name=grade_id)

        serializer = SkillSerializer(skills, many=True)

        return Response(serializer.data)


class GradeView(views.APIView):

    def get_permissions(self):
        if self.request.method in 'GET':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), )

    def get(self, request, format=None):
        grades = Grade.objects.all()

        serializer = GradeSerializer(grades, many=True)

        return Response(serializer.data)
