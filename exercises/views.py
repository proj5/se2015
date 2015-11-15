from rest_framework import viewsets, permissions, views
from rest_framework.response import Response

from exercises.models import Exercise, Skill
from exercises.serializers import ExerciseSerializer, ExerciseAnswerSerializer
from exercises.serializers import SkillSerializer
from rest_framework.response import Response
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

    def get_permission(self):
        if self.request.method == 'GET':
            return (permissions.AllowAny(),)

        return False

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
            if request.data.get('answer') == exercise.answer:
                return Response(True)
            else:
                return Response(False)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillView(views.APIView):

    def get_permission(self):
        if self.request.method == 'GET':
            return (permissions.AllowAny(),)

    def get(self, request, grade_id, format=None):
        skills = Skill.objects.filter(grade__name=grade_id)

        serializer = SkillSerializer(skills, many=True)

        return Response(serializer.data)
