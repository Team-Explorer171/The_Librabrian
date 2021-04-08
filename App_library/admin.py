from django.contrib import admin
from App_library.models import Student, Book, Borrow, Category

# Register your models here.
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Category)
