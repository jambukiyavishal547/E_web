from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
# Create your views here.

from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

class StudentApiView(viewsets.ModelViewSet):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer
        #list
        @extend_schema(
            responses={
                status.HTTP_200_OK:  {
                    'description': 'List Of Student ',
                    'example' : {
                            'id': 1,
                            'name': 'vishal',
                            'age': 21,
                            'gender': "M",
                            "is_active":True,
                            "created_at": "2024-06-03",
                            "update_at": "2024-06-03"
                        }
                    }
                }
        )
        def list(self, request):
            """
            Your view's docstring here.
            """
            student = Student.objects.first ()
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        #create
        example = {
            'id': 1,
            'name': 'vishal',
            'age': 21,
            'gender': "M"
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
            Create a new object .
            """
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #update
        @extend_schema(
            request=StudentSerializer,
            responses={
                status.HTTP_200_OK: StudentSerializer,
                status.HTTP_204_NO_CONTENT: None,
            }
        )
        def update(self, request, pk):
            """
            Update an existing object.
            """
            try:
                instance = Student.objects.get(pk=pk)
            except Student.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = StudentSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #delete
        @extend_schema(
            responses={
                status.HTTP_200_OK:  {
                    'description': 'Object deleted ',
                    'example' : {
                            'Result':'Object deleted ',
                            'id': 1
                        }
                    },
                status.HTTP_202_ACCEPTED: { 
                    'description': 'Give Only Id Of Object Like',
                    'example' : {
                    'description': 'Give Only Id Of Object ',
                            'id': 1,
                        }},
                status.HTTP_204_NO_CONTENT: {
                    'description': 'Give Id ',
                    'example' : {
                    'description': 'Input Somthing Like  ',
                            'id': 1,
                        }
                    }
            }
        )
        def destroy(self, request, pk):
            """
            Delete an existing object.
            """
            try:
                instance = Student.objects.get(pk=pk)
            except Student.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)