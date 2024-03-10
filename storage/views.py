from storage.serializers import SearchSerializer, FileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from storage.models import File, Subjects, Categories
from rest_framework.permissions import (IsAuthenticated,)


class SearchRetrieveView(APIView):
    #permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = SearchSerializer(data=request.data)
        if serializer.is_valid():
            queryset = File.objects.all()
            if (string := serializer.validated_data.get('subject')) is not None:
                queryset = queryset.filter(subject=Subjects[string])
            
            if (string := serializer.validated_data.get('name')) is not None:
                queryset = queryset.filter(name__icontains=string)

            if (string := serializer.validated_data.get('author')) is not None:
                queryset = queryset.filter(author__icontains=string)

            if (set := serializer.validated_data.get('categories')) is not None:
                categories = [Categories[string] for string in set]
                queryset = queryset.filter(category__in=categories)

            return Response({'files': FileSerializer(queryset, many=True).data}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)