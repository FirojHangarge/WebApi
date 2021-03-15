from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer



# Create your views here.

# class employeeList(APIView):
#
#     def get(self, request):
#         employee1= Employee.objects.all()
#         serializer= EmployeeSerializer(employee1,many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         try:
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             print(e)
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#
#     # def delete(self, request):

@api_view(['GET', 'POST'])
def employeeList(request):
        """
        List all code snippets, or create a new snippet.
        """
        if request.method == 'GET':
            snippets = Employee.objects.all()
            serializer = EmployeeSerializer(snippets, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class employeeList(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return EmployeeSerializer.objects.get(pk=pk)
#         except EmployeeSerializer.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = EmployeeSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = EmployeeSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


