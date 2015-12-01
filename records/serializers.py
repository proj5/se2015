from rest_framework import serializers

from records.models import ExamRecord
from users.serializers import UserAccountSerializer


class ExamRecordSerializer(serializers.ModelSerializer):
    user = UserAccountSerializer()

    class Meta:
        model = ExamRecord
        fields = ('user', 'score', 'done_time')
        read_only_fields = ('user', 'score', 'done_time')
