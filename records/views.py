from rest_framework import permissions, views
from rest_framework.response import Response

from records.models import ExerciseRecord, ExamRecord
from records.serializers import ExamRecordOneUserSerializer
from records.serializers import ExamRecordSerializer


class ExamRecordView(views.APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

    def get(self, request, exam_id):
        # Each exam record has primary key (exam, user) so need to use filter
        records = ExamRecord.objects.filter(exam__id=exam_id).all()
        serializer = ExamRecordSerializer(records, many=True)
        return Response(serializer.data)


class ExerciseRecordView(views.APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

    def get(self, request, username):
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


class ExamRecordUserView(views.APIView):

    def get_permissions(self):
        return (permissions.IsAuthenticated(),)

    def get(self, request, exam_id, format=None):
        try:
            record = ExamRecord.objects.get(
                exam__id=exam_id,
                user=request.user.profile
            )
            serializer = ExamRecordOneUserSerializer(record)
            return Response(serializer.data)
        except ExamRecord.DoesNotExist:
            return Response(False)
