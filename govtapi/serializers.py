from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'institution_id',
                  'student_id', 'name', 'other_details']

    def validate_institution_id(self, value):
        if len(value) != 4:
            raise serializers.ValidationError(
                'Instituition Id has to be 4 characters long')
        elif value.isalpha() == False:
            raise serializers.ValidationError(
                'Institution Id has illegal characters')
        return value
