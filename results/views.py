from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookDetails(APIView):
    def get(self, request, Title, Author):
        try:
            student = Book.objects.get(title=Title, author=Author)
            serializer = BookSerializer(student)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)