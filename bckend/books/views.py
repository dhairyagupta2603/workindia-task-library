from datetime import datetime
import json

from rest_framework import generics, mixins, permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets 

from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Book, IssueBook
from .serializers import BookSerializer, IssueBookSerializer
# from api.mixins import StaffEditorPermissinMixin


class BookAddAPIView(generics.GenericAPIView):
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()

        print('BOOK: ', book)

        return Response({
            'message': 'Book added successfuly',
        'book_id': BookSerializer(instance=book, context=self.get_serializer_context()).data['pk'],
        })

class BookSearchAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
         params = request.GET.get('title', None)[:-1]
         print(params)

         if params is not None:
              books = Book.objects.filter(title__icontains=params)
              print('BOOKS:', books)
              serializer = self.get_serializer(books, many=True)
              print('BOOKS:', serializer)
              return Response({'results': serializer.data})
    
         return super().list(request, *args, **kwargs)


class BookAvailiblityAPIView(generics.RetrieveAPIView):
    queryset = IssueBook.objects.all()
    serializer_class = IssueBookSerializer
    lookup_field = 'pk'

    def retrieve(self, request, pk=None, *args, **kwargs):
            current_time = datetime.now()
            print('PK', pk)
            issue = IssueBook.objects.filter(book_id=pk).exclude(
                Q(issue_time__lte=current_time) & 
                Q(return_time__gte=current_time)
            )
            print(issue)

            if len(issue) == 0:
                book_data = Book.objects.get(pk=issue)
                print(book_data)

                return Response({
                     'book_id':book_data,
                #     'issue_time': data['issue_time'],
                #     'return_time': data['return_time'],
                })
                 
            serializer = IssueBookSerializer(instance=issue, many=True)


            data1 = dict(serializer.data[0])
            bookid=data1['book_id']

            book_data = Book.objects.get(pk=bookid)
            return Response({
                'book_id': book_data.pk,
                'title': book_data.title,
                'author': book_data.author,
                'available': True,
            })


class BookBorrowAPIView(generics.GenericAPIView):
    queryset = IssueBook.objects.all()
    serializer_class = IssueBookSerializer

    def update(self, request, pk=None, *args, **kwargs):
         print(request.data)
         bookissue = IssueBook.objects.get(id=pk)
         serializer = IssueBookSerializer(instance=bookissue, data=request.data)

         serializer.is_valid()
         serializer.save()
         return Response(serializer.data)
    
