from rest_framework import permissions, views
from rest_framework.response import Response

from records.models import ExerciseRecord


class ExerciseRecordView(views.APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

    def get(self, request, username):
        print username
        records = ExerciseRecord.objects.filter(user__user__username=username)
        count_correct_answer = 0
        count_wrong_answer = 0
        total_score = 0
        total_record = 0
        for record in records:
            total_score += record.score
            total_record += 1
            if (record.score == 0):
                count_wrong_answer += 1
            else:
                count_correct_answer += 1
        return Response({
            "total_score": total_score,
            "total_record": total_record,
            "count_correct_answer": count_correct_answer,
            "count_wrong_answer": count_wrong_answer})
