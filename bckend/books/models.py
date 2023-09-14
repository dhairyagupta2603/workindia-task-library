from django.db import models
from django.db.models import CharField, ForeignKey, DateTimeField

class Book(models.Model):
    title = CharField(max_length=200)
    author = CharField(max_length=200)
    isbn = CharField(max_length=200)


    def __str__(self) -> str:
        return f'{self.title}: {self.author}'
    
    
class IssueBook(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_time = DateTimeField()
    return_time = DateTimeField()

    def __str__(self) -> str:
        return f'{self.book_id}: {self.issue_time} - {self.return_time}'
    
