from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import models
from django.db.models import fields

from .models import Book, IssueBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'pk',
            'title',
            'author',
            'isbn',
        )


class IssueBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueBook
        fields = (
            'pk',
            'book_id',
            'issue_time',
            'return_time',
        )