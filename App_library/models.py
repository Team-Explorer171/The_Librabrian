from django.db import models
from datetime import date


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.title}"


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='book_cover')
    author = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=25000, blank=True, null=True)
    available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"'{self.title}' by '{self.author}'"


class Student(models.Model):
    student_id = models.CharField(max_length=255, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    section = models.CharField(max_length=10)
    year = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=25)
