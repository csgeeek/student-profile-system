from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from .permissions import CustomPermission

from .models import Student
from .serializers import StudentSerializer
# Create your views here.


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [CustomPermission]
