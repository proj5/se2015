from rest_framework import viewsets, permissions, views
from rest_framework.response import Response

from exercises.models import Exercise, Skill
from exercises.serializers import ExerciseSerializer

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
        # print(serializer.data)
        return Response(serializer.data)
