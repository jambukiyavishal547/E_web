from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from .authentication import UsernamePasswordAuthentication
from .permissions import IsAdminUser
from drf_spectacular.utils import extend_schema

class StudentApiView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [UsernamePasswordAuthentication]
    permission_classes = [IsAdminUser]

    @extend_schema(
        responses={
            status.HTTP_200_OK: {
                'description': 'List Of Students',
                'example': {
                    'id': 1,
                    'name': 'demo',
                    'pwd':'password',
                    'age': 0,
                    'gender': 'M',
                    'is_active': True,
                    'created_at': '2024-06-03',
                    'updated_at': '2024-06-03'
                }
            }
        }
    )
    def list(self, request):
        """
        List all students.
        """
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    example = {
        'name': 'demo',
        'password':"password",
        'age': 0,
        'gender': 'M',
        'is_active': True
    }

    @extend_schema(
        request={"application/json": {'example': example, 'description': 'Student object to be created'}},
        responses={
            status.HTTP_201_CREATED: {
                'description': 'Student created successfully',
                'example': example
            }
        }
    )
    def create(self, request):
        """
        Create a new student.
        """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request={"application/json": {'example': example, 'description': 'Student object to be updated'}},
        responses={
            status.HTTP_200_OK: {
                'description': 'Student updated successfully',
                'example': {
                    'id': 1,
                    'name': 'demo',
                    "password":"password",
                    'age': 0,
                    'gender': 'M',
                    'is_active': True,
                    'created_at': '2024-06-03',
                    'updated_at': '2024-06-03'
                }
            }
        }
    )
    def update(self, request, pk=None, partial=False):
        """
        Update an existing student.
        """
        try:
            instance = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: {
                'description': 'Student deleted successfully',
                'example': {
                    'id': 1
                }
            }
        }
    )
    def destroy(self, request, pk=None):
        """
        Delete a student.
        """
        try:
            instance = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
