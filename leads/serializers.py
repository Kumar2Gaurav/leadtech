from rest_framework import serializers
from.models import LeadSolution


class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeadSolution
        fields = ('__all__')
